#!/usr/bin/env python3

import datetime
import logging
import sys

import pytz

import vietlott.crawler.logger
from vietlott.crawler.products.power655 import ProductPower655
from vietlott.crawler.products.power645 import ProductPower645

logger = logging.getLogger(__name__)

date_fmt = '%d/%m/%Y'
zone = 'Asia/Bangkok'  # +0700
if len(sys.argv) > 1:
    run_date = datetime.datetime.strptime(sys.argv[1], '%Y%m%d')
else:
    logger.info('no date arg, using today')
    run_date = datetime.datetime.now(pytz.timezone(zone)) - datetime.timedelta(days=1)
logger.info(run_date)

run_date_str = run_date.strftime(date_fmt)


def main():
    ProductPower655().crawl(run_date_str, 1)  # roll every 10 min from 6:00 to 21:55, each page 6  => 16 pages
    ProductPower645().crawl(run_date_str, 1)  # roll every 10 min from 6:00 to 21:55, each page 6  => 16 pages


if __name__ == '__main__':
    main()
