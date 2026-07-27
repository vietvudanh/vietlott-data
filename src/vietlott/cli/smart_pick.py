import json
from pathlib import Path
from datetime import datetime
from collections import Counter
import random

import click
from tabulate import tabulate

from vietlott.config.products import product_config_map


@click.command()
@click.argument("product", default="power_655")
@click.option("--tickets", "-t", default=6, type=int, help="Number of tickets to generate")
@click.option("--rare-ratio", default=0.5, type=float, help="Ratio of rare numbers (0-1)")
def smart_pick(product: str, tickets: int, rare_ratio: float):
    """Generate smart tickets combining rare numbers (ít gặp) + frequent numbers (hay trúng).

    Example: vietlott-smart-pick power_655 --tickets 6 --rare-ratio 0.5
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

    # Analyze: find last occurrence and frequency of each number
    last_occurrence = {}
    all_numbers = []
    
    for record in records:
        date = datetime.strptime(record["date"], "%Y-%m-%d").date()
        for num in record["result"]:
            all_numbers.append(num)
            if num not in last_occurrence:
                last_occurrence[num] = date
            else:
                last_occurrence[num] = max(last_occurrence[num], date)

    # Get the latest date
    latest_date = datetime.strptime(records[-1]["date"], "%Y-%m-%d").date()

    # Count frequency
    frequency = Counter(all_numbers)

    # Classify numbers
    # Rare numbers: haven't appeared for a long time
    rare_numbers = sorted(
        [num for num in range(config.min_value, config.max_value + 1) 
         if num in last_occurrence and (latest_date - last_occurrence[num]).days > 30],
        key=lambda x: (latest_date - last_occurrence[x]).days,
        reverse=True
    )
    
    # Frequent numbers: appeared recently and frequently
    frequent_numbers = sorted(
        [num for num in range(config.min_value, config.max_value + 1)
         if num in last_occurrence and (latest_date - last_occurrence[num]).days <= 10],
        key=lambda x: frequency.get(x, 0),
        reverse=True
    )

    # Ensure we have enough numbers
    if not rare_numbers:
        rare_numbers = sorted(
            range(config.min_value, config.max_value + 1),
            key=lambda x: (latest_date - last_occurrence.get(x, latest_date)).days,
            reverse=True
        )[:10]

    if not frequent_numbers:
        frequent_numbers = sorted(
            range(config.min_value, config.max_value + 1),
            key=lambda x: frequency.get(x, 0),
            reverse=True
        )[:15]

    # Generate tickets with mix of rare and frequent numbers
    result_tickets = []
    for _ in range(tickets):
        num_rare = max(1, int(config.size_output * rare_ratio))
        num_frequent = config.size_output - num_rare

        # Pick rare numbers
        selected_rare = random.sample(rare_numbers, min(num_rare, len(rare_numbers)))
        # Pick frequent numbers
        selected_frequent = random.sample(frequent_numbers, min(num_frequent, len(frequent_numbers)))

        # Combine and sort
        ticket = sorted(selected_rare + selected_frequent)
        # Ensure no duplicates
        while len(set(ticket)) < len(ticket):
            ticket = sorted(random.sample(
                list(range(config.min_value, config.max_value + 1)),
                config.size_output
            ))

        result_tickets.append(ticket)

    # Display results
    headers = ["Ticket"] + [f"So {i}" for i in range(1, config.size_output + 1)]
    data = [[i + 1] + ticket for i, ticket in enumerate(result_tickets)]

    click.echo(f"\n{product.upper()} - {tickets} Smart Tickets (Rare: {rare_ratio*100:.0f}%, Frequent: {(1-rare_ratio)*100:.0f}%)\n")
    click.echo(tabulate(data, headers=headers, tablefmt="grid"))
    click.echo()

    # Show statistics
    click.echo(f"\nStatistics (Latest: {latest_date}):")
    click.echo(f"  * Rare numbers (30+ days): {len(rare_numbers)} numbers")
    click.echo(f"  * Frequent numbers (<=10 days): {len(frequent_numbers)} numbers")
    if rare_numbers:
        click.echo(f"  * Rarest: {rare_numbers[0]} ({(latest_date - last_occurrence[rare_numbers[0]]).days} days ago)")
    if frequent_numbers:
        click.echo(f"  * Most frequent recently: {frequent_numbers[0]} (appeared {frequency[frequent_numbers[0]]} times)")
    click.echo()


if __name__ == "__main__":
    smart_pick()
