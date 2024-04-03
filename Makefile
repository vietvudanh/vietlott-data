# Makefile
VENV_DIR := .venv
LINTER := ruff  # Replace this with the packages you need
LOGURU_LEVEL := INFO

all: venv lint run
.PHONY: lint  run

.venv:
	@echo "Initializing virtual environment..."
	uv venv

requirements-dev: .venv
	source $(VENV_DIR)/bin/activate \
 		&& uv pip compile --extra dev pyproject.toml > requirements-dev.txt \
 		&& uv pip install -r requirements-dev.txt

tests:
	source $(VENV_DIR)/bin/activate \
	&& pytest src/vietlott/tests

lint: .venv
	@echo "Linting..."
	source $(VENV_DIR)/bin/activate && ruff check . && ruff format .

build: lint tests
	@echo "Building..."
	source $(VENV_DIR)/bin/activate && python3 -m build

pypi: build
	@echo "Publishing..."
	source $(VENV_DIR)/bin/activate && python3 -m twine upload --repository testpypi dist/*

run-crawl: .venv
	@echo "Running script..."
	source $(VENV_DIR)/bin/activate && LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src python src/vietlott/cli/crawl.py keno

run-missing: .venv
	@echo "Running script..."
	source $(VENV_DIR)/bin/activate && LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src python src/vietlott/cli/missing.py keno
