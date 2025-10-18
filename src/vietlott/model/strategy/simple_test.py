#!/usr/bin/env python
"""
Simple test script to verify the strategy implementations work.
"""

import sys

sys.path.append("src")

from datetime import date, timedelta

import polars as pl


def create_sample_data():
    """Create sample lottery data for testing."""
    import random

    # Generate 100 sample lottery draws
    data = []
    start_date = date(2023, 1, 1)

    for i in range(100):
        draw_date = start_date + timedelta(days=i * 3)  # Draw every 3 days

        # Generate 6 random numbers between 1-55
        result = sorted(random.sample(range(1, 56), 6))

        data.append({"id": f"655-{i + 1:03d}", "date": draw_date, "result": result})

    return pl.DataFrame(data)


def test_basic_strategies():
    """Test basic strategy functionality."""
    print("Creating sample data...")
    df = create_sample_data()
    print(f"Created {len(df)} sample lottery draws")

    # Test date for prediction
    test_date = df["date"].iloc[-10]  # 10th most recent
    print(f"Testing predictions for date: {test_date}")

    try:
        # Test RandomModel
        from vietlott.model.strategy.random_strategy import RandomModel

        random_strategy = RandomModel(df, time_predict=1)
        random_pred = random_strategy.predict(test_date)
        print(f"Random Strategy: {random_pred}")

        # Test NotRepeatStrategy
        from vietlott.model.strategy.not_repeat import NotRepeatStrategy

        not_repeat_strategy = NotRepeatStrategy(df, lookback_days=30)
        not_repeat_pred = not_repeat_strategy.predict(test_date)
        print(f"NotRepeat Strategy: {not_repeat_pred}")

        # Test FrequencyStrategy
        from vietlott.model.strategy.frequency import ColdNumbersStrategy, HotNumbersStrategy

        hot_strategy = HotNumbersStrategy(df, lookback_days=90)
        hot_pred = hot_strategy.predict(test_date)
        print(f"Hot Numbers Strategy: {hot_pred}")

        cold_strategy = ColdNumbersStrategy(df, lookback_days=90)
        cold_pred = cold_strategy.predict(test_date)
        print(f"Cold Numbers Strategy: {cold_pred}")

        # Test PatternStrategy
        from vietlott.model.strategy.pattern import PatternStrategy

        pattern_strategy = PatternStrategy(df, lookback_days=60)
        pattern_pred = pattern_strategy.predict(test_date)
        print(f"Pattern Strategy: {pattern_pred}")

        print("\n✅ All strategies tested successfully!")

    except Exception as e:
        print(f"❌ Error testing strategies: {e}")
        import traceback

        traceback.print_exc()


def test_backtesting():
    """Test backtesting functionality."""
    print("\n=== Testing Backtesting ===")

    df = create_sample_data()

    try:
        from vietlott.model.strategy.backtest import StrategyBacktester
        from vietlott.model.strategy.random_strategy import RandomModel

        backtester = StrategyBacktester(df)

        # Test on last 30 days
        end_date = df["date"].max()
        start_date = end_date - timedelta(days=30)

        result = backtester.backtest_strategy(
            RandomModel, {"time_predict": 1}, start_date=start_date, end_date=end_date
        )

        print("Backtest Results:")
        print(f"  Strategy: {result.strategy_name}")
        print(f"  ROI: {result.roi:.2f}%")
        print(f"  Win Rate: {result.win_rate:.2f}")
        print(f"  Avg Matches: {result.avg_matches:.2f}")
        print(f"  Total Predictions: {result.total_predictions}")
        print(f"  Net Profit: {result.net_profit:,.0f} VND")

        print("✅ Backtesting tested successfully!")

    except Exception as e:
        print(f"❌ Error testing backtesting: {e}")
        import traceback

        traceback.print_exc()


def main():
    """Run all tests."""
    print("🎰 Testing Vietlott Strategy Module...")

    test_basic_strategies()
    test_backtesting()

    print("\n🎉 All tests completed!")


if __name__ == "__main__":
    main()
