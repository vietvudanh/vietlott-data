#!/usr/bin/env python
"""
Prediction Summary Generator for Vietlott Data Project.

This script generates a prediction summary markdown file for the machine learning module.
It outputs detailed prediction reports with statistics for each strategy.
"""

from datetime import datetime
from pathlib import Path
from typing import Optional

import polars as pl
from loguru import logger

from machine_learning.base import PredictModel
from machine_learning.random_strategy import RandomModel
from vietlott.config.products import get_config


class PredictionSummaryGenerator:
    """Generator for prediction summary."""

    def __init__(self):
        pass

    def _load_lottery_data(self, product: str) -> pl.DataFrame:
        """Load and prepare lottery data for predictions."""
        try:
            df = pl.read_ndjson(get_config(product).raw_path)

            if "date" in df.columns:
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

            df = df.sort(["date", "id"], descending=True)
            return df
        except Exception as e:
            logger.error(f"Error loading data for {product}: {e}")
            return pl.DataFrame()

    def _to_int(self, v) -> int:
        """Convert value to integer safely."""
        try:
            return int(v)
        except Exception:
            try:
                return len(v)
            except Exception:
                return 0

    def _generate_strategy_report(self, model: PredictModel, strategy_name: str, tickets_per_day: int) -> str:
        """Generate detailed report for a single strategy."""
        df_eval = model.df_backtest_evaluate
        if df_eval is None or df_eval.empty:
            return f"### {strategy_name}\n\n> No evaluation data available.\n"

        # Calculate statistics
        total_draws = len(model.df_backtest)
        total_predictions = len(df_eval)
        cost, gain, profit = model.revenue()

        # Match distribution
        s_correct = df_eval["correct_num"].apply(self._to_int).astype(int)
        match_counts = s_correct.value_counts().sort_index(ascending=False)
        match_distribution = "\n".join(
            [f"  - **{matches} matches**: {count:,} times" for matches, count in match_counts.items()]
        )

        # Best results (5+ matches)
        mask = (s_correct >= 5).to_numpy()
        df_best = df_eval.loc[mask, ["date", "result", "predicted", "correct_num"]].copy()
        df_best["result"] = df_best["result"].apply(
            lambda x: str([int(i) for i in x]) if hasattr(x, "__iter__") else str(x)
        )
        df_best["predicted"] = df_best["predicted"].apply(
            lambda x: str([int(i) for i in x]) if hasattr(x, "__iter__") else str(x)
        )
        df_best["correct_num"] = df_best["correct_num"].apply(self._to_int)

        best_results_table = (
            df_best.to_markdown(index=False) if not df_best.empty else "No results with 5+ matches found."
        )

        # Date range
        date_min = df_eval["date"].min()
        date_max = df_eval["date"].max()

        return f"""### 🎲 {strategy_name}

#### Configuration
| Parameter | Value |
|-----------|-------|
| Strategy | {strategy_name} |
| Tickets per day | {tickets_per_day} |
| Ticket price | {model.ticket_price:,} VND |
| Number range | {model.min_val} - {model.max_val} |
| Numbers to pick | {model.number_predict} |

#### Backtest Period
| Metric | Value |
|--------|-------|
| Start date | {date_min} |
| End date | {date_max} |
| Total draws | {total_draws:,} |
| Total predictions | {total_predictions:,} |

#### Financial Summary
| Metric | Value |
|--------|-------|
| Total cost | {cost:,} VND |
| Total gain | {gain:,} VND |
| Net profit/loss | {profit:,} VND |
| ROI | {(profit / cost * 100) if cost > 0 else 0:.2f}% |

#### Match Distribution
{match_distribution}

#### Best Results (5+ matches)
{best_results_table}

"""

    def _generate_predictions_section(self, df: pl.DataFrame) -> str:
        """Generate predictions section with detailed reports."""
        if df.is_empty():
            return "## 🔮 Prediction Models\n\n> No data available for predictions.\n"

        try:
            df_pd = df.to_pandas()
            reports = []

            # Random Strategy
            tickets_per_day = 20
            random_model = RandomModel(df_pd, tickets_per_day)
            random_model.backtest()
            random_model.evaluate()
            reports.append(self._generate_strategy_report(random_model, "Random Strategy", tickets_per_day))

            return f"""## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

{"".join(reports)}
"""
        except Exception as e:
            logger.exception(f"Error generating predictions: {e}")
            raise

    def generate_prediction_summary(self) -> str:
        """Generate the complete prediction summary content."""
        logger.info("Starting prediction summary generation...")

        df_power655 = self._load_lottery_data("power_655")
        predictions = self._generate_predictions_section(df_power655)

        summary_content = f"""# 🔮 Vietlott Prediction Summary

> **Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
>
> This document contains machine learning predictions for Vietnamese lottery data.
> This is an experimental module for educational purposes only.

{predictions}

---

## ⚠️ Disclaimer

This prediction summary is for educational and research purposes only. Lottery outcomes are random and cannot be reliably predicted. Never gamble more than you can afford to lose.
"""

        return summary_content

    def save_prediction_summary(self, output_path: Optional[Path] = None) -> None:
        """Generate and save prediction summary to file."""
        if output_path is None:
            output_path = Path(__file__).parent / "prediction_summary.md"

        try:
            summary_content = self.generate_prediction_summary()

            with output_path.open("w", encoding="utf-8") as ofile:
                ofile.write(summary_content)

            logger.info(f"Prediction summary successfully written to {output_path.absolute()}")
        except Exception as e:
            logger.error(f"Error saving prediction summary: {e}")
            raise


def main():
    """Main entry point for prediction summary generation."""
    try:
        generator = PredictionSummaryGenerator()
        generator.save_prediction_summary()
        logger.info("Prediction summary generation completed successfully!")
    except Exception as e:
        logger.error(f"Failed to generate prediction summary: {e}")
        raise


if __name__ == "__main__":
    main()
