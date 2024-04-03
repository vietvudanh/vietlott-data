import click
import pendulum

from vietlott.config.products import product_config_map
from vietlott.crawler.products import BaseProduct, ProductPower655, ProductPower645, ProductKeno

_map_class_name = {
    "keno": ProductKeno,
    "power_655": ProductPower655,
    "power_645": ProductPower645,
}


@click.command()
@click.pass_context
@click.argument("product")
@click.option("--run-date", default=pendulum.now(tz="Asia/Ho_Chi_Minh").to_date_string())
@click.option("--index_from", default=0, type=int, help="page index from run since we crawl by pagination the pages")
@click.option("--index_to", default=None, type=int, help="page index from run since we crawl by pagination the pages")
def crawl(ctx, product, run_date, index_from, index_to):
    """
    crawl a product with a given run date or from/to index page
    :param ctx:
    :param product:
    :param run_date:
    :param index_from:
    :param index_to:
    :return:
    """
    if product not in product_config_map:
        click.echo(f"Error:: Product must in product_map: {list(product_config_map.keys())}", err=True)
        ctx.exit(1)
    click.echo(f"product={product}")

    product_obj: BaseProduct = _map_class_name[product]()
    product_obj.crawl(
        run_date_str=run_date,
        index_from=index_from,
        index_to=index_to,
    )


if __name__ == "__main__":
    crawl()
