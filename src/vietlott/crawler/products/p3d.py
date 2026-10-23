from typing import Dict, List

import pendulum
from bs4 import BeautifulSoup

from vietlott.crawler.collections_helper import chunks_iter
from vietlott.crawler.products.base import BaseProduct
from vietlott.crawler.schema.requests import RequestP3D


class P3D(BaseProduct):
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
            if not tds:
                continue

            divs = tr.find_all("div")
            if not divs:
                continue
            div_0_text = divs[0].get_text()

            if "Ngày: " not in div_0_text:
                continue
            date_str = div_0_text.split("Ngày: ")[1].strip()
            try:
                date_val = pendulum.from_format(date_str, "DD/MM/YYYY").to_date_string()
            except Exception:
                continue

            td_a = tds[0].find_all("a")
            if not td_a:
                continue

            div_result = tr.find("div", class_="tong_day_so_ket_qua")
            if not div_result:
                continue
            all_spans = div_result.find_all("span", class_="bong_tron")
            if len(all_spans) < 60:
                continue

            row = {
                "date": date_val,
                "id": td_a[0].text.strip(),
            }

            prizes = [
                {"name": "Giải Đặc biệt", "count": 6},
                {"name": "Giải Nhất", "count": 12},
                {"name": "Giải Nhì", "count": 18},
                {"name": "Giải ba", "count": 24},
            ]

            results = {}
            cur_idx = 0
            for prize in prizes:
                results[prize["name"]] = [
                    "".join(n)
                    for n in chunks_iter([all_spans[cur_idx + i].get_text() for i in range(prize["count"])], 3)
                ]
                cur_idx += prize["count"]
            row["result"] = results

            data.append(row)
        return data
