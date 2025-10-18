#!/usr/bin/env python
"""
Test script for enhanced error handling and look-ahead bias detection.
"""

import sys

sys.path.append("src")

import random
from datetime import date, timedelta

import polars as pl


def create_test_data():
    """Create test lottery data."""
    random.seed(42)
    data = []
    start_date = date(2022, 1, 1)

    for i in range(100):
        draw_date = start_date + timedelta(days=i * 3)
        result = sorted(random.sample(range(1, 56), 6))
        data.append({"id": f"655-{i + 1:03d}", "date": draw_date, "result": result})

    return pl.DataFrame(data)


def test_look_ahead_bias_detection():
    """Test enhanced look-ahead bias detection."""
    print("Testing Enhanced Look-ahead Bias Detection...")

    try:
        from vietlott.model.strategy.backtest import StrategyBacktester
        from vietlott.model.strategy.base import PredictModel

        valid_df = create_test_data()
        backtester = StrategyBacktester(valid_df)

        # Create a strategy with suspicious attributes
        class SuspiciousStrategy(PredictModel):
            def __init__(self, df, time_predict=1):
                super().__init__(df, time_predict)
                self.future_data = "This should trigger a warning"

            def predict(self, date):
                return list(range(1, 7))

        # Test bias detection
        strategy = SuspiciousStrategy(valid_df)
        start_date = valid_df["date"].min() + timedelta(days=30)

        has_bias, reason = backtester._check_lookback_bias(strategy, start_date)

        if has_bias:
            print(f"✅ Correctly detected bias: {reason}")
        else:
            print("❌ Failed to detect bias in suspicious strategy")

        # Create a strategy with suspicious method
        class ForecastStrategy(PredictModel):
            def __init__(self, df, time_predict=1):
                super().__init__(df, time_predict)

            def predict(self, date):
                return list(range(1, 7))

            def predict_future(self, days):
                return "This should trigger a warning"

        # Test bias detection
        strategy = ForecastStrategy(valid_df)
        has_bias, reason = backtester._check_lookback_bias(strategy, start_date)

        if has_bias:
            print(f"✅ Correctly detected bias: {reason}")
        else:
            print("❌ Failed to detect bias in forecast strategy")

    except Exception as e:
        print(f"❌ Error in look-ahead bias detection test: {e}")
        import traceback

        traceback.print_exc()


def test_error_handling():
    """Test enhanced error handling."""
    print("\nTesting Enhanced Error Handling...")

    try:
        from vietlott.model.strategy.backtest import StrategyBacktester
        from vietlott.model.strategy.base import PredictModel

        valid_df = create_test_data()
        backtester = StrategyBacktester(valid_df)

        # Create a strategy that raises different types of errors
        class ErrorStrategy(PredictModel):
            def __init__(self, df, error_type="key", time_predict=1):
                super().__init__(df, time_predict)
                self.error_type = error_type

            def predict(self, date):
                if self.error_type == "key":
                    # KeyError
                    return self.non_existent_dict["key"]
                elif self.error_type == "index":
                    # IndexError
                    return [1, 2, 3][10]
                elif self.error_type == "type":
                    # TypeError
                    return "string" + 5
                elif self.error_type == "value":
                    # ValueError
                    return int("not a number")
                elif self.error_type == "attribute":
                    # AttributeError
                    return "string".non_existent_method()
                else:
                    return list(range(1, 7))

        # Test handling of KeyError
        diagnostic = backtester._handle_prediction_error(
            date(2022, 1, 1), "ErrorStrategy", KeyError("non_existent_dict")
        )

        print(f"Diagnostic for KeyError: {diagnostic['recommendation']}")

        # Test handling of IndexError
        diagnostic = backtester._handle_prediction_error(
            date(2022, 1, 1), "ErrorStrategy", IndexError("list index out of range")
        )

        print(f"Diagnostic for IndexError: {diagnostic['recommendation']}")

        # Test handling of TypeError
        diagnostic = backtester._handle_prediction_error(
            date(2022, 1, 1), "ErrorStrategy", TypeError("can only concatenate str (not 'int') to str")
        )

        print(f"Diagnostic for TypeError: {diagnostic['recommendation']}")

        # Test handling of ValueError
        diagnostic = backtester._handle_prediction_error(
            date(2022, 1, 1), "ErrorStrategy", ValueError("invalid literal for int() with base 10: 'not a number'")
        )

        print(f"Diagnostic for ValueError: {diagnostic['recommendation']}")

        # Test handling of AttributeError
        diagnostic = backtester._handle_prediction_error(
            date(2022, 1, 1), "ErrorStrategy", AttributeError("'str' object has no attribute 'non_existent_method'")
        )

        print(f"Diagnostic for AttributeError: {diagnostic['recommendation']}")

        # Test full backtest with error-prone strategy
        result = backtester.backtest_strategy(
            ErrorStrategy,
            {"error_type": "key"},
            start_date=valid_df["date"].min() + timedelta(days=30),
            end_date=valid_df["date"].min() + timedelta(days=60),
        )

        if result.total_predictions == 0 and result.statistical_significance.get("error"):
            print(f"✅ Correctly handled strategy with errors: {result.statistical_significance.get('error_message')}")
        else:
            print("❌ Failed to properly handle strategy with errors")

    except Exception as e:
        print(f"❌ Error in error handling test: {e}")
        import traceback

        traceback.print_exc()
