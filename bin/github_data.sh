# commit to csv_data
#!/usr/bin/env bash

URL=https://github.com/vietvudanh/vietlott-data.git
FOLDER=vietlott-data
DATA_FOLDER=data
USER="Viet VU"
EMAIl="vietvudanh@gmail.com"

# generate data file
python keno.py $1

if [[ ! -d "$FOLDER" ]] ; then
  git clone $URL $FOLDER
fi

cp -r $DATA_FOLDER $FOLDER/

cd $FOLDER
git pull

# commit and push
git config user.name "\'$USER\'"
git config user.email "\'$EMAIl\'"
git add $DATA_FOLDER
git commit -m "update data @ `date +%Y-%m-%d\ %H:%M:%S`"
git push --force "https://${GH_TOKEN}@github.com/vietvudanh/vietlott-data.git" HEAD:master
