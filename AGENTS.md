# Agent Instructions for vietlott-data

## Build/Lint/Test Commands
- **Test all**: `uv run pytest src/vietlott/tests`
- **Test single**: `uv run pytest path/to/test.py::test_function`
- **Lint**: `uv run ruff check --select I --fix ./src && uv run ruff format ./src`
- **Build**: `make build` (includes lint and test)

## Code Style Guidelines
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
- **Modular design**: Separate concerns with crawler, model, and CLI modules</content>
<parameter name="filePath">/Users/vietvu/works/github.com/vietvudanh/vietlott-data/AGENTS.md