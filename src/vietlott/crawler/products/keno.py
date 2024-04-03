from typing import List, Dict

import pendulum
from bs4 import BeautifulSoup

from vietlott.crawler.products.power655 import ProductPower655
from vietlott.crawler.schema.requests import Keno


class ProductKeno(ProductPower655):
    name = "keno"
    url = "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameKenoCompareWebPart,Vietlott.PlugIn.WebParts.ashx"

    org_body = Keno(
        DrawDate="",
        GameDrawNo="",
        GameId="6",
        ORenderInfo=ProductPower655.orender_info_default,
        OddEven=2,
        PageIndex=1,
        ProcessType=0,
        TotalRow=112453,
        UpperLower=2,
        number="",
    )

    def process_result(self, params, body: dict, res_json: dict, task_data: dict) -> List[Dict]:
        """process result for keno

        Args:
            params (dict): _description_
            body (dict): _description_
            res_json (dict): _description_
            task_data (dict): contains keys
                run_date_str:
                    date to run (only get this date)


        Returns:
            List[Dict]: _description_
        """
        soup = BeautifulSoup(res_json.get("value", {}).get("HtmlContent"), "lxml")
        # run_date_str = task_data["run_date_str"]
        data = []
        for i, tr in enumerate(soup.select("table tr")):
            if i == 0:
                continue
            tds = tr.find_all("td")
            row = {}

            #
            td_a = tds[0].find_all("a")
            row["date"] = pendulum.from_format(td_a[0].text, "DD/MM/YYYY").to_date_string()

            # if row["date"] != run_date_str:
            #     logger.error("wrong date instance %s != %s", row["date"], run_date_str)
            #     continue

            row["id"] = td_a[1].text

            #
            row["result"] = [int(span.text) for span in tds[1].find_all("span")]

            #
            row["big_small"] = tds[2].text
            row["odd_even"] = tds[3].text
            row["page"] = body.get("PageIndex", -1)

            data.append(row)
        return data
