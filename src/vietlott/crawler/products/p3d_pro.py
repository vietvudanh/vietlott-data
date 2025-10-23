from vietlott.crawler.products import BaseProduct
from vietlott.crawler.products.p3d import P3D
from vietlott.crawler.schema.requests import RequestP3DPro


class P3DPro(P3D):
    name = "3d_pro"
    url = (
        "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameMax3DProCompareWebPart,Vietlott.PlugIn.WebParts.ashx"
    )

    org_body = RequestP3DPro(
        CheckMulti=0,
        GameDrawId="",
        GameId="7",
        ORenderInfo=BaseProduct.orender_info_default,
        PageIndex=1,
        number01="123",
        number02="321",
    )
