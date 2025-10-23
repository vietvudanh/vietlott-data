from vietlott.crawler.products.base import BaseProduct
from vietlott.crawler.products.power655 import ProductPower655
from vietlott.crawler.schema.requests import RequestPower655


class ProductPower645(ProductPower655):
    """Power 6/45 product. Subclass ProductPower655 to reuse HTML parsing logic
    since the response HTML structure is the same for 6/55 and 6/45.
    """

    name = "power_645"
    url = "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game645CompareWebPart,Vietlott.PlugIn.WebParts.ashx"

    # 645 expects ArrayNumbers length 6 (rows) x 18 (cols) instead of 5 rows for 655
    org_body = RequestPower655(
        ORenderInfo=BaseProduct.orender_info_default,
        Key="8290fce2",
        GameDrawId="",
        ArrayNumbers=[["" for _ in range(18)] for _ in range(6)],
        CheckMulti=False,
        PageIndex=0,
    )
