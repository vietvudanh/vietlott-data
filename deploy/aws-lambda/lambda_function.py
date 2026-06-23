"""
AWS Lambda function to crawl Vietlott lottery data and push to GitHub.

This function replicates the functionality of bin/github_data.sh for serverless execution.
It can be triggered by CloudWatch Events (scheduled) or manually invoked.

Environment Variables Required:
    - GITHUB_TOKEN: Personal access token with repo write permissions
    - GITHUB_REPO: Repository in format 'owner/repo' (e.g., 'vietvudanh/vietlott-data')
    - GIT_USER_NAME: Git commit author name
    - GIT_USER_EMAIL: Git commit author email
    - DATA_BUCKET: (Optional) S3 bucket for storing data (if not using GitHub as storage)
"""

import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime
from typing import Any

# Add the src directory to the path for local imports
sys.path.insert(0, "/opt/python")
sys.path.insert(0, "/var/task/src")

# Set environment for loguru
os.environ.setdefault("LOGURU_LEVEL", "INFO")


def run_command(cmd: list[str], cwd: str | None = None) -> tuple[int, str, str]:
    """Run a shell command and return exit code, stdout, stderr."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def setup_git(repo_dir: str, user_name: str, user_email: str) -> None:
    """Configure git settings for the repository."""
    run_command(["git", "config", "user.name", user_name], cwd=repo_dir)
    run_command(["git", "config", "user.email", user_email], cwd=repo_dir)


def clone_repository(github_token: str, github_repo: str, target_dir: str) -> bool:
    """Clone the GitHub repository using the provided token."""
    url = f"https://{github_token}@github.com/{github_repo}.git"
    returncode, stdout, stderr = run_command(["git", "clone", "--depth", "1", url, target_dir])
    if returncode != 0:
        print(f"Failed to clone repository: {stderr}")
        return False
    return True


def commit_and_push(repo_dir: str, message: str) -> bool:
    """Commit changes and push to the remote repository."""
    # Add data and readme files
    run_command(["git", "add", "data/"], cwd=repo_dir)
    run_command(["git", "add", "readme.md"], cwd=repo_dir)

    # Check if there are changes to commit
    returncode, stdout, _ = run_command(["git", "status", "--porcelain"], cwd=repo_dir)
    if not stdout.strip():
        print("No changes to commit")
        return True

    # Commit and push
    returncode, _, stderr = run_command(["git", "commit", "-m", message], cwd=repo_dir)
    if returncode != 0:
        print(f"Failed to commit: {stderr}")
        return False

    returncode, _, stderr = run_command(["git", "push"], cwd=repo_dir)
    if returncode != 0:
        print(f"Failed to push: {stderr}")
        return False

    return True


def crawl_all_products(repo_dir: str) -> dict[str, bool]:
    """Crawl all lottery products and return success status for each."""
    from vietlott.cli.crawl import crawl
    from vietlott.cli.missing import detect_missing_data
    from click.testing import CliRunner

    products = ["keno", "power_655", "power_645", "power_535", "3d", "3d_pro", "bingo18"]
    results = {}
    runner = CliRunner()

    # Change to repo directory for correct data paths
    original_cwd = os.getcwd()
    os.chdir(repo_dir)

    try:
        for product in products:
            print(f"Crawling {product}...")
            try:
                # Run crawl
                result = runner.invoke(crawl, [product])
                if result.exit_code != 0:
                    print(f"Crawl failed for {product}: {result.output}")
                    results[f"{product}_crawl"] = False
                else:
                    results[f"{product}_crawl"] = True

                # Run missing data detection
                result = runner.invoke(detect_missing_data, [product])
                if result.exit_code != 0:
                    print(f"Missing detection failed for {product}: {result.output}")
                    results[f"{product}_missing"] = False
                else:
                    results[f"{product}_missing"] = True

            except Exception as e:
                print(f"Error processing {product}: {e}")
                results[f"{product}_crawl"] = False
                results[f"{product}_missing"] = False
    finally:
        os.chdir(original_cwd)

    return results


def render_readme(repo_dir: str) -> bool:
    """Render the README file with updated statistics."""
    original_cwd = os.getcwd()
    os.chdir(repo_dir)

    try:
        from render_readme import main as render_main

        render_main()
        return True
    except Exception as e:
        print(f"Failed to render README: {e}")
        return False
    finally:
        os.chdir(original_cwd)


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """
    AWS Lambda entry point.

    Args:
        event: Lambda event data (can include 'products' list to crawl specific products)
        context: Lambda context object

    Returns:
        Response dict with status and details
    """
    print(f"Starting Vietlott data crawl at {datetime.now().isoformat()}")

    # Get environment variables
    github_token = os.environ.get("GITHUB_TOKEN")
    github_repo = os.environ.get("GITHUB_REPO", "vietvudanh/vietlott-data")
    git_user_name = os.environ.get("GIT_USER_NAME", "Lambda Bot")
    git_user_email = os.environ.get("GIT_USER_EMAIL", "lambda@example.com")

    if not github_token:
        return {"statusCode": 400, "body": json.dumps({"error": "GITHUB_TOKEN environment variable is required"})}

    # Create temporary directory for the repo
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_dir = os.path.join(tmpdir, "repo")

        # Clone repository
        print("Cloning repository...")
        if not clone_repository(github_token, github_repo, repo_dir):
            return {"statusCode": 500, "body": json.dumps({"error": "Failed to clone repository"})}

        # Setup git
        setup_git(repo_dir, git_user_name, git_user_email)

        # Update PYTHONPATH to include the cloned repo
        sys.path.insert(0, os.path.join(repo_dir, "src"))

        # Crawl all products
        print("Crawling lottery data...")
        crawl_results = crawl_all_products(repo_dir)

        # Render README
        print("Rendering README...")
        readme_success = render_readme(repo_dir)

        # Commit and push
        print("Committing and pushing changes...")
        commit_message = f"update data @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        push_success = commit_and_push(repo_dir, commit_message)

        return {
            "statusCode": 200 if push_success else 500,
            "body": json.dumps(
                {
                    "message": "Data crawl completed",
                    "timestamp": datetime.now().isoformat(),
                    "crawl_results": crawl_results,
                    "readme_rendered": readme_success,
                    "pushed": push_success,
                }
            ),
        }


# For local testing
if __name__ == "__main__":
    # Mock context for local testing
    class MockContext:
        function_name = "test"
        memory_limit_in_mb = 128
        invoked_function_arn = "arn:aws:lambda:us-east-1:123456789:function:test"

    result = lambda_handler({}, MockContext())
    print(json.dumps(result, indent=2))
