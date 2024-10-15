from typing import List, Dict

import pendulum
from bs4 import BeautifulSoup

from vietlott.crawler.collections_helper import chunks_iter
from vietlott.crawler.products import BaseProduct
from vietlott.crawler.products.power655 import ProductPower655
from vietlott.crawler.schema.requests import RequestP3D


class P3D(ProductPower655):
    name = "3d"
    url = "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameMax3DCompareWebPart,Vietlott.PlugIn.WebParts.ashx"

    org_body = RequestP3D(
        CheckMulti=0,
        GameDrawId="",
        GameId="5",
        ORenderInfo=BaseProduct.orender_info_default,
        PageIndex=1,
        number01="123",
        number02="321",
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
            tds = tr.find_all("td")
            row = {}

            #
            divs = tr.find_all("div")
            div_0 = divs[0]
            div_0_text = div_0.get_text()

            # Extract the date after "Ngày:"
            date_str = div_0_text.split("Ngày: ")[1]
            row["date"] = pendulum.from_format(date_str, "DD/MM/YYYY").to_date_string()

            # if row["date"] != run_date_str:
            #     logger.error("wrong date instance %s != %s", row["date"], run_date_str)
            #     continue

            td_a = tds[0].find_all("a")
            row["id"] = td_a[0].text

            # Find all sections that contain the results
            results = {}

            prizes = [
                {"name": "Giải Đặc biệt", "count": 6},
                {"name": "Giải Nhất", "count": 12},
                {"name": "Giải Nhì", "count": 18},
                {"name": "Giải ba", "count": 24},
            ]

            results = {}

            div_result = tr.find("div", class_="tong_day_so_ket_qua")
            all_spans = div_result.find_all("span", class_="bong_tron")

            # Loop through each prize and extract corresponding numbers
            cur_idx = 0
            for prize in prizes:
                results[prize["name"]] = [
                    "".join(n)
                    for n in chunks_iter([all_spans[cur_idx + i].get_text() for i in range(prize["count"])], 3)
                ]
                cur_idx += prize["count"]
            row["result"] = results

            #
            row["page"] = body.get("PageIndex", -1)

            data.append(row)
        return data
