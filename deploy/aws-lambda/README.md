# AWS Lambda Deployment for Vietlott Data Crawler

This directory contains the AWS Lambda deployment files for running the Vietlott data crawler on a serverless infrastructure.

## Overview

The Lambda function replicates the functionality of `bin/github_data.sh`:
1. Clones the vietlott-data repository
2. Crawls all lottery products (keno, power_655, power_645, power_535, 3d, 3d_pro, bingo18)
3. Runs missing data detection for each product
4. Regenerates the README with updated statistics
5. Commits and pushes changes back to GitHub

## Prerequisites

- AWS CLI configured with appropriate credentials
- Python 3.11+
- AWS SAM CLI (for SAM deployment) or standard deployment script
- GitHub Personal Access Token with `repo` scope

## Files

- `lambda_function.py` - Main Lambda function handler
- `build_and_deploy.sh` - Shell script for building and deploying
- `template.yaml` - AWS SAM template for infrastructure as code deployment

## Deployment Options

### Option 1: Using AWS SAM (Recommended)

1. Install AWS SAM CLI:
   ```bash
   pip install aws-sam-cli
   ```

2. Build the Lambda layer:
   ```bash
   mkdir -p layer/python
   pip install --platform manylinux2014_x86_64 \
       --target layer/python \
       --implementation cp \
       --python-version 3.11 \
       --only-binary=:all: \
       -r ../../requirements.txt
   ```

3. Deploy using SAM:
   ```bash
   sam deploy --guided \
       --parameter-overrides \
       GithubToken=your_github_token \
       GithubRepo=vietvudanh/vietlott-data \
       GitUserName="Your Name" \
       GitUserEmail=your@email.com
   ```

### Option 2: Using Build Script

1. Make the script executable:
   ```bash
   chmod +x build_and_deploy.sh
   ```

2. Run the deployment (the script will create the IAM role automatically if needed):
   ```bash
   ./build_and_deploy.sh --create
   ```

   Optionally, specify a custom IAM role name:
   ```bash
   AWS_LAMBDA_ROLE=my-custom-role ./build_and_deploy.sh --create
   ```

3. Set environment variables:
   ```bash
   aws lambda update-function-configuration \
       --function-name vietlott-data-crawler \
       --environment 'Variables={GITHUB_TOKEN=your_token,GITHUB_REPO=vietvudanh/vietlott-data,GIT_USER_NAME=Lambda Bot,GIT_USER_EMAIL=bot@example.com,LOGURU_LEVEL=INFO,PYTHONPATH=/opt/python:/var/task/src}'
   ```

## Setting Up Scheduled Execution

To run the crawler daily (like the original GitHub Actions workflow):

```bash
# Create a CloudWatch Events rule
aws events put-rule \
    --name vietlott-daily-crawl \
    --schedule-expression "rate(1 day)" \
    --description "Daily Vietlott data crawl"

# Add Lambda as target
aws events put-targets \
    --rule vietlott-daily-crawl \
    --targets "Id"="1","Arn"="arn:aws:lambda:us-east-1:YOUR_ACCOUNT_ID:function:vietlott-data-crawler"

# Grant permission to CloudWatch to invoke Lambda
aws lambda add-permission \
    --function-name vietlott-data-crawler \
    --statement-id vietlott-daily-crawl \
    --action lambda:InvokeFunction \
    --principal events.amazonaws.com \
    --source-arn arn:aws:events:us-east-1:YOUR_ACCOUNT_ID:rule/vietlott-daily-crawl
```

## Manual Invocation

To manually trigger the Lambda function:

```bash
aws lambda invoke \
    --function-name vietlott-data-crawler \
    --payload '{}' \
    response.json

cat response.json
```

## Configuration

| Environment Variable | Description | Required |
|---------------------|-------------|----------|
| `GITHUB_TOKEN` | GitHub Personal Access Token with repo write permissions | Yes |
| `GITHUB_REPO` | Repository in format 'owner/repo' | Yes |
| `GIT_USER_NAME` | Git commit author name | No (default: Lambda Bot) |
| `GIT_USER_EMAIL` | Git commit author email | No (default: lambda@example.com) |
| `LOGURU_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | No (default: INFO) |

## Costs

AWS Lambda pricing (as of 2024):
- First 1 million requests per month: **Free**
- Memory: $0.0000166667 per GB-second
- Duration: Based on memory and execution time

With 1GB memory and ~10 minute execution time per day:
- Monthly cost: ~$0.10 or less (within free tier for most usage)

## Troubleshooting

1. **Timeout errors**: Increase the function timeout (max 15 minutes)
2. **Memory errors**: Increase memory allocation
3. **Git push failures**: Verify GitHub token has `repo` scope
4. **Import errors**: Check that the layer is properly attached

## Monitoring

View logs in CloudWatch Logs:
```bash
aws logs tail /aws/lambda/vietlott-data-crawler --follow
```
