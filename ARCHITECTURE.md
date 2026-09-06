# Vietlott-data Architecture

All source code is located in `/src`. CLI entry points are in `/src/vietlott/cli`.

## Product Configuration

Adding new products uses a config-first approach centered on `vietlott.config.products.ProductConfig`.

Key points:
- Cookies are no longer required for crawling.
- Vietlott serves data across paginated endpoints. The crawler and backfill mechanism (`missing.py`) are designed around page-based fetching.

## Runner

The crawler runs via scheduled execution on local/on-premise hardware (see `bin/github_data.sh` and `Procfile`) and commits updated data back to GitHub. GitHub Actions is no longer used for data crawling because the Vietlott website blocks non-Vietnam IP addresses (see [issue #13](https://github.com/vietvudanh/vietlott-data/issues/13) and [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)).

Available CLI commands:
- `vietlott-crawl`: Crawl latest draw results.
- `vietlott-missing`: Detect and backfill missing draws.
- `vietlott-render-readme`: Update repository README with current data statistics.
- `vietlott-render-docs`: Update docs/index.html with current data statistics.