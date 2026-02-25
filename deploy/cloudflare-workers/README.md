# Cloudflare Workers Deployment for Vietlott Data Crawler

This directory contains a Cloudflare Worker that serves as a scheduler/trigger for the Vietlott data crawler.

## Important Note

**Cloudflare Workers cannot directly run the Python crawler** because:
- Workers have limited Python support (beta) 
- Heavy libraries like `polars`, `pandas`, `pyarrow` are not supported
- Workers have a 50ms CPU time limit (free tier) or 30s (paid)

Instead, this Worker acts as a **scheduler/trigger** that can:
1. **Trigger GitHub Actions workflow** (recommended, free)
2. **Invoke AWS Lambda function**
3. **Call a custom backend API**

## Architecture Options

### Option 1: Cloudflare Workers → GitHub Actions (Recommended)

```
┌─────────────────────┐    workflow_dispatch    ┌─────────────────────┐
│  Cloudflare Worker  │ ───────────────────────▶│   GitHub Actions    │
│  (Cron Trigger)     │                         │   (Runs crawler)    │
└─────────────────────┘                         └─────────────────────┘
```

This is the **recommended** approach because:
- GitHub Actions is free for public repositories
- No additional infrastructure needed
- Already works with the existing workflow

### Option 2: Cloudflare Workers → AWS Lambda

```
┌─────────────────────┐      HTTP request       ┌─────────────────────┐
│  Cloudflare Worker  │ ───────────────────────▶│    AWS Lambda       │
│  (Cron Trigger)     │                         │   (Runs crawler)    │
└─────────────────────┘                         └─────────────────────┘
```

Use this if you need more control over execution or want to avoid GitHub Actions limits.

## Prerequisites

- Node.js 16+
- Cloudflare account
- Wrangler CLI (`npm install -g wrangler`)
- GitHub Personal Access Token (for GitHub Actions trigger)

## Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Login to Cloudflare

```bash
wrangler login
```

### 3. Set Secrets

For GitHub Actions trigger (recommended):
```bash
wrangler secret put GITHUB_TOKEN
# Paste your GitHub Personal Access Token with 'repo' scope

wrangler secret put TRIGGER_SECRET
# Set a secret for authenticating GET requests
```

For AWS Lambda trigger:
```bash
wrangler secret put AWS_LAMBDA_URL
# Enter your Lambda function URL
```

### 4. Deploy

```bash
# Development
npm run deploy:dev

# Production
npm run deploy:prod
```

## GitHub Actions Workflow Setup

To use this Worker with GitHub Actions, your workflow file needs to support `workflow_dispatch`:

```yaml
# .github/workflows/crawl.yaml
name: crawl

on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC
  workflow_dispatch:      # Allow manual/API triggers
    inputs:
      triggered_by:
        description: 'Source of the trigger'
        required: false
        default: 'manual'

jobs:
  crawl:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run crawler
        run: |
          export PYTHONPATH=src
          bash bin/github_data.sh
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/status` | GET | Configuration status |
| `/trigger` | POST | Trigger the crawler |
| `/trigger?secret=xxx` | GET | Trigger with secret authentication |

## Configuration

Edit `wrangler.toml` to customize:

```toml
[vars]
GITHUB_REPO = "your-username/vietlott-data"
GITHUB_WORKFLOW = "crawl.yaml"

[triggers]
crons = ["0 0 * * *"]  # Daily at midnight UTC
```

## Cron Schedule

The Worker uses Cloudflare Cron Triggers. Default schedule is daily at midnight UTC.

Common cron patterns:
- `0 0 * * *` - Daily at midnight UTC
- `0 */6 * * *` - Every 6 hours
- `0 0 * * 1-5` - Weekdays only at midnight

## Local Development

```bash
npm run dev
```

Then test with:
```bash
curl http://localhost:8787/health
curl -X POST http://localhost:8787/trigger
```

## Costs

**Cloudflare Workers Free Tier:**
- 100,000 requests/day
- 10ms CPU time per request
- Unlimited scheduled invocations

This is more than enough for a daily crawler trigger!

## Troubleshooting

### "Failed to trigger GitHub workflow"

1. Verify your GitHub token has `repo` scope
2. Check the workflow file name matches
3. Ensure `workflow_dispatch` is in your workflow triggers

### "Not configured" error

Set the required secrets:
```bash
wrangler secret put GITHUB_TOKEN
```

### Cron not triggering

1. Check the cron syntax in `wrangler.toml`
2. Verify the Worker is deployed to production
3. Check Cloudflare dashboard for trigger logs
