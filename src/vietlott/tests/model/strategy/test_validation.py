#!/usr/bin/env python
"""
Test script for input validation and error handling in the backtesting system.
"""

import sys

sys.path.append("src")

import random
from datetime import date, timedelta

import pandas as pd


def create_valid_test_data():
    """Create valid test lottery data."""
    random.seed(42)
    data = []
    start_date = date(2022, 1, 1)

    for i in range(100):
        draw_date = start_date + timedelta(days=i * 3)
        result = sorted(random.sample(range(1, 56), 6))
        data.append({"id": f"655-{i + 1:03d}", "date": draw_date, "result": result})

    return pd.DataFrame(data)


def create_invalid_test_data():
    """Create invalid test lottery data (missing columns, wrong types)."""
    # Missing 'result' column
    df1 = pd.DataFrame({"id": ["655-001", "655-002"], "date": [date(2022, 1, 1), date(2022, 1, 4)]})

    # Invalid date format
    df2 = pd.DataFrame(
        {
            "id": ["655-001", "655-002"],
            "date": ["invalid", "date"],
            "result": [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]],
        }
    )

    # Invalid result format (not lists)
    df3 = pd.DataFrame(
        {
            "id": ["655-001", "655-002"],
            "date": [date(2022, 1, 1), date(2022, 1, 4)],
            "result": ["1,2,3,4,5,6", "7,8,9,10,11,12"],
        }
    )

    return df1, df2, df3


def test_dataframe_validation():
    """Test validation of input dataframes."""
    print("Testing DataFrame Validation...")

    try:
        from vietlott.model.strategy.backtest import StrategyBacktester

        # Test with valid data
        valid_df = create_valid_test_data()
        print(f"Created valid test data with {len(valid_df)} rows")

        try:
            _ = StrategyBacktester(valid_df)
            print("✅ Valid DataFrame accepted")
        except ValueError as e:
            print(f"❌ Valid DataFrame rejected: {e}")

        # Test with invalid data
        df_missing_column, df_invalid_date, df_invalid_result = create_invalid_test_data()

        try:
            _ = StrategyBacktester(df_missing_column)
            print("❌ DataFrame with missing columns was accepted")
        except ValueError as e:
            print(f"✅ Correctly rejected DataFrame with missing columns: {e}")

        try:
            _ = StrategyBacktester(df_invalid_date)
            print("❌ DataFrame with invalid dates was accepted")
        except ValueError as e:
            print(f"✅ Correctly rejected DataFrame with invalid dates: {e}")

        try:
            _ = StrategyBacktester(df_invalid_result)
            print("❌ DataFrame with invalid results was accepted")
        except ValueError as e:
            print(f"✅ Correctly rejected DataFrame with invalid results: {e}")

        # Test with empty DataFrame
        try:
            _ = StrategyBacktester(pd.DataFrame())
            print("❌ Empty DataFrame was accepted")
        except ValueError as e:
            print(f"✅ Correctly rejected empty DataFrame: {e}")

        # Test with None
        try:
            _ = StrategyBacktester(None)
            print("❌ None was accepted")
        except ValueError as e:
            print(f"✅ Correctly rejected None: {e}")

    except Exception as e:
        print(f"❌ Error in DataFrame validation test: {e}")
        import traceback

        traceback.print_exc()


def test_strategy_params_validation():
    """Test validation of strategy parameters."""
    print("\nTesting Strategy Parameters Validation...")

    try:
        from vietlott.model.strategy.backtest import StrategyBacktester
        from vietlott.model.strategy.base import PredictModel
        from vietlott.model.strategy.frequency import FrequencyStrategy

        valid_df = create_valid_test_data()
        backtester = StrategyBacktester(valid_df)

        # Test with valid parameters for FrequencyStrategy
        valid_params = {"time_predict": 1, "lookback_days": 30, "strategy_type": "hot", "selection_weight": 0.7}

        try:
            backtester._validate_strategy_params(FrequencyStrategy, valid_params)
            print("✅ Valid parameters accepted")
        except ValueError as e:
            print(f"❌ Valid parameters rejected: {e}")

        # Create a custom strategy class with required parameters
        class CustomStrategy(PredictModel):
            def __init__(self, df, required_param, time_predict=1):
                super().__init__(df, time_predict)
                self.required_param = required_param

            def predict(self, date):
                return list(range(1, 7))

        # Test with valid parameters for CustomStrategy
        valid_custom_params = {"required_param": "value", "time_predict": 1}

        try:
            backtester._validate_strategy_params(CustomStrategy, valid_custom_params)
            print("✅ Valid custom parameters accepted")
        except ValueError as e:
            print(f"❌ Valid custom parameters rejected: {e}")

        # Test with missing required parameters
        invalid_custom_params = {
            "time_predict": 1
            # Missing required_param
        }

        try:
            backtester._validate_strategy_params(CustomStrategy, invalid_custom_params)
            print("❌ Parameters with missing required values were accepted")
        except ValueError as e:
            print(f"✅ Correctly rejected parameters with missing values: {e}")

        # Test with invalid strategy class
        class NotAStrategy:
            pass

        try:
            backtester._validate_strategy_params(NotAStrategy, valid_params)
            print("❌ Invalid strategy class was accepted")
        except ValueError as e:
            print(f"✅ Correctly rejected invalid strategy class: {e}")

    except Exception as e:
        print(f"❌ Error in strategy parameters validation test: {e}")
        import traceback

        traceback.print_exc()


def test_lookback_bias_detection():
    """Test detection of potential look-ahead bias."""
    print("\nTesting Look-ahead Bias Detection...")

    try:
        from vietlott.model.strategy.backtest import StrategyBacktester
        from vietlott.model.strategy.frequency import FrequencyStrategy

        valid_df = create_valid_test_data()
        backtester = StrategyBacktester(valid_df)

        # Create a strategy with lookback_days longer than available history
        strategy = FrequencyStrategy(valid_df, lookback_days=500)  # Much longer than our test data

        # Test bias detection
        start_date = valid_df["date"].min() + timedelta(days=30)  # Only 30 days of history
        has_bias = backtester._check_lookback_bias(strategy, start_date)

        if has_bias:
            print("✅ Correctly detected potential look-ahead bias")
        else:
            print("❌ Failed to detect potential look-ahead bias")

        # Test with sufficient history
        strategy = FrequencyStrategy(valid_df, lookback_days=10)  # Short lookback
        has_bias = backtester._check_lookback_bias(strategy, start_date)

        if not has_bias:
            print("✅ Correctly found no bias with sufficient history")
        else:
            print("❌ Incorrectly detected bias with sufficient history")

    except Exception as e:
        print(f"❌ Error in look-ahead bias detection test: {e}")
        import traceback

        traceback.print_exc()


def test_date_validation():
    """Test validation of backtest date ranges."""
    print("\nTesting Date Range Validation...")

    try:
        from vietlott.model.strategy.backtest import StrategyBacktester
        from vietlott.model.strategy.random_strategy import RandomModel

        valid_df = create_valid_test_data()
        backtester = StrategyBacktester(valid_df)

        # Test with valid date range
        start_date = valid_df["date"].min() + timedelta(days=30)
        end_date = valid_df["date"].max() - timedelta(days=30)

        result = backtester.backtest_strategy(
            RandomModel, {"time_predict": 1}, start_date=start_date, end_date=end_date
        )

        if result.total_predictions > 0:
            print("✅ Valid date range accepted")
        else:
            print("❌ Valid date range rejected")

        # Test with start date after end date
        result = backtester.backtest_strategy(
            RandomModel, {"time_predict": 1}, start_date=end_date, end_date=start_date
        )

        if result.total_predictions == 0:
            print("✅ Correctly handled start date after end date")
        else:
            print("❌ Incorrectly processed start date after end date")

        # Test with insufficient history warning
        early_start = valid_df["date"].min() + timedelta(days=5)  # Only 5 days of history
        result = backtester.backtest_strategy(
            RandomModel,
            {"time_predict": 1},
            start_date=early_start,
            end_date=end_date,
            min_history_days=30,  # Require 30 days
        )

        print("✅ Handled insufficient history warning (check logs)")

    except Exception as e:
        print(f"❌ Error in date validation test: {e}")
        import traceback

        traceback.print_exc()
