import random
import sys
import os

import click
from tabulate import tabulate

from vietlott.config.products import product_config_map

# Fix encoding on Windows
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"


@click.command()
@click.argument("product", default="power_655")
@click.option("--count", "-c", default=1, type=int, help="Number of tickets to pick")
def pick(product: str, count: int):
    """Pick random numbers for a lottery product.

    Example: vietlott-pick power_655 --count 6
    """
    if product not in product_config_map:
        click.echo(f"Product must be in: {list(product_config_map.keys())}", err=True)
        return

    config = product_config_map[product]

    if count < 1:
        click.echo("Count must be >= 1", err=True)
        return

    tickets = []
    for i in range(count):
        numbers = sorted(random.sample(range(config.min_value, config.max_value + 1), config.size_output))
        tickets.append([i + 1] + numbers)

    headers = ["Ticket"] + [f"So {j}" for j in range(1, config.size_output + 1)]
    click.echo(f"\n{product.upper()} - {count} tickets picked:\n", nl=False)
    click.echo(tabulate(tickets, headers=headers, tablefmt="grid"))
    click.echo()


if __name__ == "__main__":
    pick()
