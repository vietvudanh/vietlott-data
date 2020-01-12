#!/usr/bin/env python3

import logging
import datetime
import pytz
import itertools
import json
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s::%(lineno)s %(message)s')

date_fmt = '%d/%m/%Y'
zone = 'Asia/Bangkok'  # +0700
if len(sys.argv) > 1:
    run_date = datetime.datetime.strptime(sys.argv[1], '%Y%m%d')
else:
    run_date = datetime.datetime.now(pytz.timezone(zone))
logging.info(run_date)

current_date = run_date.strftime(date_fmt)

name = "Keno"
url = 'https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameKenoCompareWebPart,Vietlott.PlugIn.WebParts.ashx'
page_to_run = 34
num_thread = 5
headers = {
    "Host": "vietlott.vn",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "text/plain; charset=utf-8",
    "X-AjaxPro-Method": "ServerSideDrawResult",
    "Content-Length": "706",
    "Origin": "https://vietlott.vn",
    "Connection": "keep-alive",
    "Referer": "https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno"
}
params = {
    "DrawDate": "",
    "DrawId": "",
    "GameDrawId": "",
    "GameId": "6",
    "ORenderInfo": {
        "ExtraParam1": "",
        "ExtraParam2": "",
        "ExtraParam3": "",
        "FullPageAlias": None,
        "HttpMediaPathRoot": "https://media.vietlott.vn",
        "HttpRoot": "http://10.98.20.20",
        "HttpTempPathRoot": "",
        "IsPageDesign": False,
        "MediaPathRoot": "D:\\Portal\\Vietlott\\Media",
        "OrgPageAlias": None,
        "PageAlias": None,
        "PathRoot": "D:\\Portal\\Vietlott\\Frontend\\Web",
        "RefKey": None,
        "SiteAlias": "main.vi",
        "SiteId": "main.frontend.vi",
        "SiteLang": "vi",
        "SiteName": "Vietlott",
        "SiteURL": "",
        "System": 0,
        "TempPathRoot": "",
        "UserSessionId": "",
        "WebHttpRoot": "http://10.98.20.20",
        "WebPage": None,
        "WebPathRoot": "D:\\Portal\\Vietlott\\Frontend\\Web"
    },
    "PageIndex": 1,
    "ProcessType": 0,
    "number": ""
}


def fetch(indexes):
    with requests.session() as session:
        results = []
        for i in indexes:
            p = params.copy()
            p['PageIndex'] = i
            res = session.post(url, json=p, headers=headers)

            if not res.ok:
                logging.info(p)
                continue

            result = process_result(res.json(), i)
            results.append(result)
        logging.info(f'task {len(indexes)} done')
        return results


def process_result(res_json, page):
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
        if row['date'] != current_date:
            logging.info('wrong date instance %s', row['date'])
            continue

        row['id'] = td_a[1].text

        #
        row['result'] = [int(span.text) for span in tds[1].find_all('span')]

        #
        row['big_small'] = tds[2].text
        row['odd_even'] = tds[3].text
        row['page'] = page

        data.append(row)
    return data


def chunks_iter(data, n):
    it = iter(data)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def run(index_to):
    pool = ThreadPoolExecutor(num_thread)
    page_per_task = int(index_to / num_thread)
    tasks = chunks_iter(range(1, index_to), page_per_task)

    logging.info(f'there are {page_per_task} tasks')

    results = pool.map(fetch, tasks)

    results = [
        l3
        for l1 in results
        for l2 in l1
        for l3 in l2
    ]

    p = pathlib.Path('data') / 'keno' / f"{run_date.strftime('%Y%m%d')}.jsonl"
    logging.info(f'writting to {p}')
    with open(str(p), 'w') as f:
        for r in results:
            f.write(json.dumps(r))
            f.write('\n')


def main():
    run(page_to_run)  # roll every 10 min from 6:00 to 21:55 => 16 pages


def main1():
    res = requests.post(url, json=params, headers=headers)
    logging.info(res.json())


if __name__ == '__main__':
    main()
