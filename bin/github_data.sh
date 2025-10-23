#!/usr/bin/env bash
# commit to csv_data

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

# generate data file
echo "pwd $(pwd)"

export PYTHONPATH="src"
export LOGURU_LEVEL="INFO"

python src/vietlott/cli/crawl.py keno
python src/vietlott/cli/missing.py keno
python src/vietlott/cli/crawl.py power_655
python src/vietlott/cli/missing.py power_655
python src/vietlott/cli/crawl.py power_645
python src/vietlott/cli/missing.py power_645
python src/vietlott/cli/crawl.py power_535
python src/vietlott/cli/missing.py power_535
python src/vietlott/cli/crawl.py 3d
python src/vietlott/cli/missing.py 3d
python src/vietlott/cli/crawl.py 3d_pro
python src/vietlott/cli/missing.py 3d_pro
python src/vietlott/cli/crawl.py bingo18
python src/vietlott/cli/missing.py bingo18

python src/render_readme.py

#if [[ ! -d "$FOLDER" ]] ; then
#  git clone $URL $FOLDER
#fi

#cp -r $DATA_FOLDER $FOLDER/

#cd $FOLDER
#git pull

# commit and push
git remote add github git@github.com:vietvudanh/vietlott-data.git
git config user.name "\'$USER\'"
git config user.email "\'$EMAIl\'"
git status
git add $DATA_FOLDER
git add readme.md
git commit -m "update data @ `date +%Y-%m-%d\ %H:%M:%S`"
git push github master
