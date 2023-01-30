import re
import sys

import requests

from cli.power655 import logger

from vietlott.crawler.requests_helper import fetch

url = 'https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game655CompareWebPart,Vietlott.PlugIn.WebParts.ashx'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
           'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.5', 'Content-Type': 'text/plain; charset=utf-8',
           'X-AjaxPro-Method': 'ServerSideDrawResult', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin'}
body = {'ORenderInfo': {'SiteId': 'main.frontend.vi', 'SiteAlias': 'main.vi', 'UserSessionId': '', 'SiteLang': 'en',
                        'IsPageDesign': False, 'ExtraParam1': '', 'ExtraParam2': '', 'ExtraParam3': '', 'SiteURL': '',
                        'WebPage': None, 'SiteName': 'Vietlott', 'OrgPageAlias': None, 'PageAlias': None,
                        'FullPageAlias': None, 'RefKey': None, 'System': 1}, 'Key': '23bbd667', 'GameDrawId': '',
        'ArrayNumbers': [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']], 'CheckMulti': False,
        'PageIndex': 0}
params = {}

fetch_fn = fetch.fetch_wrapper(url,
                               headers,
                               params,
                               body,
                               lambda x: x, )
# fetch_fn([
#     {
#         'task_id': 0,
#         'task_data': {
#             'params': {},
#             'body': {'PageIndex': 0}
#         }
#     }])

tasks = [
    {
        'task_id': 0,
        'task_data': {
            'params': {},
            'body': {'PageIndex': 0}
        }
    }]

process_result_fn = lambda v: v

with requests.session() as session:
    res = session.post(url, json=body, params={}, headers=headers, timeout=2)
    cookie = re.search(r'document.cookie="(.*?)"', res.text).group(1)
    cookies = {cookie.split('=')[0]: cookie.split('=')[1]}
    logger.info(cookies)
    res3 = requests.post(url, json=body, params={}, headers=headers, timeout=1)

    results = []
    for task in tasks:
        task_id, task_data = task['task_id'], task['task_data']
        params = params.copy()
        body = body.copy()

        params.update(task_data['params'])
        body.update(task_data['body'])

        res = session.post(url, json=body, params=params,
                           headers=headers, cookies=cookies, timeout=2)
        res2 = requests.post(url, json=body, params=params, headers=headers, cookies=cookies, timeout=1)
        logger.info(res2.status_code)
        logger.info(res2.text)

        if not res.ok:
            logger.error(
                f"req fail, args={task_data}, code={res.status_code}, text={res.text[:200]}, headers={headers}, body={body}, params={params}")
            continue
        try:
            result = process_result_fn(params, body, res.json())
            results.append(result)
            logger.info(f"task {task_id} done")
        except requests.exceptions.JSONDecodeError as e:
            logger.error(
                f'json decode error, args={task_data}, text={res.text[:200]}, headers={headers}, cookies={cookies}, body={body}, params={params}')

#
res3 = requests.post(url, json=body, params=params, headers=headers, timeout=1)
logger.info(res3.status_code)
logger.info(res3.text)

# cookie = re.search(r'document.cookie="(.*?)"', res3.text).group(1)
# cookies = {cookie.split("=")[0]: cookie.split("=")[1]}
# logger.info(cookies)
# res = requests.post(url, headers=headers, cookies=cookies, json=body, params=params, timeout=2)
# logger.info(res.text)
