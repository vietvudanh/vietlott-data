# Deployment Guide

This document outlines the deployment and scheduling architecture for vietlott-data.

## Architecture & Geo-blocking

The Vietlott web endpoints block HTTP requests originating from IP addresses outside Vietnam (see [issue #13](https://github.com/vietvudanh/vietlott-data/issues/13)). As a result:

- Cloud-hosted runners (such as standard GitHub Actions environments) cannot crawl data from Vietlott directly.
- The crawler is deployed on local/on-premise hardware located in Vietnam.
- Crawled data and updated statistics are committed and pushed back to the GitHub repository.

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (package and project manager)
- Git configured with commit and push permissions to the repository

Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Local Setup

Clone the repository and install dependencies using uv:

```bash
git clone https://github.com/vietvudanh/vietlott-data.git
cd vietlott-data
uv sync --dev
```

## Local Runner Pipeline

The automated crawler runs via `bin/github_data.sh`.

### What the Runner Script Does

1. Pulls the latest changes from `main`:
   ```bash
   git pull --rebase --autostash origin main
   ```
2. Runs the crawler and missing-data detector for all supported products:
   ```bash
   for product in keno power_655 power_645 power_535 3d 3d_pro bingo18; do
     uv run python src/vietlott/cli/crawl.py "$product"
     uv run python src/vietlott/cli/missing.py "$product"
   done
   ```
3. Regenerates repository documentation and web statistics:
   ```bash
   uv run python src/render_readme.py
   uv run python src/render_docs.py
   ```
4. Commits changed data files and documentation, then pushes to `origin main`.

### Scheduling

The runner can be scheduled via cron or a task runner (see `Procfile`):

```cron
0 * * * * cd /path/to/vietlott-data && bash bin/github_data.sh
```

On macOS, you can alternatively use `launchd` or a cron entry via `crontab -e`.
On Linux, a systemd timer or cron job can execute the script at your desired interval.

## Manual Execution with uv

To run tasks manually using uv:

### Crawl Latest Draws
```bash
uv run vietlott-crawl keno
uv run vietlott-crawl power_655
uv run vietlott-crawl power_645
```

### Backfill Missing Draws
```bash
uv run vietlott-missing power_655 --limit 50
```

### Update Documentation
```bash
# Update repository README with current data statistics
uv run vietlott-render-readme

# Update docs/index.html with current data statistics
uv run vietlott-render-docs
```

### Run Tests and Linter
```bash
# Run test suite
uv run pytest

# Lint and format
uv run ruff check --select I --fix ./src
uv run ruff format ./src
```

## Other Deployments

### GitHub Pages (Static Documentation)
- Workflow: `.github/workflows/deploy-pages.yml`
- Deploys the static web visualization in `docs/` to GitHub Pages.
- Runs on a daily schedule and can be manually dispatched.

### PyPI Publishing
- Workflow: `.github/workflows/publish-to-pypi.yaml`
- Automatically triggers when a new version tag starting with `v` (e.g. `v0.2.7`) is pushed to GitHub.
