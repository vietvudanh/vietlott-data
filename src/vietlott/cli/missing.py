import math

import click
import pendulum
import polars as pl
from loguru import logger

from vietlott.config.map_class import map_class_name
from vietlott.config.products import ProductConfig, product_config_map
from vietlott.crawler.products import BaseProduct


@click.command()
@click.pass_context
@click.argument("product")
@click.option("--limit", default=20)
def detect_missing_data(ctx, product, limit):
    """
    detect_missing_data and run if needed
    :param ctx: context
    :param product: product to run
    :param limit: number of pages to run
    :return:
    """
    if product not in product_config_map:
        logger.error(f"Product must be in product_map: {list(product_config_map.keys())}")
        ctx.exit(1)
    logger.info(f"product={product}, limit={limit}")

    product_cfg: ProductConfig = product_config_map[product]
    df = pl.read_ndjson(product_cfg.raw_path)
    logger.info(f"ID column data type: {df['id'].dtype}")
    # Handle both string and numeric IDs
    if df["id"].dtype == pl.String:
        df = df.with_columns(pl.col("id").str.replace("#", "").cast(pl.Int64))
    df = df.with_columns(pl.col("id").shift(-1).alias("id_next"))
    df = df.with_columns((pl.col("id_next") - pl.col("id")).alias("diff"))

    df_missing = df.filter(pl.col("diff") > 1)
    last_id = df["id"].max()
    df_missing = df_missing.with_columns(
        ((last_id - pl.col("id")) / product_cfg.page_size).alias("index"),
        ((last_id - pl.col("id_next")) / product_cfg.page_size).alias("index_next"),
    )
    df_missing_process = df_missing.reverse().slice(1, limit)

    # Convert to pandas for markdown display (tabulate doesn't support polars well yet)
    df_display = df_missing_process.select(["date", "id", "id_next", "diff", "index", "index_next"]).to_pandas()
    logger.info("\n" + df_display.to_markdown())

    run_date = pendulum.now(tz="Asia/Ho_Chi_Minh").to_date_string()
    product_obj: BaseProduct = map_class_name[product]()
    for row in df_missing_process.iter_rows(named=True):
        if (row["index"] - row["index_next"]) > 50:
            step = 20
            for i in range(int(math.floor(row["index_next"])), int(math.ceil(row["index"])), step):
                product_obj.crawl(
                    run_date_str=run_date,
                    index_from=i,
                    index_to=i + step,
                )
        else:
            product_obj.crawl(
                run_date_str=run_date,
                index_from=int(math.floor(row["index_next"])),
                index_to=int(math.ceil(row["index"])),
            )


if __name__ == "__main__":
    detect_missing_data()
