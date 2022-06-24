#!/usr/bin/env python3

import datetime
import json
import logging
import math
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict

from collections import defaultdict
import pytz
import requests
from bs4 import BeautifulSoup

import utils

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s::%(lineno)s %(message)s')

date_fmt = '%d/%m/%Y'
zone = 'Asia/Bangkok'  # +0700
if len(sys.argv) > 1:
    run_date = datetime.datetime.strptime(sys.argv[1], '%Y%m%d')
else:
    logging.info('no date arg, using today')
    run_date = datetime.datetime.now(pytz.timezone(zone)) - datetime.timedelta(days=1)
logging.info(run_date)

run_date_str = run_date.strftime(date_fmt)










def main():
    run(1)  # roll every 10 min from 6:00 to 21:55, each page 6  => 16 pages


def main1():
    res = requests.post(url, json=params, headers=headers)
    logging.info(res.json())


if __name__ == '__main__':
    main()
