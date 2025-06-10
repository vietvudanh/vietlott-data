#!/usr/bin/env python
"""
Demo script showing how to use the lottery prediction strategies,
backtesting, and parameter tuning systems.
"""

from datetime import timedelta
import pandas as pd
from loguru import logger

from vietlott.config.products import get_config
from vietlott.model.strategy import (
    RandomModel,
    NotRepeatStrategy,
    FrequencyStrategy,
    HotNumbersStrategy,
    ColdNumbersStrategy,
    PatternStrategy,
    StrategyBacktester,
    ParameterTuner,
    StrategyComparator,
)


def load_sample_data():
    """Load sample lottery data."""
    try:
        df = pd.read_json(get_config("power_655").raw_path, lines=True, dtype=object, convert_dates=False)
        df["date"] = pd.to_datetime(df["date"]).dt.date
        df = df.sort_values(by=["date", "id"], ascending=False)
        logger.info(f"Loaded {len(df)} records from {df['date'].min()} to {df['date'].max()}")
        return df
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        return None


def demo_basic_predictions():
    """Demonstrate basic strategy predictions."""
    logger.info("=== Demo: Basic Strategy Predictions ===")

    df = load_sample_data()
    if df is None:
        return

    # Get a sample date for prediction
    sample_date = df["date"].iloc[10]  # Use 10th most recent date
    logger.info(f"Making predictions for date: {sample_date}")

    # Test different strategies
    strategies = [
        ("Random", RandomModel(df, time_predict=3)),
        ("NotRepeat", NotRepeatStrategy(df, lookback_days=30, avoid_weight=0.8)),
        ("HotNumbers", HotNumbersStrategy(df, lookback_days=180)),
        ("ColdNumbers", ColdNumbersStrategy(df, lookback_days=180)),
        ("Pattern", PatternStrategy(df, lookback_days=90, pattern_weight=0.7)),
    ]

    for name, strategy in strategies:
        try:
            predictions = strategy.predict(sample_date)
            logger.info(f"{name:12}: {predictions}")
        except Exception as e:
            logger.error(f"Failed to predict with {name}: {e}")


def demo_backtesting():
    """Demonstrate strategy backtesting."""
    logger.info("\n=== Demo: Strategy Backtesting ===")

    df = load_sample_data()
    if df is None:
        return

    # Initialize backtester
    backtester = StrategyBacktester(df)

    # Define backtest period (last 6 months)
    end_date = df["date"].max()
    start_date = end_date - timedelta(days=180)

    logger.info(f"Backtesting period: {start_date} to {end_date}")

    # Test different strategies
    strategies_to_test = [
        (RandomModel, {"time_predict": 1}),
        (NotRepeatStrategy, {"lookback_days": 30, "avoid_weight": 0.7}),
        (HotNumbersStrategy, {"lookback_days": 365}),
        (ColdNumbersStrategy, {"lookback_days": 365}),
        (PatternStrategy, {"lookback_days": 180, "pattern_weight": 0.6}),
    ]

    results = []
    for strategy_class, params in strategies_to_test:
        try:
            result = backtester.backtest_strategy(strategy_class, params, start_date=start_date, end_date=end_date)
            results.append(result)
            logger.info(
                f"{result.strategy_name:15}: ROI={result.roi:6.2f}%, "
                f"WinRate={result.win_rate:5.2f}%, "
                f"AvgMatches={result.avg_matches:.2f}"
            )
        except Exception as e:
            logger.error(f"Backtesting failed for {strategy_class.__name__}: {e}")

    # Find best strategy
    if results:
        best_strategy = max(results, key=lambda x: x.roi)
        logger.info(f"\nBest strategy: {best_strategy.strategy_name} " f"(ROI: {best_strategy.roi:.2f}%)")


def demo_parameter_tuning():
    """Demonstrate parameter tuning."""
    logger.info("\n=== Demo: Parameter Tuning ===")

    df = load_sample_data()
    if df is None:
        return

    # Initialize backtester and tuner
    backtester = StrategyBacktester(df)
    tuner = ParameterTuner(backtester)

    # Define backtest period
    end_date = df["date"].max()
    start_date = end_date - timedelta(days=90)  # Shorter period for demo

    logger.info("Tuning NotRepeatStrategy parameters...")

    # Define parameter grid for NotRepeatStrategy
    param_grid = {"lookback_days": [15, 30, 60, 90], "avoid_weight": [0.5, 0.7, 0.9], "time_predict": [1, 2]}

    try:
        # Run grid search (limited for demo)
        results = tuner.grid_search(
            NotRepeatStrategy,
            param_grid,
            metric="roi",
            max_workers=2,  # Limit workers for demo
            start_date=start_date,
            end_date=end_date,
        )

        # Show top 3 results
        logger.info("Top 3 parameter combinations:")
        for i, result in enumerate(results[:3]):
            logger.info(f"{i+1}. {result.parameters} -> ROI: {result.roi:.2f}%")

    except Exception as e:
        logger.error(f"Parameter tuning failed: {e}")


def demo_strategy_comparison():
    """Demonstrate strategy comparison."""
    logger.info("\n=== Demo: Strategy Comparison ===")

    df = load_sample_data()
    if df is None:
        return

    # Initialize backtester and comparator
    backtester = StrategyBacktester(df)
    comparator = StrategyComparator(backtester)

    # Define strategies to compare with optimized parameters
    strategies_configs = [
        (RandomModel, {"time_predict": 1}),
        (NotRepeatStrategy, {"lookback_days": 30, "avoid_weight": 0.8}),
        (FrequencyStrategy, {"lookback_days": 365, "strategy_type": "hot", "selection_weight": 0.7}),
        (FrequencyStrategy, {"lookback_days": 365, "strategy_type": "cold", "selection_weight": 0.7}),
        (PatternStrategy, {"lookback_days": 180, "pattern_weight": 0.6}),
    ]

    # Define backtest period
    end_date = df["date"].max()
    start_date = end_date - timedelta(days=120)

    try:
        # Run comparison
        results_df = comparator.compare_strategies(strategies_configs, start_date=start_date, end_date=end_date)

        if not results_df.empty:
            # Display results
            logger.info("Strategy Comparison Results:")
            logger.info("=" * 80)

            for _, row in results_df.iterrows():
                strategy_name = row["strategy_name"]
                roi = row["roi"]
                win_rate = row["win_rate"] * 100
                avg_matches = row["avg_matches"]
                net_profit = row["net_profit"]

                logger.info(
                    f"{strategy_name:20}: ROI={roi:6.2f}% | "
                    f"Win Rate={win_rate:5.2f}% | "
                    f"Avg Matches={avg_matches:.2f} | "
                    f"Net Profit={net_profit:>12,.0f} VND"
                )

            # Generate and save report
            report = comparator.generate_report(results_df)
            with open("strategy_comparison_report.txt", "w") as f:
                f.write(report)
            logger.info("Detailed report saved to 'strategy_comparison_report.txt'")

        else:
            logger.warning("No comparison results generated")

    except Exception as e:
        logger.error(f"Strategy comparison failed: {e}")


def demo_advanced_strategies():
    """Demonstrate advanced strategy features."""
    logger.info("\n=== Demo: Advanced Strategy Features ===")

    df = load_sample_data()
    if df is None:
        return

    sample_date = df["date"].iloc[20]

    # Test FrequencyStrategy with different configurations
    logger.info("FrequencyStrategy variations:")

    configs = [
        ("Hot-Heavy", {"strategy_type": "hot", "selection_weight": 0.9}),
        ("Cold-Heavy", {"strategy_type": "cold", "selection_weight": 0.9}),
        ("Balanced", {"strategy_type": "balanced", "selection_weight": 0.5}),
    ]

    for name, params in configs:
        try:
            strategy = FrequencyStrategy(df, lookback_days=180, **params)
            predictions = strategy.predict(sample_date)
            logger.info(f"{name:12}: {predictions}")
        except Exception as e:
            logger.error(f"Failed with {name}: {e}")

    # Test PatternStrategy with different weights
    logger.info("\nPatternStrategy variations:")

    pattern_weights = [0.3, 0.6, 0.9]
    for weight in pattern_weights:
        try:
            strategy = PatternStrategy(df, pattern_weight=weight)
            predictions = strategy.predict(sample_date)
            logger.info(f"Weight {weight:3.1f}:    {predictions}")
        except Exception as e:
            logger.error(f"Failed with weight {weight}: {e}")


def main():
    """Run all demonstrations."""
    logger.info("🎰 Vietlott Strategy Demo Starting...")

    try:
        demo_basic_predictions()
        demo_backtesting()
        demo_parameter_tuning()
        demo_strategy_comparison()
        demo_advanced_strategies()

        logger.info("\n✅ All demos completed successfully!")

    except Exception as e:
        logger.error(f"Demo failed: {e}")
        raise


if __name__ == "__main__":
    main()
