from vietlott.crawler.products.base import BaseProduct
from vietlott.crawler.schema.requests import RequestPower535


class ProductPower535(BaseProduct):
    name = "power_535"
    url = "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.Game535CompareWebPart,Vietlott.PlugIn.WebParts.ashx"

    stored_data_dtype = {
        "date": str,
        "id": str,
        "result": "list",
        "page": int,
        "process_time": str,
    }

    # Use RequestPower535 schema similar to 645/655 but adjusted for 5/35
    org_body = RequestPower535(
        ORenderInfo=BaseProduct.orender_info_default,
        Key="d0ea794f",  # Will need to be updated with actual key if found
        GameDrawId="",
        ArrayNumbers=[
            ["" for _ in range(35)] for _ in range(5)
        ],  # 5 numbers from 1-35, so 15 slots per row should be sufficient
        CheckMulti=False,
        PageIndex=0,
    )
