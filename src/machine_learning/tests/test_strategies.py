"""
Tests for ML prediction strategies.

Covers:
- All strategies return exactly `number_predict` distinct numbers within [min_val, max_val]
- RandomModel correctly samples from the full range including max_val
- MarkovChainStrategy handles date_from / date_to backtest filtering
- backtest + evaluate pipeline produces expected DataFrame columns
"""

import random
from datetime import date, timedelta

import pandas as pd
import pytest

from machine_learning.strategies import (
    ColdNumbersStrategy,
    ExponentialDecayStrategy,
    HotNumbersStrategy,
    LongAbsenceStrategy,
    MarkovChainStrategy,
    NotRepeatStrategy,
    PairFrequencyStrategy,
    PatternStrategy,
    RandomModel,
)
from machine_learning.strategies.base import PredictModel

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

MIN_VAL = 1
MAX_VAL = 55
N_DRAWS = 40


def _make_df(n: int = N_DRAWS, seed: int = 42) -> pd.DataFrame:
    """Create a synthetic lottery DataFrame with `n` draws."""
    rng = random.Random(seed)
    start = date(2023, 1, 1)
    rows = []
    for i in range(n):
        draw_date = start + timedelta(days=i * 3)
        result = sorted(rng.sample(range(MIN_VAL, MAX_VAL + 1), 6))
        rows.append({"date": draw_date, "result": result, "id": i + 1})
    return pd.DataFrame(rows)


@pytest.fixture
def df():
    return _make_df()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _assert_valid_prediction(pred, model: PredictModel):
    """Assert that a prediction is a sorted list of valid distinct numbers."""
    assert isinstance(pred, list), "predict() must return a list"
    assert len(pred) == model.number_predict, (
        f"Expected {model.number_predict} numbers, got {len(pred)}"
    )
    assert len(set(pred)) == model.number_predict, "Predicted numbers must be distinct"
    assert all(model.min_val <= n <= model.max_val for n in pred), (
        f"All numbers must be in [{model.min_val}, {model.max_val}]"
    )
    assert pred == sorted(pred), "Predicted numbers must be sorted"


# ---------------------------------------------------------------------------
# RandomModel: correctness and full-range coverage
# ---------------------------------------------------------------------------

class TestRandomModel:
    def test_predict_returns_valid_numbers(self, df):
        model = RandomModel(df, time_predict=1)
        pred = model.predict(date(2023, 6, 1))
        _assert_valid_prediction(pred, model)

    def test_predict_includes_max_val(self, df):
        """max_val (55) must be reachable — regression for off-by-one bug."""
        model = RandomModel(df, time_predict=1)
        # 150 iterations: P(55 not seen) = (54/55)^(6*150) ≈ 5e-8
        all_nums = set()
        for _ in range(150):
            all_nums.update(model.predict(date(2023, 6, 1)))
        assert MAX_VAL in all_nums, (
            f"max_val ({MAX_VAL}) was never predicted — "
            f"off-by-one bug in range() call"
        )

    def test_predict_includes_min_val(self, df):
        """min_val (1) must be reachable."""
        model = RandomModel(df, time_predict=1)
        all_nums = set()
        for _ in range(150):
            all_nums.update(model.predict(date(2023, 6, 1)))
        assert MIN_VAL in all_nums

    def test_backtest_evaluate_pipeline(self, df):
        model = RandomModel(df, time_predict=2)
        model.backtest()
        result = model.evaluate()
        assert "correct_time" in result
        assert "count_correct_num" in result
        assert model.df_backtest_evaluate is not None
        assert not model.df_backtest_evaluate.empty

    def test_revenue_returns_three_values(self, df):
        model = RandomModel(df, time_predict=1)
        model.backtest()
        model.evaluate()
        cost, gain, profit = model.revenue()
        assert cost > 0
        assert gain >= 0
        assert profit == gain - cost


# ---------------------------------------------------------------------------
# MarkovChainStrategy
# ---------------------------------------------------------------------------

class TestMarkovChainStrategy:
    def test_predict_valid(self, df):
        model = MarkovChainStrategy(df, time_predict=1, lookback_days=365)
        pred = model.predict(df["date"].iloc[-1] + timedelta(days=3))
        _assert_valid_prediction(pred, model)

    def test_predict_fallback_no_history(self, df):
        """With no prior history, falls back to uniform random."""
        model = MarkovChainStrategy(df, time_predict=1, lookback_days=365)
        very_early = df["date"].min() - timedelta(days=1)
        pred = model.predict(very_early)
        _assert_valid_prediction(pred, model)

    def test_backtest_date_from_filters_rows(self, df):
        """date_from filters evaluated rows but leaves self.df unchanged."""
        model = MarkovChainStrategy(df, time_predict=1)
        split_date = df["date"].quantile(0.5)
        if hasattr(split_date, "date"):
            split_date = split_date.date()

        model.backtest(date_from=split_date)
        model.evaluate()

        assert model.df_backtest["date"].min() >= split_date
        # Full data still accessible on the model
        assert len(model.df) == len(df)

    def test_backtest_date_to_filters_rows(self, df):
        """date_to filters evaluated rows."""
        model = MarkovChainStrategy(df, time_predict=1)
        split_date = df["date"].quantile(0.5)
        if hasattr(split_date, "date"):
            split_date = split_date.date()

        model.backtest(date_to=split_date)
        model.evaluate()

        assert model.df_backtest["date"].max() <= split_date

    def test_backtest_date_range(self, df):
        """Both date_from and date_to together narrow the evaluated window."""
        model = MarkovChainStrategy(df, time_predict=1)
        all_dates = sorted(df["date"].unique())
        d_from = all_dates[len(all_dates) // 4]
        d_to = all_dates[3 * len(all_dates) // 4]

        model.backtest(date_from=d_from, date_to=d_to)
        model.evaluate()

        assert model.df_backtest["date"].min() >= d_from
        assert model.df_backtest["date"].max() <= d_to

    def test_caching_consistent(self, df):
        """Multiple predict() calls for the same date return same-length result."""
        model = MarkovChainStrategy(df, time_predict=1)
        target = df["date"].iloc[-1] + timedelta(days=3)
        results = [model.predict(target) for _ in range(10)]
        # All predictions must have the right length and be valid
        for r in results:
            _assert_valid_prediction(r, model)


# ---------------------------------------------------------------------------
# All strategies: parametric correctness check
# ---------------------------------------------------------------------------

STRATEGY_FACTORIES = [
    lambda df: RandomModel(df, time_predict=1),
    lambda df: LongAbsenceStrategy(df, time_predict=1, top_n=10),
    lambda df: PatternStrategy(df, time_predict=1, lookback_days=90, pattern_weight=0.6),
    lambda df: HotNumbersStrategy(df, time_predict=1, lookback_days=90),
    lambda df: ColdNumbersStrategy(df, time_predict=1, lookback_days=90),
    lambda df: NotRepeatStrategy(df, time_predict=1, lookback_days=14),
    lambda df: ExponentialDecayStrategy(df, time_predict=1, half_life_days=30),
    lambda df: PairFrequencyStrategy(df, time_predict=1, lookback_days=90),
    lambda df: MarkovChainStrategy(df, time_predict=1, lookback_days=90),
]

STRATEGY_NAMES = [
    "RandomModel",
    "LongAbsenceStrategy",
    "PatternStrategy",
    "HotNumbersStrategy",
    "ColdNumbersStrategy",
    "NotRepeatStrategy",
    "ExponentialDecayStrategy",
    "PairFrequencyStrategy",
    "MarkovChainStrategy",
]


@pytest.mark.parametrize("factory,name", zip(STRATEGY_FACTORIES, STRATEGY_NAMES))
def test_all_strategies_predict_valid(factory, name, df):
    """Every strategy must return a valid ticket for an unseen future date."""
    model = factory(df)
    future_date = df["date"].max() + timedelta(days=3)
    pred = model.predict(future_date)
    _assert_valid_prediction(pred, model)


@pytest.mark.parametrize("factory,name", zip(STRATEGY_FACTORIES, STRATEGY_NAMES))
def test_all_strategies_backtest_pipeline(factory, name, df):
    """Every strategy must complete backtest + evaluate + revenue without error."""
    model = factory(df)
    model.backtest()
    result = model.evaluate()
    cost, gain, profit = model.revenue()

    assert cost > 0, f"{name}: cost should be positive"
    assert gain >= 0, f"{name}: gain cannot be negative"
    assert profit == gain - cost, f"{name}: profit must equal gain - cost"
    assert model.df_backtest_evaluate is not None
    assert not model.df_backtest_evaluate.empty


# ---------------------------------------------------------------------------
# PredictModel.backtest: date filtering works for base class
# ---------------------------------------------------------------------------

class TestBacktestDateFilter:
    def test_no_filter_uses_all_rows(self, df):
        model = RandomModel(df, time_predict=1)
        model.backtest()
        assert len(model.df_backtest) == len(df)

    def test_date_from_reduces_rows(self, df):
        model = RandomModel(df, time_predict=1)
        cutoff = df["date"].iloc[len(df) // 2]
        model.backtest(date_from=cutoff)
        assert len(model.df_backtest) < len(df)
        assert all(d >= cutoff for d in model.df_backtest["date"])

    def test_date_to_reduces_rows(self, df):
        model = RandomModel(df, time_predict=1)
        cutoff = df["date"].iloc[len(df) // 2]
        model.backtest(date_to=cutoff)
        assert len(model.df_backtest) < len(df)
        assert all(d <= cutoff for d in model.df_backtest["date"])
