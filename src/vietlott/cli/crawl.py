import click
import pendulum
import logging

from vietlott.config.map_class import map_class_name
from vietlott.config.products import product_config_map
from vietlott.crawler.products import BaseProduct

logger = logging.getLogger(__name__)


@click.command()
@click.pass_context
@click.argument("product")
@click.option("--run-date", default=None)
@click.option("--index_from", default=0)
@click.option("--index_to", default=None)
def crawl(ctx, product, run_date, index_from, index_to):
    """crawl data for a specific product"""
    # Exclude bingo18 from crawling
    if product == "bingo18":
        logger.warning("Bingo18 is currently excluded from crawling")
        return
    
    logger.info(f"Starting crawl for product: {product}")
    
    try:
        product_class = map_class_name.get(product)
        if product_class is None:
            logger.error(f"Unknown product: {product}")
            return

        product_obj = product_class()
        product_obj.crawl(run_date, index_from, index_to)
        logger.info(f"Successfully crawled data for {product}")
    except Exception as e:
        logger.error(f"Error crawling {product}: {e}")
        raise


if __name__ == "__main__":
    crawl()
