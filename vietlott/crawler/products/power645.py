from vietlott.crawler.products.power655 import ProductPower655
from vietlott.crawler.schema.requests import RequestPower655


class ProductPower645(ProductPower655):
    name = "power_645"
    url = "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game645CompareWebPart,Vietlott.PlugIn.WebParts.ashx"

    # don't know why ArrayNumbers in 645 needs to be len 6 instead of 5 like in 655
    org_body = RequestPower655(
        ORenderInfo=ProductPower655.orender_info_default,
        Key="7d861b77",  # DIFF
        GameDrawId="",
        ArrayNumbers=[["" for _ in range(18)] for _ in range(6)],  # DIFF
        CheckMulti=False,
        PageIndex=0,
    )
