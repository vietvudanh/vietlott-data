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
 		&& uv pip install -r requirements-dev.txt \
   		&& uv pip install -e .

.PHONY: test
test:
	source $(VENV_DIR)/bin/activate \
	&& pytest src/vietlott/tests

lint: .venv
	@echo "Linting..."
	source $(VENV_DIR)/bin/activate && ruff check --select I --fix ./src && ruff format ./src

build: lint tests
	@echo "Building..."
	source $(VENV_DIR)/bin/activate && python3 -m build
	source $(VENV_DIR)/bin/activate && python3 -m bdist_wheel

pypi: build
	@echo "Publishing..."
	source $(VENV_DIR)/bin/activate && python3 -m twine upload --repository pypi dist/*

run-crawl: .venv
	@echo "Running script..."
	source $(VENV_DIR)/bin/activate && LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src python src/vietlott/cli/crawl.py keno
	source $(VENV_DIR)/bin/activate && LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src python src/vietlott/cli/crawl.py power_535
	source $(VENV_DIR)/bin/activate && LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src python src/vietlott/cli/crawl.py power_655

run-missing: .venv
	@echo "Running script..."
	source $(VENV_DIR)/bin/activate && LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src python src/vietlott/cli/missing.py keno
	source $(VENV_DIR)/bin/activate && LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src python src/vietlott/cli/missing.py power_535
