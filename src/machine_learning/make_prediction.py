#!/usr/bin/env python
"""
Generate lottery predictions using the top 5 ML strategies and write result.txt.

Usage:
    python make_prediction.py --product power_655
    python make_prediction.py --product power_655 --predict-date 2026-05-13
    python make_prediction.py --product power_655 --index-from 0 --index-to 5
    python make_prediction.py --product power_655 --output my_result.txt
"""

import smtplib
import sys
import time
from collections import Counter
from contextlib import contextmanager
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import pandas as pd
import click
import pendulum
import polars as pl
from loguru import logger

from machine_learning.strategies import (
    ColdNumbersStrategy,
    ExponentialDecayStrategy,
    LongAbsenceStrategy,
    MarkovChainStrategy,
    PairFrequencyStrategy,
)
from vietlott.config.map_class import map_class_name
from vietlott.config.products import ProductConfig, get_config, product_config_map

# Top 5 strategies by backtest ROI (Random excluded — no predictive logic).
# Each entry: (display_name, factory(df, cfg) -> model)
_STRATEGY_DEFS = [
    ("Markov Chain      ", lambda df, cfg: _make(MarkovChainStrategy, df, cfg, lookback_days=365, smoothing=0.5)),
    ("Long Absence      ", lambda df, cfg: _make(LongAbsenceStrategy, df, cfg, top_n=15)),
    ("Cold Numbers      ", lambda df, cfg: _make(ColdNumbersStrategy, df, cfg, lookback_days=365, selection_weight=0.7)),
    ("Exponential Decay ", lambda df, cfg: _make(ExponentialDecayStrategy, df, cfg, half_life_days=90, hot=True, selection_weight=0.8)),
    ("Pair Frequency    ", lambda df, cfg: _make(PairFrequencyStrategy, df, cfg, lookback_days=365)),
]


def _make(cls, df, cfg: ProductConfig, **kwargs):
    """Instantiate a strategy with the correct number range from product config."""
    model = cls(df, time_predict=1, min_val=cfg.min_value, max_val=cfg.max_value, **kwargs)
    model.number_predict = cfg.size_output
    return model


@contextmanager
def _timed(step: str):
    logger.info(f"[START] {step}")
    t0 = time.perf_counter()
    yield
    elapsed = time.perf_counter() - t0
    logger.info(f"[DONE ] {step}  ({elapsed:.2f}s)")


def _send_email(smtp_user: str, smtp_password: str, to: str, subject: str, body: str) -> None:
    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to, msg.as_string())


def _fetch_data(product: str, run_date: str, index_from: int, index_to) -> None:
    product_obj = map_class_name[product]()
    product_obj.crawl(
        run_date_str=run_date,
        index_from=index_from,
        index_to=index_to,
    )


def _normalize_result(value) -> list:
    """Flatten any result shape to a plain list of Python ints.

    Handles:
    - list/array of ints or int-like scalars  (power*, keno, bingo18)
    - dict of prize-category → list of str    (3d, 3d_pro)
    """
    if value is None:
        return []
    if isinstance(value, dict):
        nums = []
        for prizes in value.values():
            if isinstance(prizes, (list, tuple)):
                for v in prizes:
                    try:
                        nums.append(int(v))
                    except (ValueError, TypeError):
                        pass
        return nums
    try:
        return [int(v) for v in value]
    except (TypeError, ValueError):
        return []


def _load_data(product: str) -> pl.DataFrame:
    try:
        df = pl.read_ndjson(get_config(product).raw_path)
        if "date" not in df.columns:
            return df
        try:
            if df["date"].dtype in [pl.Date, pl.Datetime]:
                df = df.with_columns(pl.col("date").cast(pl.Date))
            elif df["date"].dtype in [pl.Int64, pl.Int32, pl.Float64]:
                max_val = df["date"].max()
                if max_val > 1_000_000_000_000:
                    df = df.with_columns(
                        (pl.col("date").cast(pl.Int64) / 1000).cast(pl.Datetime("ms")).cast(pl.Date)
                    )
                else:
                    df = df.with_columns(pl.col("date").cast(pl.Int64).cast(pl.Datetime("s")).cast(pl.Date))
            else:
                df = df.with_columns(pl.col("date").str.to_date(strict=False))
        except Exception as e:
            logger.warning(f"Could not parse date column: {e}")
            df = df.with_columns(pl.col("date").str.to_date(strict=False))
        return df.sort(["date", "id"], descending=True)
    except Exception as e:
        logger.error(f"Error loading data for {product}: {e}")
        return pl.DataFrame()


def _format_numbers(nums: list) -> str:
    return "  ".join(f"{n:2d}" for n in nums) if nums else "N/A"


@click.command()
@click.option("--product", required=True, help="Lottery product to predict for.")
@click.option(
    "--predict-date",
    default=None,
    help="Date to predict for (YYYY-MM-DD). Defaults to today (Vietnam time).",
)
@click.option(
    "--index-from",
    default=0,
    type=int,
    show_default=True,
    help="Crawl pagination start index.",
)
@click.option(
    "--index-to",
    default=None,
    type=int,
    help="Crawl pagination end index (omit to crawl all pages).",
)
@click.option(
    "--output",
    default="result.txt",
    show_default=True,
    help="Output file path.",
)
def make_prediction(
    product: str,
    predict_date: str,
    index_from: int,
    index_to,
    output: str,
) -> None:
    """Fetch latest data, then predict lottery numbers using the top 5 ML strategies."""
    if product not in product_config_map:
        logger.error(f"Unknown product '{product}'. Available: {list(product_config_map.keys())}")
        sys.exit(1)

    run_date = pendulum.now(tz="Asia/Ho_Chi_Minh").to_date_string()
    pred_date: date = date.fromisoformat(predict_date) if predict_date else pendulum.now(tz="Asia/Ho_Chi_Minh").date()
    generated_at = pendulum.now(tz="Asia/Ho_Chi_Minh").strftime("%Y-%m-%d %H:%M:%S")

    t_total = time.perf_counter()
    cfg = get_config(product)
    logger.info(f"product={product}  run_date={run_date}  predict_date={pred_date}")
    logger.info(f"number range={cfg.min_value}–{cfg.max_value}  pick={cfg.size_output}")
    logger.info(f"crawl index_from={index_from}  index_to={index_to}")

    # Step 1 — fetch
    with _timed(f"Fetch data  (index {index_from}–{index_to if index_to is not None else 'end'})"):
        try:
            _fetch_data(product, run_date, index_from, index_to)
        except Exception as e:
            logger.warning(f"Fetch failed (continuing with existing data): {e}")

    # Step 2 — load
    with _timed("Load data from disk"):
        df_pl = _load_data(product)
        if df_pl.is_empty():
            logger.error("No data loaded. Aborting.")
            sys.exit(1)
        df_pd = df_pl.to_pandas()
        if "result" in df_pd.columns:
            df_pd["result"] = df_pd["result"].apply(_normalize_result)
        logger.info(f"Loaded {len(df_pd):,} rows")

    # Step 3 — predict
    predictions: dict[str, list[int]] = {}
    for name, factory in _STRATEGY_DEFS:
        with _timed(f"Strategy: {name.strip()}"):
            try:
                model = factory(df_pd, cfg)
                predictions[name] = sorted(model.predict(pd.Timestamp(pred_date)))
            except Exception as e:
                logger.error(f"{name.strip()} failed: {e}")
                predictions[name] = []

    # Step 4 — consensus
    with _timed("Compute consensus"):
        votes: Counter = Counter()
        for nums in predictions.values():
            votes.update(nums)
        consensus = sorted(
            [num for num, _ in sorted(votes.most_common(), key=lambda x: (-x[1], x[0]))[:cfg.size_output]]
        )

    # Step 5 — write output
    with _timed(f"Write result to {output}"):
        sep = "=" * 52
        thin = "-" * 52

        lines = [
            sep,
            f"  Vietlott Prediction — {product.upper()}",
            f"  Predict date : {pred_date}",
            f"  Generated at : {generated_at} (ICT)",
            sep,
            "",
            "Individual Strategy Predictions",
            thin,
        ]

        for name, nums in predictions.items():
            lines.append(f"{name}: {_format_numbers(nums)}")

        lines += [
            "",
            sep,
            "Consensus  (top-voted numbers across all strategies)",
            thin,
            f"  {_format_numbers(consensus)}",
            "",
            "Number vote breakdown",
            thin,
        ]

        max_votes = max(votes.values(), default=1)
        for num in sorted(votes.keys()):
            v = votes[num]
            bar = "#" * v + "." * (max_votes - v)
            lines.append(f"  {num:2d}  [{bar}]  {v}/{len(_STRATEGY_DEFS)}")

        lines += [
            "",
            sep,
            "Disclaimer: For referral purposes only.",
            "Lottery outcomes are random and cannot be reliably predicted.",
            sep,
        ]

        output_path = Path(output)
        output_path.write_text("\n".join(lines), encoding="utf-8")

    logger.info(f"Done. Result written to {output_path.absolute()}")

    # Step 6 — email
    _smtp_user = "kimnguyenvn085@gmail.com"
    _smtp_password = "dflk ysxq nkjj alck"
    _to = "kimnguyen085@gmail.com"
    with _timed(f"Send email to {_to}"):
        try:
            subject = f"Vietlott Prediction — {product.upper()} — {pred_date}"
            _send_email(_smtp_user, _smtp_password, _to, subject, output_path.read_text(encoding="utf-8"))
            logger.info(f"Email sent to {_to}")
        except Exception as e:
            logger.error(f"Email failed: {e}")

    logger.info(f"Total time: {time.perf_counter() - t_total:.2f}s")


if __name__ == "__main__":
    make_prediction()
