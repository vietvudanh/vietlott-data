from typing import Dict, List

import pendulum
from bs4 import BeautifulSoup
from loguru import logger

from vietlott.crawler.products import BaseProduct
from vietlott.crawler.products.power655 import ProductPower655
from vietlott.crawler.schema.requests import RequestBingo18


class ProductBingo18(ProductPower655):
    name = "bingo18"
    url = "https://vietlott.vn/ajaxpro/Vietlott.PlugIn.WebParts.GameBingoCompareWebPart,Vietlott.PlugIn.WebParts.ashx"

    stored_data_dtype = {
        "date": str,
        "id": str,
        "result": List[int],
        "total": int,
        "large_small": str,
        "page": int,
        "process_time": str,
    }

    org_body = RequestBingo18(
        ORenderInfo=BaseProduct.orender_info_default,
        GameId="8",
        GameDrawNo="",
        number="",
        DrawDate="",
        PageIndex=1,
        TotalRow=43569,
    )

    def process_result(self, params: dict, body: dict, res_json: dict, task_data: dict) -> List[Dict]:
        """Process result for Bingo18

        Args:
            params (dict): Request parameters
            body (dict): Request body
            res_json (dict): Response JSON
            task_data (dict): Contains keys
                run_date_str: date to run (only get this date)

        Returns:
            List[Dict]: List of processed data records
        """
        # Debug: Print the response to understand the structure
        logger.debug(f"Response JSON keys: {res_json.keys() if res_json else 'None'}")
        logger.debug(f"Response JSON: {res_json}")

        # Check if response has the expected structure
        html_content = None
        if res_json and "value" in res_json:
            if isinstance(res_json["value"], dict) and "HtmlContent" in res_json["value"]:
                html_content = res_json["value"]["HtmlContent"]
            elif isinstance(res_json["value"], str):
                html_content = res_json["value"]

        if not html_content:
            logger.warning(f"No HTML content found in response. Response structure: {res_json}")
            return []

        soup = BeautifulSoup(html_content, "lxml")
        data = []

        for i, tr in enumerate(soup.select("table tr")):
            if i == 0:  # Skip header row
                continue

            tds = tr.find_all("td")
            if len(tds) < 4:  # Ensure we have enough columns
                continue

            row = {}

            # Extract date and ID from first column
            date_id_links = tds[0].find_all("a")
            if len(date_id_links) >= 2:
                # Parse date
                date_text = date_id_links[0].text.strip()
                try:
                    row["date"] = pendulum.from_format(date_text, "DD/MM/YYYY").to_date_string()
                except Exception as e:
                    logger.warning(f"Failed to parse date '{date_text}': {e}")
                    continue

                # Extract ID
                row["id"] = date_id_links[1].text.strip().replace("#", "")

            # Extract result numbers (3 numbers from 0-9)
            result_spans = tds[1].find_all("span")
            if result_spans:
                try:
                    row["result"] = [int(span.text.strip()) for span in result_spans if span.text.strip().isdigit()]
                except ValueError as e:
                    logger.warning(f"Failed to parse result numbers: {e}")
                    continue
            else:
                # Fallback: try to extract numbers from text
                result_text = tds[1].get_text().strip()
                try:
                    # Split by spaces and filter digits
                    numbers = [int(x) for x in result_text.split() if x.isdigit()]
                    row["result"] = numbers[:3]  # Take first 3 numbers
                except ValueError as e:
                    logger.warning(f"Failed to parse result from text '{result_text}': {e}")
                    continue

            # Validate result - should be exactly 3 numbers
            if len(row["result"]) != 3:
                logger.warning(f"Invalid result length: {row['result']}")
                continue

            # Extract total from third column
            if len(tds) > 2:
                try:
                    row["total"] = int(tds[2].get_text().strip())
                except ValueError:
                    row["total"] = sum(row["result"])  # Calculate if not available

            # Extract large/small classification from fourth column
            if len(tds) > 3:
                row["large_small"] = tds[3].get_text().strip()

            # Add metadata
            row["page"] = body.get("PageIndex", -1)
            row["process_time"] = process_time  # Use precomputed timestamp

            data.append(row)

        logger.info(f"Processed {len(data)} Bingo18 records")
        return data
