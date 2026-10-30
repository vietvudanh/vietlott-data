# Vietlott-data Architecture

Production crawling and rendering are implemented in the Go crawler (`/crawler`, binary `bin/vietlott-crawler`). Legacy Python code and the PyPI package live in `/src`.

## Product Configuration

The Go crawler configures products in `crawler/internal/model/product.go` and `crawler/internal/client/products.go`. The legacy Python package uses `vietlott.config.products.ProductConfig`.

Key points:
- Cookies are no longer required for crawling.
- Vietlott serves data across paginated endpoints. The crawler and backfill mechanism are designed around page-based fetching with targeted gap calculation.

## Runner

The Go crawler runs via scheduled execution on local/on-premise hardware (see `bin/github_data.sh` and `Procfile`) and commits updated data back to GitHub. GitHub Actions is no longer used for data crawling because the Vietlott website blocks non-Vietnam IP addresses (see [issue #13](https://github.com/vietvudanh/vietlott-data/issues/13) and [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)).

### Go CLI Commands (Recommended)
- `./bin/vietlott-crawler status`: Compare existing stored draws vs. latest upstream draws.
- `./bin/vietlott-crawler sync --all`: Crawl latest draw results and backfill missing draws.
- `./bin/vietlott-crawler render-readme`: Update `readme.md` with current data statistics.
- `./bin/vietlott-crawler render-docs`: Update `docs/index.html`, English `/en/`, individual product pages, and `docs/sitemap.xml` with current data statistics.

### Legacy Python CLI Commands (Deprecated)
- `vietlott-crawl`: Crawl latest draw results.
- `vietlott-missing`: Detect and backfill missing draws.
- `vietlott-render-readme`: Update repository README with current data statistics.
- `vietlott-render-docs`: Update `docs/index.html` with current data statistics.