# Agent Instructions for vietlott-data

## Quick Reference (Build/Lint/Test)
- **Test all**: `uv run pytest src/vietlott/tests`
- **Test single**: `uv run pytest path/to/test.py::test_function`
- **Lint**: `uv run ruff check --select I --fix ./src && uv run ruff format ./src`
- **Build**: `make build` (includes lint and test)

## Project Overview
This project is a Python-based data pipeline that crawls, analyzes, and stores Vietnamese lottery data from the official Vietlott website. It provides a CLI for crawling and backfilling data. Scheduled crawling runs on local/on-premise hardware (as Vietlott blocks non-Vietnam IP addresses) and commits data to GitHub.

The project uses Python libraries including `requests`, `beautifulsoup4`, `polars`, `click`, and `pendulum`.

## Architecture
The project source code is in `/src`. CLI commands are defined in `/src/vietlott/cli`.

### Product Config
Adding new products uses a config-first approach centered on `vietlott.config.products.ProductConfig`.

Key points:
- Cookies are no longer required for crawling.
- Data is fetched by pages, with missing-data detection and backfilling handled in `missing.py`.

### Runner
The crawler runs via a scheduled local runner (`bin/github_data.sh` / `Procfile`) and commits new data to GitHub. GitHub Actions is no longer used for crawling due to Vietlott IP geo-blocking. See `docs/DEPLOYMENT.md` for full deployment details.

## Development Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vietvudanh/vietlott-data.git
    cd vietlott-data
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    uv sync --dev
    ```

### Running the Crawler
The primary entry point for data crawling is the `vietlott-crawl` command.
To crawl data for a specific product:
```bash
uv run vietlott-crawl <PRODUCT_NAME>
```
Example: `uv run vietlott-crawl keno`

### Generating README and Docs (project frontpage and GitHub Pages)
This repository includes scripts that generate updated documentation with current data:

1. **Generate README** (project frontpage):
```bash
python src/render_readme.py
# or using the CLI command:
vietlott-render-readme
```

2. **Generate docs/index.html** (GitHub Pages):
```bash
python src/render_docs.py
# or using the CLI command:
vietlott-render-docs
```

Both scripts read data from the `data/` folder and update their respective files with current statistics. This ensures the documentation stays synchronized with the actual data.

### Running Tests
```bash
make test
```

### Linting and Formatting
```bash
make lint
```

## Release Process
To publish a new version to PyPI:
1. Update the version in `pyproject.toml`
2. Commit the version change
3. Create and push a git tag starting with `v`:
   ```bash
   git tag v0.1.4
   git push origin v0.1.4
   ```
4. The GitHub Actions workflow will automatically build and publish to PyPI.

## Code Style & Conventions
- **Python version**: 3.11+
- **Line length**: 120 characters (enforced by ruff)
- **Imports**: stdlib → third-party → local, separated by blank lines
- **Type hints**: Required for function parameters and return types
- **Data structures**: Use `attrs`/`cattrs` for schemas, `polars` for dataframes
- **Data format**: NDJSON for data storage (use `pl.read_ndjson()`/`pl.write_ndjson()`)
- **Logging**: Use `loguru` logger
- **Paths**: Use `pathlib` for file operations
- **Dates**: Use `pendulum` for date/time handling
- **CLI**: Use `click` for command-line interfaces
- **Naming**: Descriptive snake_case for variables/functions, PascalCase for classes
- **Error handling**: Log errors with context, continue on individual failures, raise `ValueError` for invalid states
- **Validation**: Use assertions for critical checks
- **Docstrings**: Required for public functions and classes
- **Comments**: Avoid unless absolutely necessary for complex logic
- **Testing**: Use descriptive test names, print success messages, test data structures thoroughly

## Project Structure
- **Source code**: All code in `/src` directory
- **CLI entry points**: Available via `vietlott-crawl` and `vietlott-missing` commands
- **Config-first approach**: Add new products via configuration in `vietlott.config.products`
- **Modular design**: Separate concerns with crawler, model, and CLI modules
- **Configuration**: Centralized configuration system in `src/vietlott/config`
- **Crawling Logic**: Core logic in `src/vietlott/crawler`
- **Automation**: Scheduled local crawler via `bin/github_data.sh` and `Procfile`