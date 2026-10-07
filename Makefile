# Makefile
VENV_DIR := .venv
UV := uv
LINTER := ruff  # Replace this with the packages you need
LOGURU_LEVEL := INFO
export

all: lint test
.PHONY: all requirements-dev test lint build pypi run-crawl run-missing build-crawler build-arm-pi sync-data

.venv:
	@echo "Initializing virtual environment..."
	$(UV) venv

requirements-dev: .venv
	@echo "Generating & installing dev requirements..."
	$(UV) run pip compile --extra dev pyproject.toml > requirements-dev.txt
	$(UV) run pip install -r requirements-dev.txt
	$(UV) run pip install -e .

test:
	$(UV) run pytest src/vietlott/tests

lint: .venv
	@echo "Linting..."
	$(UV) run ruff check --select I --fix ./src
	$(UV) run ruff format ./src

build: lint test
	@echo "Building..."
	$(UV) run python -m build

build-crawler:
	cd crawler && go build -o ../bin/vietlott-crawler ./cmd/vietlott

build-arm-pi:
	cd crawler && GOOS=linux GOARCH=arm64 GOARM=7 go build -ldflags="-s -w" -o ../bin/vietlott-crawler-arm64 ./cmd/vietlott

pypi: build
	@echo "Publishing..."
	$(UV) run python -m twine upload --repository testpypi dist/*

run-crawl: .venv
	@echo "Running crawl scripts..."
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py keno
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py power_535
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py power_655

run-missing: .venv
	@echo "Running missing scripts..."
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py keno
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py power_535

# Scheduled data update using the Go crawler (mirrors bin/github_data.sh,
# which still drives the Python crawler via cron). MAX_DRAWS bounds each
# product's gap fill; 0 means no limit.
MAX_DRAWS ?= 0

sync-data: build-crawler
	@echo "Syncing lottery data with Go crawler..."
	./bin/vietlott-crawler sync --all --max-draws $(MAX_DRAWS) || true
	./bin/vietlott-crawler render-readme
	./bin/vietlott-crawler render-docs
	git add data readme.md docs/index.html
	git commit -m "update data @ `date +%Y-%m-%d\ %H:%M:%S`" || echo "nothing to commit"
	git push origin main
