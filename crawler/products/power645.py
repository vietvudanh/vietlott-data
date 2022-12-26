from crawler.products.power655 import ProductPower655


class ProductPower645(ProductPower655):
    name = "power_645"
    url = 'https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game645CompareWebPart,Vietlott.PlugIn.WebParts.ashx'

    # don't know why ArrayNumbers in 645 needs to be len 6
    org_body = {
        "ORenderInfo": {
            "SiteId": "main.frontend.vi",
            "SiteAlias": "main.vi",
            "UserSessionId": "",
            "SiteLang": "vi",
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
        "Key": "7d861b77",
        "GameDrawId": "",
        "ArrayNumbers": [
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        ],
        "CheckMulti": False,
        "PageIndex": 0
    }
