#!/usr/bin/env python3

import datetime
import logging
import sys

import pytz

from crawler.products.power655 import ProductPower655
from crawler.products.power645 import ProductPower645

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
    ProductPower655.crawl(1)  # roll every 10 min from 6:00 to 21:55, each page 6  => 16 pages
    # ProductPower645.crawl(1)  # roll every 10 min from 6:00 to 21:55, each page 6  => 16 pages


if __name__ == '__main__':
    main()
