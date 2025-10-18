---
applyTo: '**/*.py'
---
# Instructions for AI agents

## Project description
Python code to crawl data about lottery from Vietlott.vn

**DO NOT** attempt to change `/readme.md` as it is generated via `/src/render_readme.py`


## Dev environment tips
- Always use `uv` for package management and run python command (`uv run python`)
- Add 

# Styling rules
- Always use Python type hint
- Always activate virtualenv before running command. (`source .venv/bin/activate.fish`)
- Always run `make lint` all code changes.

# Testing instruction

## 1. run test

Run tests as follow to make sure code works
```shell
PYTHON_PATH=src uv run pytest -q src/vietlott/tests
```

## 2. To verify main flow works
Always run `uv run python src/render_readme.py` after code changes.
Always run `uv run python src/vietlott/cli/crawl.py power_645` after code changes.

