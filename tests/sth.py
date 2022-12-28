import re
import requests

url = 'https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game655CompareWebPart,Vietlott.PlugIn.WebParts.ashx'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "text/plain; charset=utf-8",
    "X-AjaxPro-Method": "ServerSideDrawResult",
    # "Cookie": "D1N=7902e190b064b1fdb395e85f70c3a2ae"
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

#
with requests.Session() as session:
    res = session.post(url, json=body, params=params, headers=headers)
    print(res.text)

    # TODO: add cookie check to task
    if headers.get("Cookie") is None:
        cookie = re.search(r'document.cookie="(.*?)"', res.text).group(1)
        print(cookie)
        headers["Cookie"] = cookie

    res = session.post(url, json=body, params=params, headers=headers)
    print(res.text)

# res = requests.post(url, json=body, params=params, headers=headers, timeout=1)
# print(res.text)