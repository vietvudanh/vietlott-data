#!/usr/bin/env bash
# crawl with the Go crawler, render readme/docs and commit to github

set -euo pipefail

DATA_FOLDER=data
USER="Viet VU"
EMAIl="vietvudanh@gmail.com"
MAX_DRAWS="${MAX_DRAWS:-0}"

cd "$(dirname "$0")/.."

git pull --rebase --autostash origin main

echo "pwd $(pwd)"

(cd crawler && go build -o ../bin/vietlott-crawler ./cmd/vietlott)

# sync fetches the latest draws and backfills missing ones for every product;
# a failing product must not block rendering and committing the others
./bin/vietlott-crawler sync --all --max-draws "$MAX_DRAWS" || echo "sync reported failures"

./bin/vietlott-crawler render-readme
./bin/vietlott-crawler render-docs

# commit and push
git config user.name "$USER"
git config user.email "$EMAIl"
git status
git add $DATA_FOLDER
git add readme.md
git add docs/index.html
git commit -m "update data @ `date +%Y-%m-%d\ %H:%M:%S`" || { echo "nothing to commit"; exit 0; }
git push origin main
