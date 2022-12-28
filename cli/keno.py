#!/usr/bin/env python3

import datetime
import json
import logging
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor

import pytz
import requests
from bs4 import BeautifulSoup

import crawler.requests_helper.fetch
from crawler import collections_helper

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s::%(lineno)s %(message)s')

date_fmt = '%d/%m/%Y'
zone = 'Asia/Bangkok'  # +0700
if len(sys.argv) > 1:
    run_date = datetime.datetime.strptime(sys.argv[1], '%Y%m%d')
else:
    run_date = datetime.datetime.now(pytz.timezone(zone)) - datetime.timedelta(days=1)
logging.info(run_date)

run_date_str = run_date.strftime(date_fmt)

name = "Keno"
url = 'https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameKenoCompareWebPart,Vietlott.PlugIn.WebParts.ashx'
page_to_run = 34
num_thread = 5

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "text/plain; charset=utf-8",
    "X-AjaxPro-Method": "ServerSideDrawResult",
    "Content-Length": "437",
    "Origin": "https//vietlott.vn",
    "Connection": "keep-alive",
    "Referer": "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno",
    "Cookie": "D1N=52a5f96f7aa3046bdd6976a73f9d7b2e",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}
params = {}
body = {
    "DrawDate": "",
    "GameDrawNo": "",
    "GameId": "6",
    "ORenderInfo":
        {
            "ExtraParam1": "",
            "ExtraParam2": "",
            "ExtraParam3": "",
            "FullPageAlias": None,
            "IsPageDesign": False,
            "OrgPageAlias": None,
            "PageAlias": None,
            "RefKey": None,
            "SiteAlias": "main.vi",
            "SiteId": "main.frontend.vi",
            "SiteLang": "vi",
            "SiteName": "Vietlott",
            "SiteURL": "",
            "System": 1,
            "UserSessionId": "",
            "WebPage": None
        },
    "OddEven": 2,
    "PageIndex": 1,
    "ProcessType": 0,
    "TotalRow": 112453,
    "UpperLower": 2,
    "number": ""
}


def process_result(params, body, res_json):
    """
    process keno result
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
        td_a = tds[0].find_all('a')
        row['date'] = td_a[0].text
        if row['date'] != run_date_str:
            logging.info('wrong date instance %s != %s', row['date'], run_date_str)
            continue

        row['id'] = td_a[1].text

        #
        row['result'] = [int(span.text) for span in tds[1].find_all('span')]

        #
        row['big_small'] = tds[2].text
        row['odd_even'] = tds[3].text
        row['page'] = body.get("PageIndex", -1)

        data.append(row)
    return data


def run(index_to):
    pool = ThreadPoolExecutor(num_thread)
    page_per_task = int(index_to / num_thread)
    tasks = collections_helper.chunks_iter([
        {
            'task_id': i,
            'task_data': {
                'params': {},
                'body': {'PageIndex': i}
            }
        }
        for i in range(0, index_to)
    ], page_per_task)

    logging.info(f'there are {page_per_task} tasks')
    fetch = crawler.requests_helper.fetch.fetch_wrapper(url, headers, params, body, process_result)

    results = pool.map(fetch, tasks)

    # flatten results, as it is 3 level deeps
    results = [
        l3
        for l1 in results
        for l2 in l1
        for l3 in l2
    ]

    p = pathlib.Path('../data') / 'keno' / f"{run_date.strftime('%Y%m%d')}.jsonl"
    logging.info(f'writting to {p}')
    with open(str(p), 'w') as f:
        for r in results:
            f.write(json.dumps(r))
            f.write('\n')


def main():
    run(page_to_run)


def main1():
    res = requests.post(url, json=body, headers=headers)
    logging.info(res.text)


if __name__ == '__main__':
    main()
