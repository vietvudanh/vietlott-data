# /usr/bin/env python
"""
this script is used to render the README.md that shows in repo's Github
"""

import pandas as pd
from datetime import datetime, timedelta
from io import StringIO
from loguru import logger
from pathlib import Path

from vietlott.config.products import get_config
from vietlott.model.strategy.random import RandomModel

include_toc = """- [Vietlot data](#vietlot-data)
  * [Predictions (just for testing, not a financial advice)](#predictions--just-for-testing--not-a-financial-advice-)
    + [random](#random)
  * [raw details 6/55](#raw-details-6-55)
  * [stats 6/55 all time](#stats-6-55-all-time)
  * [stats 6/55 -15d](#stats-6-55--15d)
  * [stats 6/55 -30d](#stats-6-55--30d)
  * [stats 6/55 -60d](#stats-6-55--60d)
  * [stats 6/55 -90d](#stats-6-55--90d)
- [Install](#install)
  * [via pip](#via-pip)
  * [cli](#cli)
    + [crawl](#crawl)
    + [Backfill missing data](#backfill-missing-data)
"""
include_how_it_works = """# How project works
Since there are many people asked, I write this section.

## Schedule
The project is schedule automatically via Github Actions, run a script, fetch data and auto commit to Github. No server is required, I don't need to do anything.
Details in [workflow file](https://github.com/vietvudanh/vietlott-data/blob/dffb2bcdfa860a0dfc3f2e22e269e6978d478965/.github/workflows/crawl.yaml#L8)

## How crawling works
I just inspected network packages sent between browser and server to find out how data is fetched and replicated that in Python code. 
"""
include_install_section = """# Install
 
## via pip

```shell
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.3
```

## cli
project provides two cli

### crawl
```shell
Usage: vietlott-crawl [OPTIONS] PRODUCT

  crawl a product with a given run date or from/to index page 

Options:
  --run-date TEXT
  --index_from INTEGER  page index from run since we crawl by pagination the
                        pages
  --index_to INTEGER    page index from run since we crawl by pagination the
                        pages
  --help                Show this message and exit.
```

### Backfill missing data

```shell
Usage: vietlott-missing [OPTIONS] PRODUCT

  detect_missing_data and run if needed :param ctx: context :param product:
  product to run :param limit: number of pages to run :return:

Options:
  --limit INTEGER
  --help           Show this message and exit.
```
"""


def _balance_long_df(df_: pd.DataFrame, n_splits: int = 20):
    """convert long dataframe to multiple columns"""
    df_ = df_.reset_index()
    df_["result"] = df_["result"].astype(str)
    df_["count"] = df_["count"].astype(str)

    final = None

    for i in range(len(df_) // n_splits + 1):
        dd = df_.iloc[i * n_splits : (i + 1) * n_splits]

        if final is None:
            final = dd
        else:
            final = pd.concat(
                [
                    final.reset_index(drop=True),
                    pd.DataFrame([None] * len(dd), columns=["-"]),
                    dd.reset_index(drop=True),
                ],
                axis="columns",
            )
    final = final.fillna("")

    return final


def read_data(data_dir: Path):
    df_files = [
        pd.read_json(str(file), dtype=False, convert_dates=False, lines=True) for file in data_dir.glob("*.jsonl")
    ]
    logger.info("df_files: %d", len(df_files))
    logger.info(df_files[0])
    df = pd.concat(df_files, axis="rows")
    return df


def read_data_str(data_dir: Path):
    string = ""
    for file in data_dir.glob("*.jsonl"):
        string += file.open("r").read()
    df = pd.read_json(StringIO(string), lines=True, dtype=object, convert_dates=False)
    return df


def main():
    df = pd.read_json(get_config("power_655").raw_path, lines=True, dtype=object, convert_dates=False)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df = df.sort_values(by=["date", "id"], ascending=False)

    def fn_stats(df_):
        df_explode = df_.explode("result")
        stats = df_explode.groupby("result").agg(count=("id", "count"))
        stats["%"] = (stats["count"] / len(df_explode) * 100).round(2)
        return stats

    stats = _balance_long_df(fn_stats(df))

    # stats n months
    # stats_15d = _balance_long_df(fn_stats(df[df["date"] >= (datetime.now().date() - timedelta(days=15))]))
    stats_30d = _balance_long_df(fn_stats(df[df["date"] >= (datetime.now().date() - timedelta(days=30))]))
    stats_60d = _balance_long_df(fn_stats(df[df["date"] >= (datetime.now().date() - timedelta(days=60))]))
    stats_90d = _balance_long_df(fn_stats(df[df["date"] >= (datetime.now().date() - timedelta(days=90))]))

    # predictions
    ticket_per_days = 20
    random_model = RandomModel(df, ticket_per_days)
    random_model.backtest()
    random_model.evaluate()
    df_random_correct = random_model.df_backtest_evaluate[random_model.df_backtest_evaluate["correct_num"] >= 5][
        ["date", "result", "predicted"]
    ]

    output_str = f"""# Vietlot data

Data crawling from https://vietlott.vn/, results for products:
- [6/55](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655)
- [6/45](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645)
- [Keno](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno)
- [Max 3D](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d)
- [Max 3D Pro](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro)

{include_toc}

## Predictions (just for testing, not a financial advice)
These are backtest results for the strategies I have tested (just the abstract method at the moment, you can't predict lotery lol)

### random strategy
predicted: {ticket_per_days} / day ({ticket_per_days} tickets perday or {10000 * ticket_per_days:,d} vnd)
predicted corrected:
{df_random_correct.to_markdown()} 

## raw details 6/55 last 10 days
{df.head(10).to_markdown(index=False)}
## stats 6/55 all time
{stats.to_markdown(index=False)}
## stats 6/55 -15d
{stats_30d.to_markdown(index=False)}
## stats 6/55 -30d
{stats_30d.to_markdown(index=False)}
## stats 6/55 -60d
{stats_60d.to_markdown(index=False)}
## stats 6/55 -90d
{stats_90d.to_markdown(index=False)}

{include_how_it_works}
{include_install_section}
"""
    path_output = Path("./readme.md")
    with path_output.open("w") as ofile:
        logger.info(f"cwd: {Path.cwd()}")
        logger.info(f"writing to {path_output.absolute()}")
        ofile.write(output_str)


if __name__ == "__main__":
    main()
