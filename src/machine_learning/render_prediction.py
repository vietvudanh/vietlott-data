#!/usr/bin/env python
"""
Prediction Summary Generator for Vietlott Data Project.

This script generates a prediction summary markdown file for the machine learning module.
It outputs detailed prediction reports with statistics for each strategy.
"""

from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

import polars as pl
from loguru import logger

from machine_learning.strategies import (
    ColdNumbersStrategy,
    ExponentialDecayStrategy,
    HotNumbersStrategy,
    LongAbsenceStrategy,
    NotRepeatStrategy,
    PairFrequencyStrategy,
    PatternStrategy,
    RandomModel,
)
from machine_learning.strategies.base import PredictModel
from vietlott.config.products import get_config

# (strategy_name, tickets_per_day, model_instance) after backtest+evaluate
_StrategyEntry = Tuple[str, int, PredictModel]


class PredictionSummaryGenerator:
    """Generator for prediction summary."""

    def __init__(self):
        pass

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # Strategy runner
    # ------------------------------------------------------------------

    def _build_and_run_strategies(self, df_pd) -> List[_StrategyEntry]:
        """
        Instantiate, backtest, and evaluate all strategies.

        Returns a list of ``(name, tickets_per_day, model)`` tuples where
        each model has already been backtested and evaluated.
        """
        tpd = 20  # tickets per day for all strategies

        strategy_defs = [
            ("Random Strategy", RandomModel(df_pd, tpd)),
            ("Long Absence Strategy", LongAbsenceStrategy(df_pd, time_predict=tpd, top_n=15)),
            ("Pattern Strategy", PatternStrategy(df_pd, time_predict=tpd, lookback_days=180, pattern_weight=0.6)),
            (
                "Hot Numbers Strategy",
                HotNumbersStrategy(df_pd, time_predict=tpd, lookback_days=365, selection_weight=0.7),
            ),
            (
                "Cold Numbers Strategy",
                ColdNumbersStrategy(df_pd, time_predict=tpd, lookback_days=365, selection_weight=0.7),
            ),
            ("Not Repeat Strategy", NotRepeatStrategy(df_pd, time_predict=tpd, lookback_days=30, avoid_weight=0.8)),
            (
                "Exponential Decay Strategy",
                ExponentialDecayStrategy(df_pd, time_predict=tpd, half_life_days=90, hot=True, selection_weight=0.8),
            ),
            ("Pair Frequency Strategy", PairFrequencyStrategy(df_pd, time_predict=tpd, lookback_days=365)),
        ]

        results: List[_StrategyEntry] = []
        for name, model in strategy_defs:
            logger.info(f"Running {name}...")
            model.backtest()
            model.evaluate()
            results.append((name, tpd, model))

        return results

    # ------------------------------------------------------------------
    # ROI comparison table (header)
    # ------------------------------------------------------------------

    def _roi_comparison_table(self, strategies: List[_StrategyEntry]) -> str:
        """Generate a ROI comparison table sorted best → worst."""
        rows = []
        for name, tpd, model in strategies:
            cost, gain, profit = model.revenue()
            roi = (profit / cost * 100) if cost > 0 else 0.0
            rows.append((name, cost, gain, profit, roi))

        rows.sort(key=lambda x: x[4], reverse=True)

        medals = ["🥇", "🥈", "🥉"] + ["  "] * len(rows)
        header = "| Rank | Strategy | Total Cost (VND) | Total Gain (VND) | Net Profit (VND) | ROI |"
        sep = "|------|----------|-----------------|-----------------|-----------------|-----|"
        lines = [header, sep]
        for i, (name, cost, gain, profit, roi) in enumerate(rows):
            lines.append(f"| {medals[i]} {i + 1} | {name} | {cost:,} | {gain:,} | {profit:,} | {roi:.2f}% |")

        return f"""## 📊 Strategy Performance Comparison

> Sorted by ROI (best → worst).  All strategies backtested with **{strategies[0][1]} tickets/draw**.
> Note: All ROIs are deeply negative — lottery odds make profit impossible at scale.
> The comparison shows *which strategy loses the least*, not which one is profitable.

{chr(10).join(lines)}
"""

    # ------------------------------------------------------------------
    # Per-strategy detailed report
    # ------------------------------------------------------------------

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

        total_draws = len(model.df_backtest)
        total_predictions = len(df_eval)
        cost, gain, profit = model.revenue()

        s_correct = df_eval["correct_num"].apply(self._to_int).astype(int)
        match_counts = s_correct.value_counts().sort_index(ascending=False)
        match_distribution = "\n".join(
            [f"  - **{matches} matches**: {count:,} times" for matches, count in match_counts.items()]
        )

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

    def _generate_predictions_section(self, strategies: List[_StrategyEntry]) -> str:
        """Generate per-strategy detailed reports from pre-run strategy list."""
        reports = [self._generate_strategy_report(model, name, tpd) for name, tpd, model in strategies]
        return f"""## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

{"".join(reports)}
"""

    # ------------------------------------------------------------------
    # Strategy documentation
    # ------------------------------------------------------------------

    _STRATEGY_DOCS = {
        "Random Strategy": (
            "**How it works**: Generates tickets by shuffling all numbers in the valid range "
            "and picking the first `number_predict` entries.  Every number has an equal chance "
            "of being selected; no historical data is used.\n\n"
            "**Use case**: Serves as an unbiased performance baseline.  Any strategy that "
            "cannot beat random selection over a large backtest offers no predictive value."
        ),
        "Long Absence Strategy": (
            "**How it works**: For each draw date, looks back at all past draws and records "
            "the last date each number appeared.  Numbers are ranked by how many days have "
            "elapsed since they last appeared (numbers that have *never* appeared rank highest). "
            "A configurable pool of the `top_n` most-absent numbers is assembled, and "
            "`number_predict` numbers are randomly sampled from that pool.\n\n"
            "**Key parameter**: `top_n` (default 10) – larger pool → more randomness; "
            "smaller pool → stronger bias toward the longest-absent numbers.\n\n"
            "**Use case**: Captures the intuition that numbers that have been *overdue* for "
            "a long time are somehow more likely to appear.  (Note: for a fair lottery this "
            "intuition is mathematically incorrect, but the strategy is included for "
            "empirical comparison.)"
        ),
        "Pattern Strategy": (
            "**How it works**: Analyses two structural properties of historical draws in "
            "a rolling `lookback_days` window:\n\n"
            "1. **Spacing patterns** – gaps between consecutive sorted numbers in a ticket.  "
            "The most common gaps are used to generate the next number by applying a sampled "
            "gap to the previously chosen number.\n"
            "2. **Range distribution** – the number range 1–55 is split into five equal "
            "sub-ranges.  The historical fraction of draws falling in each sub-range is used "
            "as a probability weight for choosing the first number.\n\n"
            "A `pattern_weight` fraction of the ticket is filled with pattern-derived numbers; "
            "the remainder is filled randomly.\n\n"
            "**Key parameters**: `lookback_days` (default 180), `pattern_weight` (default 0.6)."
        ),
        "Hot Numbers Strategy": (
            "**How it works**: Counts how many times each number appeared over the last "
            "`lookback_days` days.  Numbers are sorted from most-frequent to least-frequent.  "
            "A weighted pool is built where each number is repeated proportionally to its "
            "frequency, then numbers are drawn without replacement from that pool.\n\n"
            "A `selection_weight` fraction of the ticket is filled from the frequency-weighted "
            "pool; the rest is filled uniformly at random.\n\n"
            "**Key parameters**: `lookback_days` (default 365), `selection_weight` (default 0.7).\n\n"
            "**Use case**: Tests whether recently hot numbers continue to appear at above-average rates."
        ),
        "Cold Numbers Strategy": (
            "**How it works**: Identical to Hot Numbers Strategy but ranks numbers in the "
            "*reverse* order (least frequent first).  The weighted pool gives higher weight "
            "to numbers that have appeared fewer times in the lookback window.\n\n"
            "**Key parameters**: `lookback_days` (default 365), `selection_weight` (default 0.7).\n\n"
            "**Use case**: Tests the complementary hypothesis that rarely-drawn numbers are "
            "more likely to appear (mean-reversion / gambler's fallacy)."
        ),
        "Not Repeat Strategy": (
            "**How it works**: Collects all numbers that appeared in *any* draw within the "
            "last `lookback_days` days.  Whenever enough *non-recent* numbers exist to fill "
            "a full ticket they are sampled uniformly.  When the pool of non-recent numbers "
            "is too small, remaining slots are filled using an `avoid_weight` probability to "
            "decide whether to pick from recent numbers or from the full range.\n\n"
            "**Key parameters**: `lookback_days` (default 30), `avoid_weight` (default 0.8).\n\n"
            "**Use case**: Models the idea that numbers drawn recently are *less* likely to "
            "repeat in the very next draw."
        ),
        "Exponential Decay Strategy": (
            "**How it works**: Every historical draw contributes a score to each number it "
            "contained, but the contribution decays exponentially with age: "
            "``weight = exp(-ln(2) × days_ago / half_life_days)``.  Draws from yesterday "
            "contribute much more than draws from a year ago.  Numbers are then selected "
            "from a pool weighted by their accumulated scores.\n\n"
            "Unlike Hot/Cold Numbers Strategy there is **no hard window cutoff** — all "
            "history is used, with very old draws contributing negligibly.  The smooth "
            "decay avoids abrupt weight changes when a draw ages past a window boundary.\n\n"
            "**Key parameters**: `half_life_days` (default 90), `hot` (default True), "
            "`selection_weight` (default 0.8)."
        ),
        "Pair Frequency Strategy": (
            "**How it works**: Builds a co-occurrence matrix from historical draws: "
            "``cooccurrence[a][b]`` counts draws where numbers ``a`` and ``b`` both "
            "appeared.  Tickets are assembled iteratively:\n\n"
            "1. The first number is sampled proportional to individual draw frequency.\n"
            "2. Each subsequent number is sampled proportional to its **average "
            "co-occurrence score** with the numbers already selected.\n\n"
            "This produces clusters of numbers that historically appear together, "
            "exploiting second-order correlations that all single-number strategies ignore.\n\n"
            "**Key parameter**: `lookback_days` (default 365)."
        ),
    }

    def _strategy_docs_section(self) -> str:
        """Return a markdown section documenting every strategy."""
        lines = ["## 📚 Strategy Descriptions\n"]
        for name, description in self._STRATEGY_DOCS.items():
            lines.append(f"### {name}\n\n{description}\n")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Summary assembly
    # ------------------------------------------------------------------

    def generate_prediction_summary(self) -> str:
        """Generate the complete prediction summary content."""
        logger.info("Starting prediction summary generation...")

        df_power655 = self._load_lottery_data("power_655")
        if df_power655.is_empty():
            return "# Error\n\nNo data available.\n"

        df_pd = df_power655.to_pandas()
        strategies = self._build_and_run_strategies(df_pd)

        roi_table = self._roi_comparison_table(strategies)
        strategy_docs = self._strategy_docs_section()
        predictions = self._generate_predictions_section(strategies)

        return f"""# 🔮 Vietlott Power 655 Prediction Summary

> **Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
>
> This document contains machine learning predictions for Vietnamese lottery data.
> This is an experimental module for educational purposes only.

{roi_table}

{strategy_docs}

{predictions}

---

## ⚠️ Disclaimer

This prediction summary is for educational and research purposes only. Lottery outcomes are random and cannot be reliably predicted. Never gamble more than you can afford to lose.
"""

    def save_prediction_summary(self, output_path: Optional[Path] = None) -> None:
        """Generate and save prediction summary to file."""
        if output_path is None:
            output_path = Path(__file__).parent / "readme.md"

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
