#!/usr/bin/env python3

import datetime
import json
import logging
import math
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor

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
    run_date = datetime.datetime.now(pytz.timezone(zone)) - datetime.timedelta(days=1)
logging.info(run_date)

run_date_str = run_date.strftime(date_fmt)

name = "Power655"
url = 'https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game655CompareWebPart,Vietlott.PlugIn.WebParts.ashx'
page_to_run = 1  # roll every 2 days
num_thread = 5
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "text/plain; charset=utf-8",
    "X-AjaxPro-Method": "ServerSideDrawResult"
}
params = {}
body = {
    "ORenderInfo": {
        "SiteId": "main.frontend.vi",
        "SiteAlias": "main.vi",
        "UserSessionId": "",
        "SiteLang": "en",
        "IsPageDesign": False,
        "ExtraParam1": "",
        "ExtraParam2": "",
        "ExtraParam3": "",
        "SiteURL": "",
        "WebPage": None,
        "SiteName": "Vietlott",
        "OrgPageAlias": None,
        "PageAlias": None,
        "FullPageAlias": None,
        "RefKey": None,
        "System": 1
    },
    "Key": "23bbd667",
    "GameDrawId": "",
    "ArrayNumbers": [
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    ],
    "CheckMulti": False,
    "PageIndex": 0
}


def process_result(params, body, res_json):
    """
    process 655 result
    :param params:
    :param body:
    :param res_json:
    :return:
    """
    soup = BeautifulSoup(res_json.get('value', {}).get('HtmlContent'), 'lxml')
    data = []
    for i, tr in enumerate(soup.select('table tr')):
        if i == 0:
            continue
        tds = tr.find_all('td')
        row = {}

        #
        row['date'] = tds[0].text
        row['id'] = tds[1].text

        # last number of special
        row['result'] = [int(span.text) for span in tds[2].find_all('span') if span.text.strip() != '|']
        row['page'] = body.get("PageIndex", -1)

        data.append(row)
    return data


def run(index_to):
    pool = ThreadPoolExecutor(num_thread)
    page_per_task = math.ceil(index_to / num_thread)
    tasks = utils.chunks_iter([
        ({}, {'PageIndex': i})
        for i in range(0, index_to)
    ], page_per_task)

    logging.info(f'there are {page_per_task} tasks')
    fetch = utils.fetch_wrapper(url, headers, params, body, process_result)

    results = pool.map(fetch, tasks)

    # flatten results, as it is 3 level deeps
    date_dict = defaultdict(list)
    for l1 in results:
        for l2 in l1:
            for row in l2:
                date_dict[row['date']].append(row)

    for date, date_items in date_dict.items():
        date_dt = datetime.datetime.strptime(date, '%d/%m/%Y')
        p = pathlib.Path('data') / '655' / f"{date_dt.strftime('%Y%m%d')}.jsonl"
        logging.info(f'writting to {p}')

        with open(str(p), 'w') as f:
            for r in date_items:
                f.write(json.dumps(r))
                f.write('\n')


def main():
    run(page_to_run)  # roll every 10 min from 6:00 to 21:55, each page 6  => 16 pages


def main1():
    res = requests.post(url, json=params, headers=headers)
    logging.info(res.json())


if __name__ == '__main__':
    main()
