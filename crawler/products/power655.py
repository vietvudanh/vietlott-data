import logging
import math
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import List, Dict

logger = logging.getLogger(__name__)

import pandas as pd
from bs4 import BeautifulSoup

from crawler import collections as collections_utils, config
from crawler import fetch

name = "Power655"
url = 'https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game655CompareWebPart,Vietlott.PlugIn.WebParts.ashx'
page_to_run = 1  # roll every 2 days
num_thread = 20

stored_data_dtype = {
    'date': str,
    'id': str,
    'result': 'list',
    'page': int,
    'process_time': str
}

org_body = {
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
params = {}


def process_result(params, body, res_json) -> List[Dict]:
    """
    process 655 result
    :param params:
    :param body:
    :param res_json:
    :return: list of dict data
    """
    soup = BeautifulSoup(res_json.get('value', {}).get('HtmlContent'), 'lxml')
    data = []
    for i, tr in enumerate(soup.select('table tr')):
        if i == 0:
            continue
        tds = tr.find_all('td')
        row = {}

        #
        row['date'] = datetime.strptime(tds[0].text, '%d/%m/%Y').strftime('%Y-%m-%d')
        row['id'] = tds[1].text

        # last number of special
        row['result'] = [int(span.text) for span in tds[2].find_all('span') if span.text.strip() != '|']
        row['page'] = body.get("PageIndex", -1)
        row['process_time'] = datetime.now().isoformat()

        data.append(row)
    return data


def crawl(index_to: int = 1):
    """
    spawn multiple worker to get data from vietlott
    each worker craw a list of dates
    :param index_to: earliest page we want to crawl, default = 1 (1 page)
    """
    pool = ThreadPoolExecutor(num_thread)
    page_per_task = math.ceil(index_to / num_thread)
    tasks = collections_utils.chunks_iter([
        {
            'task_id': i,
            'task_data': {
                'params': {},
                'body': {'PageIndex': i}
            }
        }
        for i in range(0, index_to)
    ], page_per_task)

    logger.info(f'there are {page_per_task} tasks')
    fetch_fn = fetch.fetch_wrapper(url, config.headers, params, org_body, process_result)

    results = pool.map(fetch_fn, tasks)

    # flatten results, as it is 3 level deeps
    date_dict = defaultdict(list)
    for l1 in results:
        for l2 in l1:
            for row in l2:
                date_dict[row['date']].append(row)

    list_data = []
    for date, date_items in date_dict.items():
        list_data += date_items
    df = pd.DataFrame(list_data)
    logger.info(f'crawled data min_date={df["date"].min()}, max_date={df["date"].max()}' +
                f', records={len(df)}')

    # store data
    if config.power655_file.exists():
        current_data = pd.read_json(config.power655_file, lines=True, dtype=stored_data_dtype)
        logger.info(f'current data min_date={current_data["date"].min()}, max_date={current_data["date"].max()}' +
                    f', records={len(current_data)}')
        df_take = df[~df['id'].isin(current_data['id'])]
        df_final = pd.concat([
            current_data,
            df_take
        ], axis='rows')
    else:
        df_final = df

    logger.info(f'final data min_date={df_final["date"].min()}, max_date={df_final["date"].max()}' +
                f', records={len(df_final)}')
    df_final.to_json(config.power655_file.absolute(), orient='records', lines=True)
    logger.info(f"wrote to file {config.power655_file.absolute()}")
