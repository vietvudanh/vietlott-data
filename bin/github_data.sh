#!/usr/bin/env bash
# commit to csv_data

set -euo pipefail

URL=https://github.com/vietvudanh/vietlott-data.git
FOLDER=vietlott-data
DATA_FOLDER=data
USER="Viet VU"
EMAIl="vietvudanh@gmail.com"
VENV=".venv"

# Activate virtual environment if it exists
if [ -n "$VENV" ]; then
  source "$VENV/bin/activate"
fi

git pull --rebase --autostash origin main

# generate data file
echo "pwd $(pwd)"

export PYTHONPATH="src"
export LOGURU_LEVEL="INFO"

for product in keno power_655 power_645 power_535 3d 3d_pro bingo18; do
  python src/vietlott/cli/crawl.py "$product"
  python src/vietlott/cli/missing.py "$product"
done

python src/render_readme.py
python src/render_docs.py

#if [[ ! -d "$FOLDER" ]] ; then
#  git clone $URL $FOLDER
#fi

#cp -r $DATA_FOLDER $FOLDER/

#cd $FOLDER
#git pull

# commit and push
git config user.name "\'$USER\'"
git config user.email "\'$EMAIl\'"
git status
git add $DATA_FOLDER
git add readme.md
git add docs/index.html
git commit -m "update data @ `date +%Y-%m-%d\ %H:%M:%S`"
git push origin main
