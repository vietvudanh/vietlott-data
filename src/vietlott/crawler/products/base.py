import math
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import cattrs
import polars as pl
from loguru import logger

from vietlott.config.products import get_config
from vietlott.crawler import collections_helper
from vietlott.crawler.requests_helper import config as requests_config
from vietlott.crawler.requests_helper import fetch
from vietlott.crawler.requests_helper.fetch import get_vietlott_cookie
from vietlott.crawler.schema.requests import ORenderInfoCls


class BaseProduct:
    name = ""
    url = ""
    page_to_run: int = 1
    stored_data_dtype = {}

    org_body = None
    org_params = None

    product_config = None

    orender_info_default = ORenderInfoCls(
        SiteId="main.frontend.vi",
        SiteAlias="main.vi",
        UserSessionId="",
        SiteLang="vi",
        IsPageDesign=False,
        ExtraParam1="",
        ExtraParam2="",
        ExtraParam3="",
        SiteURL="",
        WebPage=None,
        SiteName="Vietlott",
        OrgPageAlias=None,
        PageAlias=None,
        RefKey=None,
        FullPageAlias=None,
    )

    def __init__(self):
        self.product_config = get_config(self.name)
        self.headers = requests_config.headers

        if self.product_config.use_cookies:
            self.vietlott_cookie, self.cookies = get_vietlott_cookie()
            self.headers.update({"Cookie": self.vietlott_cookie})
        else:
            self.vietlott_cookie, self.cookies = None, None

    def process_result(self, params, body, res_json, task_data):
        pass

    def crawl(self, run_date_str: str, index_from: int = 0, index_to: int = 1):
        """
        spawn multiple worker to get data from vietlott
        each worker craw a list of dates

        crawl from [index_from, index_to)
        :param product_config:
        :param index_from: latest page we want to crawl, default = 0 (1 page)
        :param index_to: the earliest page we want to crawl, default = 1 (1 page)
            if null then using default index_to in product's config
        """
        if index_to is None:
            index_to = self.product_config.default_index_to

        if index_to == index_from:
            index_to += 1

        pool = ThreadPoolExecutor(self.product_config.num_thread)
        page_per_task = math.ceil((index_to - index_from) / self.product_config.num_thread)
        tasks = collections_helper.chunks_iter(
            [
                {
                    "task_id": i,
                    "task_data": {
                        "params": {},
                        "body": {"PageIndex": i},
                        "run_date_str": run_date_str,
                    },
                }
                for i in range(index_from, index_to + 1)
            ],
            page_per_task,
        )

        logger.info(
            f"there are {index_to - index_from} pages, from {index_from}->{index_to}, {page_per_task} page per task"
        )
        fetch_fn = fetch.fetch_wrapper(
            self.url,
            requests_config.headers,
            self.org_params,
            cattrs.unstructure(self.org_body),
            self.process_result,
            self.cookies,
        )

        results = pool.map(fetch_fn, tasks)

        # flatten results, as it is 3 level deep
        date_dict = defaultdict(list)
        for l1 in results:
            for l2 in l1:
                for row in l2:
                    date_dict[row["date"]].append(row)

        list_data = []
        for date, date_items in date_dict.items():
            list_data += date_items
        if len(list_data) == 0:
            logger.info("No results")
            return
        df_crawled = pl.DataFrame(list_data)
        logger.info(
            f"crawled data date: min={df_crawled['date'].min()}, max={df_crawled['date'].max()}"
            + f" id min={df_crawled['id'].min()}, max={df_crawled['id'].max()}"
            + f", records={len(df_crawled)}"
        )

        # store data
        current_data_count = 0
        if self.product_config.raw_path.exists():
            current_data = pl.read_ndjson(self.product_config.raw_path)
            logger.info(
                f"current data date min={current_data['date'].min()}, max={current_data['date'].max()}"
                + f" id min={current_data['id'].min()}, max={current_data['id'].max()}"
                + f", records={len(current_data)}"
            )
            current_data_count = len(current_data)
            # Use set-based filtering to avoid deprecation warning
            existing_ids = set(current_data["id"].to_list())
            df_take = df_crawled.filter(~pl.col("id").is_in(existing_ids))
            df_final = pl.concat([current_data, df_take])
        else:
            df_final = df_crawled

        # Sort the final dataframe
        assert isinstance(df_final, pl.DataFrame), "df_final should be a DataFrame"
        df_final = df_final.sort(["date", "id"])
        # Convert date column to date type if it's not already
        if df_final["date"].dtype != pl.Date:
            df_final = df_final.with_columns(pl.col("date").str.to_date())

        logger.info(
            f"final data min_date={df_final['date'].min()}, max_date={df_final['date'].max()}"
            + f", records={current_data_count}->{len(df_final)}, diff:{len(df_final) - current_data_count}"
        )
        df_final.write_ndjson(self.product_config.raw_path.absolute())
        logger.info(f"wrote to file {self.product_config.raw_path.absolute()}")
