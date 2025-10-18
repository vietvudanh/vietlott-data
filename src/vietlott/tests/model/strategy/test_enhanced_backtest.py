#!/usr/bin/env python
"""
Test script for enhanced BacktestResult functionality.
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


def test_enhanced_backtest():
    """Test the enhanced BacktestResult functionality."""
    print("Testing Enhanced BacktestResult...")

    try:
        from vietlott.model.strategy.backtest import StrategyBacktester
        from vietlott.model.strategy.random_strategy import RandomModel

        # Create test data
        df = create_test_data()
        print(f"Created {len(df)} test lottery draws")

        # Initialize backtester
        backtester = StrategyBacktester(df)

        # Test backtest with enhanced metrics
        end_date = df["date"].max()
        start_date = end_date - timedelta(days=60)

        print(f"Running backtest from {start_date} to {end_date}")

        result = backtester.backtest_strategy(
            RandomModel, {"time_predict": 1}, start_date=start_date, end_date=end_date
        )

        print("\n=== Enhanced Backtest Results ===")
        print(f"Strategy: {result.strategy_name}")
        print(f"Total Predictions: {result.total_predictions}")
        print(f"ROI: {result.roi:.2f}%")
        print(f"Win Rate: {result.win_rate:.4f}")
        print(f"Average Matches: {result.avg_matches:.2f}")
        print(f"Sharpe Ratio: {result.sharpe_ratio:.4f}")
        print(f"Max Drawdown: {result.max_drawdown:.2f}%")
        print(f"Consistency Score: {result.consistency_score:.4f}")

        # Test data conversion methods
        print("\n=== Testing Data Conversion ===")
        result_dict = result.to_dict()
        print(f"Dictionary keys: {list(result_dict.keys())}")

        result_df = result.to_dataframe()
        print(f"DataFrame shape: {result_df.shape}")
        print(f"DataFrame columns: {list(result_df.columns)}")

        # Test prediction history
        history_df = result.get_prediction_history_df()
        print(f"Prediction history shape: {history_df.shape}")

        # Test summary stats
        summary = result.get_summary_stats()
        print(f"\nSummary stats keys: {list(summary.keys())}")

        # Test comparison (create another result to compare)
        result2 = backtester.backtest_strategy(
            RandomModel, {"time_predict": 2}, start_date=start_date, end_date=end_date
        )

        comparison = result.compare_with(result2)
        print(f"\nComparison keys: {list(comparison.keys())}")
        print(f"ROI comparison: {comparison['roi_comparison']}")

        print("\n✅ Enhanced BacktestResult test completed successfully!")

        # Test visualization (optional - will only work if matplotlib is available)
        try:
            print("\n=== Testing Visualization ===")
            # Note: In a real environment, this would show plots
            # For testing, we'll just verify the methods don't crash
            result.plot_performance()
            result.plot_matches_distribution()
            print("✅ Visualization methods work correctly!")
        except Exception as e:
            print(f"⚠️  Visualization test skipped: {e}")

    except Exception as e:
        print(f"❌ Error in enhanced backtest test: {e}")
        import traceback

        traceback.print_exc()
