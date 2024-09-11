from typing import List, Dict

import pendulum
from bs4 import BeautifulSoup

from vietlott.crawler.products.power655 import ProductPower655
from vietlott.crawler.schema.requests import P3D


class P3D(ProductPower655):
    name = "3d"
    url = "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameMax3DCompareWebPart,Vietlott.PlugIn.WebParts.ashx"

    org_body = P3D(
        CheckMulti=0,
        GameDrawId="",
        GameId="5",
        ORenderInfo=ProductPower655.orender_info_default,
        PageIndex=1,
        number01="123",
        number02="321"
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
            divs = tr.find_all("div")
            div_0 = divs[0]
            div_0_text = div_0.get_text()

            # Extract the date after "Ngày:"
            date_str = div_0_text.split('Ngày: ')[1]
            row["date"] = pendulum.from_format(date_str, "DD/MM/YYYY").to_date_string()

            # if row["date"] != run_date_str:
            #     logger.error("wrong date instance %s != %s", row["date"], run_date_str)
            #     continue

            td_a = tds[0].find_all("a")
            row["id"] = td_a[0].text

            #
            # Find all sections that contain the results
            results = {}

            #
            # div_result = tr.find('div', class_='tong_day_so_ket_qua text-center')
            # # Extract special prize (Giải Đặc biệt)
            # special_prize_spans = div_result.find_all('h5', string='Giải Đặc biệt')[0].find_next('div').find_all('span')
            # special_prize_numbers = ''.join([span.get_text() for span in special_prize_spans])
            # results['Giải Đặc biệt'] = [special_prize_numbers[:3], special_prize_numbers[3:]]
            #
            # # Extract first prize (Giải Nhất)
            # first_prize_spans = div_result.find_all('h5', string='Giải Nhất')[0].find_next('div').find_all('span')
            # first_prize_numbers = [span.get_text() for span in first_prize_spans]
            # results['Giải Nhất'] = [first_prize_numbers[i:i + 3] for i in range(0, len(first_prize_numbers), 3)]
            #
            # # Extract second prize (Giải Nhì)
            # second_prize_spans = div_result.find_all('h5', string='Giải Nhì')[0].find_next('div').find_all('span')
            # second_prize_numbers = [span.get_text() for span in second_prize_spans]
            # results['Giải Nhì'] = [second_prize_numbers[i:i + 3] for i in range(0, len(second_prize_numbers), 3)]
            #
            # # Extract third prize (Giải Ba)
            # third_prize_spans = div_result.find_all('h5', string='Giải ba')[0].find_next('div').find_all('span')
            # third_prize_numbers = [span.get_text() for span in third_prize_spans]
            # results['Giải ba'] = [third_prize_numbers[i:i + 3] for i in range(0, len(third_prize_numbers), 3)]

            prizes = {
                "Giải Đặc biệt": 6,  # 2 sets of 3 numbers, so total 6 spans
                "Giải Nhất": 12,  # 4 sets of 3 numbers, total 12 spans
                "Giải Nhì": 18,  # 6 sets of 3 numbers, total 18 spans
                "Giải ba": 24  # 8 sets of 3 numbers, total 24 spans
            }

            results = {}

            div_result = tr.find('div', class_='tong_day_so_ket_qua text-center')
            # Loop through each prize and extract corresponding numbers
            for prize, span_count in prizes.items():
                prize_header = div_result.find('h5', text=prize)
                # print(prize_header.find_next('div', class_='row'))

                if prize_header:
                    spans = prize_header.find_all('span', class_='bong_tron tiny',
                                                                                 limit=span_count)
                    numbers = [span.text for span in spans]
                    results[prize] = numbers
            row["result"] = results

            #
            row["page"] = body.get("PageIndex", -1)

            data.append(row)
        return data
