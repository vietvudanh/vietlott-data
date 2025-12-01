#!/usr/bin/env python
"""
Prediction Summary Generator for Vietlott Data Project.

This script generates a prediction summary markdown file for the machine learning module.
It extracts prediction logic from the main README generator and outputs to a separate file.
"""

from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import pandas as pd
import polars as pl
from loguru import logger

from vietlott.config.products import get_config

from .random_strategy import RandomModel


class PredictionSummaryGenerator:
    """Generator for prediction analysis summary."""

    def __init__(self):
        pass

    def _balance_long_df(self, df_: pl.DataFrame, n_splits: int = 20) -> pl.DataFrame:
        """Convert long dataframe to multiple columns for better display."""
        if df_.is_empty():
            return df_

        df_pd = df_.to_pandas()

        # reset_index may return a view in some edge-cases; work on an explicit copy
        df_pd = df_pd.reset_index().copy()
        # Create converted columns in a separate DataFrame and concat them back to
        # avoid assigning object-dtype data into existing numeric columns which
        # can trigger FutureWarnings about incompatible dtype setting.
        if "result" in df_pd.columns and "count" in df_pd.columns:
            converted = pd.DataFrame(
                {
                    "result": df_pd["result"].apply(lambda x: str(x)).astype(object),
                    "count": df_pd["count"].apply(lambda x: str(x)).astype(object),
                },
                index=df_pd.index,
            )
            # drop original columns then concat converted ones to preserve order
            left = df_pd.drop(columns=["result", "count"])
            df_pd = pd.concat([left, converted], axis=1)

        final = None

        for i in range(len(df_pd) // n_splits + 1):
            dd = df_pd.iloc[i * n_splits : (i + 1) * n_splits]

            if dd.empty:
                continue

            if final is None:
                final = dd
            else:
                final = pd.concat(
                    [
                        final.reset_index(drop=True),
                        pd.DataFrame([None] * len(dd), columns=["-"]).add_prefix(str(i)),
                        dd.reset_index(drop=True).add_prefix(str(i)),
                    ],
                    axis="columns",
                )

        if final is not None:
            # ensure we operate on an explicit copy before filling
            final = final.copy().fillna("")

            # Guarantee unique, string-based column names before conversion
            seen: dict[str, int] = {}
            renamed_columns = []
            for col in final.columns:
                col_str = str(col)
                if col_str in seen:
                    seen[col_str] += 1
                    col_str = f"{col_str}_{seen[col_str]}"
                else:
                    seen[col_str] = 0
                renamed_columns.append(col_str)
            final.columns = renamed_columns

            # Convert everything to string for display to avoid numeric columns with empty strings
            data = {}
            for col in final.columns:
                col_values = []
                for value in final[col].tolist():
                    if value == "":
                        col_values.append("")
                    else:
                        col_values.append(str(value))
                data[col] = col_values

            return pl.DataFrame(data)
        else:
            return pl.DataFrame()

    def _load_lottery_data(self, product: str) -> pl.DataFrame:
        """Load and prepare lottery data for analysis."""
        try:
            df = pl.read_ndjson(get_config(product).raw_path)

            # Normalize/parse date column which can be in multiple formats
            if "date" in df.columns:
                # Try to parse the date column
                try:
                    # Check if it's already a date type
                    if df["date"].dtype in [pl.Date, pl.Datetime]:
                        df = df.with_columns(pl.col("date").cast(pl.Date))
                    # Check if it's numeric (epoch time)
                    elif df["date"].dtype in [pl.Int64, pl.Int32, pl.Float64]:
                        # Check if values are in milliseconds or seconds
                        max_val = df["date"].max()
                        if max_val > 1_000_000_000_000:
                            # milliseconds
                            df = df.with_columns(
                                (pl.col("date").cast(pl.Int64) / 1000).cast(pl.Datetime("ms")).cast(pl.Date)
                            )
                        else:
                            # seconds
                            df = df.with_columns(pl.col("date").cast(pl.Int64).cast(pl.Datetime("s")).cast(pl.Date))
                    else:
                        # String date - try to parse
                        df = df.with_columns(pl.col("date").str.to_date(strict=False))
                except Exception as e:
                    logger.warning(f"Could not parse date column: {e}")
                    # Fallback: try string parsing
                    df = df.with_columns(pl.col("date").str.to_date(strict=False))

            df = df.sort(["date", "id"], descending=True)
            return df
        except Exception as e:
            logger.error(f"Error loading data for {product}: {e}")
            return pl.DataFrame()

    def _calculate_stats(self, df: pl.DataFrame) -> pl.DataFrame:
        """Calculate number frequency statistics."""
        if df.is_empty():
            return pl.DataFrame()

        df_explode = df.explode("result")
        stats = df_explode.group_by("result").agg(pl.count("id").alias("count"))
        total_count = len(df_explode)
        stats = stats.with_columns(((pl.col("count") / total_count * 100).round(2)).alias("%"))
        return stats

    def _generate_predictions_section(self, df: pl.DataFrame) -> str:
        """Generate predictions analysis section."""
        if df.is_empty():
            return "## 🔮 Prediction Models\n\n> No data available for predictions.\n"

        try:
            # Convert to pandas for the model (if it expects pandas)
            df_pd = df.to_pandas()

            ticket_per_days = 20
            random_model = RandomModel(df_pd, ticket_per_days)
            random_model.backtest()
            random_model.evaluate()

            # Coerce `correct_num` to integer safely before applying threshold
            if "correct_num" in random_model.df_backtest_evaluate.columns:

                def _to_int(v):
                    try:
                        return int(v)
                    except Exception:
                        try:
                            return len(v)
                        except Exception:
                            return 0

                s_correct = random_model.df_backtest_evaluate["correct_num"].apply(_to_int)
                df_correct = random_model.df_backtest_evaluate[s_correct >= 5][["date", "result", "predicted"]]
            else:
                df_correct = pd.DataFrame()

            cost_per_day = 10000 * ticket_per_days

            return f"""## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: {ticket_per_days}
- **Daily cost**: {cost_per_day:,} VND
- **Results with 5+ matches**:

{df_correct.to_markdown(index=False) if not df_correct.empty else "No significant matches found in backtest period."}

"""
        except Exception as e:
            logger.error(f"Error generating predictions: {e}")
            return "## 🔮 Prediction Models\n\n> Error generating prediction analysis.\n"

    def _generate_power655_analysis(self, df: pl.DataFrame) -> str:
        """Generate detailed Power 6/55 analysis section."""
        if df.is_empty():
            return "## 📈 Power 6/55 Analysis\n\n> No data available for analysis.\n"

        try:
            # Calculate stats for different periods
            stats_all = self._balance_long_df(self._calculate_stats(df))

            current_date = datetime.now().date()
            stats_30d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=30))))
            )
            stats_60d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=60))))
            )
            stats_90d = self._balance_long_df(
                self._calculate_stats(df.filter(pl.col("date") >= (current_date - timedelta(days=90))))
            )

            recent_results = df.head(10)

            recent_results_pd = recent_results.to_pandas()
            stats_all_pd = stats_all.to_pandas() if not stats_all.is_empty() else pd.DataFrame()
            stats_30d_pd = stats_30d.to_pandas() if not stats_30d.is_empty() else pd.DataFrame()
            stats_60d_pd = stats_60d.to_pandas() if not stats_60d.is_empty() else pd.DataFrame()
            stats_90d_pd = stats_90d.to_pandas() if not stats_90d.is_empty() else pd.DataFrame()

            return f"""## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
{recent_results_pd.to_markdown(index=False)}

### 🎲 Number Frequency (All Time)
{stats_all_pd.to_markdown(index=False) if not stats_all_pd.empty else "No data available"}

### 📊 Frequency Analysis by Period

#### Last 30 Days
{stats_30d_pd.to_markdown(index=False) if not stats_30d_pd.empty else "No data available"}

#### Last 60 Days
{stats_60d_pd.to_markdown(index=False) if not stats_60d_pd.empty else "No data available"}

#### Last 90 Days
{stats_90d_pd.to_markdown(index=False) if not stats_90d_pd.empty else "No data available"}

"""
        except Exception as e:
            logger.exception(f"Error generating Power 6/55 analysis: {e}")
            return "## 📈 Power 6/55 Analysis\n\n> Error generating analysis.\n"

    def generate_prediction_summary(self) -> str:
        """Generate the complete prediction summary content."""
        logger.info("Starting prediction summary generation...")

        # Load Power 6/55 data (main focus)
        df_power655 = self._load_lottery_data("power_655")

        # Generate prediction and analysis sections
        predictions = self._generate_predictions_section(df_power655)
        power655_analysis = self._generate_power655_analysis(df_power655)

        # Combine all sections
        summary_content = f"""# 🔮 Vietlott Prediction Summary

> **Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
>
> This document contains machine learning predictions and analysis for Vietnamese lottery data.
> This is an experimental module for educational purposes only.

{predictions}

{power655_analysis}

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
