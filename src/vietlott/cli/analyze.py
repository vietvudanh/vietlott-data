import json
from pathlib import Path
from datetime import datetime

import click
from tabulate import tabulate

from vietlott.config.products import product_config_map


@click.command()
@click.argument("product", default="power_645")
@click.option("--start", "-s", type=int, help="Start number range")
@click.option("--end", "-e", type=int, help="End number range")
def analyze_days_since(product: str, start: int, end: int):
    """Analyze days since last appearance for lottery numbers.

    Example: vietlott-analyze power_645 --start 20 --end 24
    """
    if product not in product_config_map:
        click.echo(f"Product must be in: {list(product_config_map.keys())}", err=True)
        return

    config = product_config_map[product]

    # Load data
    data_file = config.raw_path
    if not data_file.exists():
        click.echo(f"Data file not found: {data_file}", err=True)
        return

    records = []
    with open(data_file, encoding="utf-8") as f:
        for line in f:
            records.append(json.loads(line))

    if not records:
        click.echo("No data found", err=True)
        return

    # Find the last occurrence of each number
    last_occurrence = {}
    for record in records:
        date = datetime.strptime(record["date"], "%Y-%m-%d").date()
        for num in record["result"]:
            if num not in last_occurrence:
                last_occurrence[num] = date
            else:
                last_occurrence[num] = max(last_occurrence[num], date)

    # Get the latest date
    latest_date = datetime.strptime(records[-1]["date"], "%Y-%m-%d").date()

    # Determine the range to analyze
    if start is None:
        start = config.min_value
    if end is None:
        end = config.max_value

    # Validate range
    if start < config.min_value or end > config.max_value:
        click.echo(f"Range must be between {config.min_value} and {config.max_value}", err=True)
        return

    # Calculate days since last appearance
    data = []
    for num in range(start, end + 1):
        if num in last_occurrence:
            last_date = last_occurrence[num]
            days_since = (latest_date - last_date).days
            data.append([num, last_date.strftime("%Y-%m-%d"), days_since])
        else:
            data.append([num, "Never", "N/A"])

    # Sort by days since (descending)
    data.sort(key=lambda x: x[2] if isinstance(x[2], int) else -1, reverse=True)

    headers = ["Number", "Last Appeared", "Days Since"]
    click.echo(f"\n{product.upper()} - Numbers {start}-{end} (Latest: {latest_date})\n")
    click.echo(tabulate(data, headers=headers, tablefmt="grid"))
    click.echo()


if __name__ == "__main__":
    analyze_days_since()
