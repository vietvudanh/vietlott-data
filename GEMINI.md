# Gemini Code Assistant Context

## Project Overview

This project is a Python-based data pipeline that automatically crawls, analyzes, and stores Vietnamese lottery data from the official Vietlott website. It provides a command-line interface (CLI) for manual data crawling and backfilling, and it is configured to run daily using GitHub Actions.

The project is well-structured, with clear separation of concerns between data crawling, configuration, and command-line interfaces. It uses modern Python libraries such as `requests`, `beautifulsoup4`, `pandas`, `click`, and `pendulum`.

## Building and Running

### Development Setup

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

The primary entry point for data crawling is the `vietlott-crawl` command, which is defined in `pyproject.toml` and implemented in `src/vietlott/cli/crawl.py`.

To crawl data for a specific product, you can run:

```bash
source .venv/bin/activate
vietlott-crawl <PRODUCT_NAME>
```

For example, to crawl Keno data, you would run:

```bash
vietlott-crawl keno
```

### Running Tests

The project uses `pytest` for testing. To run the test suite, use the following command:

```bash
make test
```

### Linting and Formatting

The project uses `ruff` for linting and formatting. To check and fix the code style, run:

```bash
make lint
```

## Development Conventions

*   **Configuration:** The project uses a centralized configuration system in `src/vietlott/config` to manage lottery product details and class mappings.
*   **Crawling Logic:** The core data crawling logic is implemented in the `src/vietlott/crawler` directory, with a base class and specific implementations for each lottery product.
*   **CLI:** The command-line interface is built using `click` and is defined in the `src/vietlott/cli` directory.
*   **Automation:** The project is configured to run daily using a GitHub Actions workflow defined in `.github/workflows/crawl.yaml`.
*   **Dependencies:** Project dependencies are managed using `pyproject.toml` and `uv`.
*   **Makefile:** A `Makefile` is provided with convenient commands for common development tasks such as setting up the environment, running tests, linting, and building the project.
