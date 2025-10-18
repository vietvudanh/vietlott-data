from datetime import datetime
from typing import Dict, List

from bs4 import BeautifulSoup

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

    def process_result(self, params, body, res_json, task_data) -> List[Dict]:
        """
        process 5/35 (power_535) result
        return list of dicts with keys: date, id, result, page, process_time
        """
        soup = BeautifulSoup(res_json.get("value", {}).get("HtmlContent"), "lxml")
        data = []
        for i, tr in enumerate(soup.select("table tr")):
            if i == 0:
                continue
            tds = tr.find_all("td")
            if not tds:
                continue

            row = {}
            # date in first column, id in second like other products
            try:
                row["date"] = datetime.strptime(tds[0].text.strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
            except Exception:
                # skip rows with unexpected format
                continue
            row["id"] = tds[1].text.strip()
            # numbers are in the following td, collect span texts
            row["result"] = [int(span.text) for span in tds[2].find_all("span") if span.text.strip() != "|"]
            row["page"] = body.get("PageIndex", -1)
            row["process_time"] = datetime.now().isoformat()

            data.append(row)
        return data
