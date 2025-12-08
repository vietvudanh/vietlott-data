# Serverless Deployment for Vietlott Data Crawler

This directory contains deployment configurations for running the Vietlott data crawler (`bin/github_data.sh`) on free serverless platforms.

## Overview

The original `bin/github_data.sh` script performs the following tasks:
1. Crawls lottery data for all products (keno, power_655, power_645, power_535, 3d, 3d_pro, bingo18)
2. Runs missing data detection and backfills
3. Regenerates the README with updated statistics
4. Commits and pushes changes to GitHub

## Deployment Options

### 1. GitHub Actions (Already Configured ✅)

**Location:** `.github/workflows/crawl.yaml`

This is the **simplest and recommended** option for this project:
- ✅ Free for public repositories
- ✅ No external infrastructure needed
- ✅ Already integrated with the repository
- ✅ Automatic commits and pushes

**Schedule:** Daily at midnight UTC (7:00 AM Vietnam time)

**Manual Trigger:**
```bash
# Using GitHub CLI
gh workflow run crawl.yaml

# Using curl
curl -X POST \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/vietvudanh/vietlott-data/actions/workflows/crawl.yaml/dispatches \
  -d '{"ref":"main"}'
```

### 2. AWS Lambda

**Location:** `deploy/aws-lambda/`

For running the crawler as a standalone Lambda function:
- ✅ Full Python support with all libraries
- ✅ Up to 15 minutes execution time
- ✅ Free tier: 1 million requests/month
- ⚠️ Requires AWS account setup
- ⚠️ Need to manage Lambda layers for dependencies

See [AWS Lambda README](./aws-lambda/README.md) for detailed setup.

### 3. Cloudflare Workers

**Location:** `deploy/cloudflare-workers/`

Acts as a scheduler to trigger GitHub Actions or AWS Lambda:
- ✅ Free tier: 100K requests/day
- ✅ Cron Triggers for scheduling
- ⚠️ Cannot run Python code directly (limited support)
- ⚠️ Requires another service to run the actual crawler

See [Cloudflare Workers README](./cloudflare-workers/README.md) for detailed setup.

## Comparison Table

| Platform | Direct Python | Free Tier | Max Duration | Setup Complexity |
|----------|---------------|-----------|--------------|------------------|
| GitHub Actions | ✅ Full | ✅ Unlimited (public) | 6 hours | ⭐ Easy |
| AWS Lambda | ✅ Full | ✅ 1M requests | 15 minutes | ⭐⭐⭐ Medium |
| Cloudflare Workers | ❌ Limited | ✅ 100K/day | 30 seconds | ⭐⭐ Easy |

## Recommended Architecture

For most use cases, the **GitHub Actions workflow** is the best choice:

```
┌─────────────────────────────────────────────────────────────────┐
│                        GitHub Actions                            │
│                                                                   │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐   │
│  │  Crawl   │ ──▶│  Missing │ ──▶│  Render  │ ──▶│  Commit  │   │
│  │  Data    │    │  Check   │    │  README  │    │  & Push  │   │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘   │
│                                                                   │
│  Triggered by: Schedule (cron) or API (workflow_dispatch)        │
└─────────────────────────────────────────────────────────────────┘
```

### Alternative: Cloudflare + GitHub Actions

If you want external monitoring or custom scheduling:

```
┌─────────────────┐    workflow_dispatch    ┌─────────────────────┐
│   Cloudflare    │ ───────────────────────▶│   GitHub Actions    │
│   Worker        │         API             │   (Full crawler)    │
│   (Scheduler)   │                         │                     │
└─────────────────┘                         └─────────────────────┘
```

## Quick Start

### Option A: Use GitHub Actions (Recommended)

1. The workflow is already configured at `.github/workflows/crawl.yaml`
2. It runs automatically daily
3. To trigger manually: `gh workflow run crawl.yaml`

### Option B: Add Cloudflare Scheduler

1. Deploy the Worker:
   ```bash
   cd deploy/cloudflare-workers
   npm install
   wrangler login
   wrangler secret put GITHUB_TOKEN
   npm run deploy:prod
   ```

2. The Worker will trigger GitHub Actions daily

### Option C: Use AWS Lambda

1. Deploy to Lambda:
   ```bash
   cd deploy/aws-lambda
   chmod +x build_and_deploy.sh
   ./build_and_deploy.sh --create
   ```

2. Set environment variables and schedule

## Environment Variables

| Variable | Description | Used By |
|----------|-------------|---------|
| `GITHUB_TOKEN` | Personal access token with `repo` scope | All |
| `GITHUB_REPO` | Repository in format `owner/repo` | Lambda, Worker |
| `GIT_USER_NAME` | Git commit author name | Lambda |
| `GIT_USER_EMAIL` | Git commit author email | Lambda |
| `AWS_LAMBDA_URL` | Lambda function URL (for Worker trigger) | Worker |

## Monitoring

### GitHub Actions
- View runs: https://github.com/vietvudanh/vietlott-data/actions
- Badge: `[![crawl](https://github.com/vietvudanh/vietlott-data/workflows/crawl/badge.svg)](https://github.com/vietvudanh/vietlott-data/actions)`

### AWS Lambda
```bash
aws logs tail /aws/lambda/vietlott-data-crawler --follow
```

### Cloudflare Workers
```bash
wrangler tail
```
