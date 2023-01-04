import re

import requests

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

res = requests.post(url, json=body, params=params, headers=headers, timeout=1)
print(res.status_code)
print(res.text)

cookie = re.search(r'document.cookie="(.*?)"', res.text).group(1)
cookies = {cookie.split("=")[0]: cookie.split("=")[1]}

res = requests.post(url, headers=headers, cookies=cookies, json=body, params=params, timeout=2)
print(res.text)

"""conclusion:
not using session is ok too, wtf, but must use cookies
"""
