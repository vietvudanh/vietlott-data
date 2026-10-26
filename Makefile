# Makefile
VENV_DIR := .venv
UV := uv
LINTER := ruff  # Replace this with the packages you need
LOGURU_LEVEL := INFO
export

PI_HOST ?= pi
DEPLOY_FOLDER ?= /home/pi/projects/vietlott-data
BINARY_ARM := bin/vietlott-crawler-arm64

all: lint test
.PHONY: all requirements-dev test lint build pypi run-crawl run-missing build-crawler build-arm-pi deploy deploy-arm-pi sync-data

.venv:
	@echo "Initializing virtual environment..."
	$(UV) venv

requirements-dev: .venv
	@echo "Generating & installing dev requirements..."
	$(UV) run pip compile --extra dev pyproject.toml > requirements-dev.txt
	$(UV) run pip install -r requirements-dev.txt
	$(UV) run pip install -e .

test:
	$(UV) run pytest

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
	mkdir -p bin
	cd crawler && GOOS=linux GOARCH=arm64 GOARM=7 go build -ldflags="-s -w" -o ../$(BINARY_ARM) ./cmd/vietlott

deploy: build-arm-pi
	@ssh "$(PI_HOST)" "mkdir -p $(DEPLOY_FOLDER)/bin"
	@scp -C "$(BINARY_ARM)" "$(PI_HOST):$(DEPLOY_FOLDER)/bin/vietlott-crawler"

deploy-arm-pi: deploy

pypi: build
	@echo "Publishing..."
	$(UV) run python -m twine upload --repository testpypi dist/*

run-crawl: .venv
	@echo "Running crawl scripts..."
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py keno
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py power_655
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py power_645
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py power_535
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py 3d
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py 3d_pro
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/crawl.py bingo18

run-missing: .venv
	@echo "Running missing scripts..."
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py keno
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py power_655
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py power_645
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py power_535
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py 3d
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py 3d_pro
	LOGURU_LEVEL=$(LOGURU_LEVEL) PYTHONPATH=src $(UV) run python src/vietlott/cli/missing.py bingo18

# Scheduled data update using the Go crawler (mirrors bin/github_data.sh,
# which now drives the same Go crawler via cron). MAX_DRAWS bounds each
# product's gap fill; 0 means no limit.
MAX_DRAWS ?= 0

sync-data: build-crawler
	@echo "Syncing lottery data with Go crawler..."
	./bin/vietlott-crawler sync --all --max-draws $(MAX_DRAWS)
	./bin/vietlott-crawler render-readme
	./bin/vietlott-crawler render-docs
	git add data readme.md docs/index.html
	git commit -m "update data @ `date +%Y-%m-%d\ %H:%M:%S`" || echo "nothing to commit"
	git push origin main
