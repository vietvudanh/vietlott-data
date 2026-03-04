#!/usr/bin/env python
"""
Tests for LongAbsenceStrategy.
"""

import random
from datetime import date, timedelta

import pandas as pd
import pytest


def create_sample_data(seed: int = 42, n: int = 50) -> pd.DataFrame:
    """Create reproducible sample lottery data."""
    random.seed(seed)
    data = []
    start_date = date(2023, 1, 1)
    for i in range(n):
        draw_date = start_date + timedelta(days=i * 3)
        result = sorted(random.sample(range(1, 56), 6))
        data.append({"id": f"655-{i + 1:03d}", "date": draw_date, "result": result})
    return pd.DataFrame(data)


def test_long_absence_returns_correct_number_of_predictions():
    """Strategy should return exactly number_predict numbers."""
    from machine_learning.long_absence import LongAbsenceStrategy

    df = create_sample_data()
    strategy = LongAbsenceStrategy(df, top_n=10)
    target_date = df["date"].iloc[20]
    predicted = strategy.predict(target_date)
    assert len(predicted) == strategy.number_predict
    print(f"✅ Returned {len(predicted)} predictions: {predicted}")


def test_long_absence_no_duplicates():
    """Predicted numbers must all be unique."""
    from machine_learning.long_absence import LongAbsenceStrategy

    df = create_sample_data()
    strategy = LongAbsenceStrategy(df, top_n=10)
    target_date = df["date"].iloc[25]
    predicted = strategy.predict(target_date)
    assert len(predicted) == len(set(predicted))
    print(f"✅ No duplicates in predictions: {predicted}")


def test_long_absence_numbers_in_valid_range():
    """All predicted numbers must be within [min_val, max_val]."""
    from machine_learning.long_absence import LongAbsenceStrategy

    df = create_sample_data()
    strategy = LongAbsenceStrategy(df, top_n=10)
    target_date = df["date"].iloc[30]
    predicted = strategy.predict(target_date)
    assert all(strategy.min_val <= n <= strategy.max_val for n in predicted)
    print(f"✅ All numbers in valid range [{strategy.min_val}, {strategy.max_val}]: {predicted}")


def test_long_absence_predictions_are_sorted():
    """Predict should return a sorted list."""
    from machine_learning.long_absence import LongAbsenceStrategy

    df = create_sample_data()
    strategy = LongAbsenceStrategy(df, top_n=10)
    target_date = df["date"].iloc[20]
    predicted = strategy.predict(target_date)
    assert predicted == sorted(predicted)
    print(f"✅ Predictions are sorted: {predicted}")


def test_long_absence_no_lookahead_bias():
    """Strategy must not use data on or after the target date."""
    from machine_learning.long_absence import LongAbsenceStrategy

    df = create_sample_data()
    strategy = LongAbsenceStrategy(df, top_n=10)

    # Use the earliest date where there is some history
    target_date = df["date"].iloc[10]

    # Verify _days_since_last_appearance only considers data before target_date
    sorted_nums = strategy._days_since_last_appearance(target_date)

    past_data = df[df["date"] < target_date]
    seen_numbers = set(n for result in past_data["result"] for n in result)

    # Numbers not yet seen should come first (highest absence)
    never_seen = [n for n in range(strategy.min_val, strategy.max_val + 1) if n not in seen_numbers]
    top_candidates = sorted_nums[: len(never_seen)]
    assert set(top_candidates) == set(never_seen), "Never-seen numbers should be ranked first"
    print(f"✅ No look-ahead bias: never-seen numbers ranked first correctly")


def test_long_absence_integrates_with_backtest():
    """LongAbsenceStrategy should work end-to-end with the base backtest/evaluate pipeline."""
    from machine_learning.long_absence import LongAbsenceStrategy

    df = create_sample_data()
    strategy = LongAbsenceStrategy(df, time_predict=1, top_n=10)
    strategy.backtest()
    results = strategy.evaluate()

    assert "correct_time" in results
    assert "count_correct_num" in results
    print(f"✅ Backtest complete. Correct times: {results['correct_time']}")
    print(f"   Match distribution:\n{results['count_correct_num']}")


def test_long_absence_top_n_larger_than_pool():
    """If top_n > number of available numbers, strategy should still work."""
    from machine_learning.long_absence import LongAbsenceStrategy

    df = create_sample_data()
    # top_n bigger than the entire number range (1-55 = 55 numbers)
    strategy = LongAbsenceStrategy(df, top_n=100)
    target_date = df["date"].iloc[20]
    predicted = strategy.predict(target_date)
    assert len(predicted) == strategy.number_predict
    print(f"✅ Works with top_n > pool size: {predicted}")


if __name__ == "__main__":
    print("🎰 Testing LongAbsenceStrategy...\n")
    test_long_absence_returns_correct_number_of_predictions()
    test_long_absence_no_duplicates()
    test_long_absence_numbers_in_valid_range()
    test_long_absence_predictions_are_sorted()
    test_long_absence_no_lookahead_bias()
    test_long_absence_integrates_with_backtest()
    test_long_absence_top_n_larger_than_pool()
    print("\n🎉 All tests passed!")
