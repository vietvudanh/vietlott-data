import click
import pandas as pd
from loguru import logger

from vietlott.config.products import product_config_map, ProductConfig


@click.command()
@click.pass_context
@click.argument('product')
def detect_missing_data(ctx, product):
    """detect_missing_data"""
    if product not in product_config_map:
        click.echo(f"Error:: Product must in product_map: {list(product_config_map.keys())}", err=True)
        ctx.exit(1)
    click.echo(f'product={product}')

    product_cfg: ProductConfig = product_config_map[product]
    df = pd.read_json(product_cfg.raw_path, lines=True)
    print(df['id'].dtype)
    if df['id'].dtype == 'object':
        df['id'] = df['id'].str.replace('#', '').astype(int)
    df['id_next'] = df['id'].shift(-1)
    df['diff'] = df['id_next'] - df['id']

    df_missing = df[df['diff'] != 1]
    logger.info('\n' + df_missing[['date', 'id', 'id_next', 'diff']].to_markdown())


if __name__ == '__main__':
    detect_missing_data()
