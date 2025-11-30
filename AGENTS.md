# Agent Instructions for vietlott-data

## Quick Reference (Build/Lint/Test)
- **Test all**: `uv run pytest src/vietlott/tests`
- **Test single**: `uv run pytest path/to/test.py::test_function`
- **Lint**: `uv run ruff check --select I --fix ./src && uv run ruff format ./src`
- **Build**: `make build` (includes lint and test)

## Project Overview
This project is a Python-based data pipeline that automatically crawls, analyzes, and stores Vietnamese lottery data from the official Vietlott website. It provides a command-line interface (CLI) for manual data crawling and backfilling, and it is configured to run daily using GitHub Actions.

The project is well-structured, with clear separation of concerns between data crawling, configuration, and command-line interfaces. It uses modern Python libraries such as `requests`, `beautifulsoup4`, `pandas`, `click`, and `pendulum`.

## Architecture
The project is quite simple with all sources are in `/src`.
You can start with `/src/cli` to check what are available and start there.

### Product Config
The process of adding new product is designed to be easy via a config-first approach.
The base config is at `vietlott.config.products.ProductConfig`, with settings mostly works for all products of Vietlott.

Key points:
- Cookies used to be needed to crawl but not anymore (disabled for all products).
- Data on website are in pages so the fetching are designed around that mechanism (also the detect missing and back-filled mechanism at `missing.py`).

### Runner
The project uses Github Actions with config to schedule the run daily to crawl & push to itself. So no server required.

## Development Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vietvudanh/vietlott-data.git
    cd vietlott-data
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    make requirements-dev
    ```

### Running the Crawler
The primary entry point for data crawling is the `vietlott-crawl` command.
To crawl data for a specific product:
```bash
source .venv/bin/activate
vietlott-crawl <PRODUCT_NAME>
```
Example: `vietlott-crawl keno`

### Generating README (project frontpage)
This repository includes a script that generates an updated `readme.md` for the project's frontpage. The `uv` task alias used in the docs may not be defined in all environments — run the script directly with Python:

```bash
python src/render_readme.py
```

If you prefer a shortcut you can add a script entry to `pyproject.toml` under `[project.scripts]` or create a `uv` task. The recommended script name is `vietlott-render-readme`.

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
- **Automation**: GitHub Actions workflow in `.github/workflows/crawl.yaml`