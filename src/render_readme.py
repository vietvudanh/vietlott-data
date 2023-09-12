from datetime import datetime, timedelta
from io import StringIO
from pathlib import Path

import pandas as pd
from loguru import logger

from vietlott.config.products import get_config
from vietlott.model.strategy.random import RandomModel


def read_data(data_dir: Path):
    df_files = [
        pd.read_json(str(file), dtype=False, convert_dates=False, lines=True)
        for file in data_dir.glob('*.jsonl')
    ]
    print("df_files", len(df_files))
    print(df_files[0])
    df = pd.concat(df_files, axis='rows')
    return df


def read_data_str(data_dir: Path):
    string = ""
    for file in data_dir.glob('*.jsonl'):
        string += file.open('r').read()
    df = pd.read_json(StringIO(string), lines=True, dtype=object, convert_dates=False)
    return df


def main():
    df = pd.read_json(get_config('power_655').raw_path, lines=True, dtype=object, convert_dates=False)
    df['date'] = pd.to_datetime(df['date']).dt.date
    df = df.sort_values(by=['date', 'id'], ascending=False)

    def fn_stats(df_):
        df_explode = df_.explode('result')
        stats = df_explode.groupby('result').agg(
            count=('id', 'count')
        )
        stats['%'] = (stats['count'] / len(df_explode) * 100).round(2)
        return stats

    stats = fn_stats(df)

    # stats n months
    stats_15d = fn_stats(df[df['date'] >= (datetime.now().date() - timedelta(days=15))])
    stats_30d = fn_stats(df[df['date'] >= (datetime.now().date() - timedelta(days=30))])
    stats_60d = fn_stats(df[df['date'] >= (datetime.now().date() - timedelta(days=60))])
    stats_90d = fn_stats(df[df['date'] >= (datetime.now().date() - timedelta(days=90))])

    # predictions
    ticket_per_days = 20
    random_model = RandomModel(df, ticket_per_days)
    random_model.backtest()
    random_model.evaluate()
    df_random_correct = random_model.df_backtest_evaluate[
        random_model.df_backtest_evaluate['correct_num'] >= 5
        ][['date', 'result', 'predicted']]

    output_str = f"""#Vietlot data
## Predictions (just for testing, not a financial advice)
These are backtest results for the strategies I have developed
### random
predicted: {ticket_per_days} / day ({ticket_per_days} tickets perday or {10000 * ticket_per_days:,d} vnd)
predicted corrected:
{df_random_correct.to_markdown()} 

## raw details 6/55
{df.head(10).to_markdown(index=False)}
## stats 6/55 all time
{stats.to_markdown()}
## stats 6/55 -15d
{stats_30d.to_markdown()}
## stats 6/55 -30d
{stats_30d.to_markdown()}
## stats 6/55 -60d
{stats_60d.to_markdown()}
## stats 6/55 -90d
{stats_90d.to_markdown()}
"""
    path_output = Path('./readme.md')
    with path_output.open('w') as ofile:
        logger.info(f'cwd: {Path.cwd()}')
        logger.info(f'writing to {path_output.absolute()}')
        ofile.write(output_str)


if __name__ == "__main__":
    main()
