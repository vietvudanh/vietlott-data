import itertools
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any, Dict, List, Optional, Tuple, Type

import numpy as np
import pandas as pd
from loguru import logger

from vietlott.model.strategy.base import PredictModel


@dataclass
class BacktestResult:
    """Container for backtest results."""

    strategy_name: str
    parameters: Dict[str, Any]
    total_cost: float
    total_revenue: float
    net_profit: float
    win_rate: float
    avg_matches: float
    best_match: int
    total_predictions: int
    matches_distribution: Dict[int, int]
    roi: float  # Return on Investment

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for easy serialization."""
        return {
            "strategy_name": self.strategy_name,
            "parameters": self.parameters,
            "total_cost": self.total_cost,
            "total_revenue": self.total_revenue,
            "net_profit": self.net_profit,
            "win_rate": self.win_rate,
            "avg_matches": self.avg_matches,
            "best_match": self.best_match,
            "total_predictions": self.total_predictions,
            "matches_distribution": self.matches_distribution,
            "roi": self.roi,
        }


class StrategyBacktester:
    """
    Comprehensive backtesting system for lottery prediction strategies.
    """

    def __init__(self, df: pd.DataFrame, ticket_price: float = 10000):
        """
        Initialize the backtester.

        Args:
            df: Historical lottery data
            ticket_price: Cost per ticket
        """
        self.df = df.copy()
        self.df["date"] = pd.to_datetime(self.df["date"]).dt.date
        self.df = self.df.sort_values("date")
        self.ticket_price = ticket_price

        # Prize structure for Power 6/55
        self.prizes = {
            6: 40_000_000_000,  # Jackpot
            5: 5_000_000_000,  # Second prize
            4: 500_000,  # Third prize
            3: 50_000,  # Fourth prize
        }

    def _calculate_revenue(self, matches_count: int) -> float:
        """Calculate revenue based on number of matches."""
        return self.prizes.get(matches_count, 0)

    def backtest_strategy(
        self,
        strategy_class: Type[PredictModel],
        strategy_params: Dict[str, Any],
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        min_history_days: int = 365,
    ) -> BacktestResult:
        """
        Backtest a single strategy configuration.

        Args:
            strategy_class: Strategy class to test
            strategy_params: Parameters for the strategy
            start_date: Start date for backtesting
            end_date: End date for backtesting
            min_history_days: Minimum days of history needed before starting predictions

        Returns:
            BacktestResult object
        """
        # Determine backtest period
        if start_date is None:
            start_date = self.df["date"].min() + timedelta(days=min_history_days)
        if end_date is None:
            end_date = self.df["date"].max()

        # Filter data for backtest period
        test_data = self.df[(self.df["date"] >= start_date) & (self.df["date"] <= end_date)]

        if test_data.empty:
            logger.warning("No data available for backtesting period")
            return self._empty_result(strategy_class.__name__, strategy_params)

        # Initialize strategy
        try:
            strategy = strategy_class(self.df, **strategy_params)
        except Exception as e:
            logger.error(f"Failed to initialize strategy {strategy_class.__name__}: {e}")
            return self._empty_result(strategy_class.__name__, strategy_params)

        # Run predictions and evaluate
        results = []

        for _, row in test_data.iterrows():
            try:
                predicted = strategy.predict(row["date"])
                actual = row["result"]

                # Calculate matches
                matches = len(set(predicted) & set(actual))
                cost = self.ticket_price * strategy.time_predict
                revenue = self._calculate_revenue(matches)

                results.append(
                    {
                        "date": row["date"],
                        "predicted": predicted,
                        "actual": actual,
                        "matches": matches,
                        "cost": cost,
                        "revenue": revenue,
                        "profit": revenue - cost,
                    }
                )

            except Exception as e:
                logger.warning(f"Prediction failed for date {row['date']}: {e}")
                continue

        if not results:
            logger.warning("No successful predictions during backtest")
            return self._empty_result(strategy_class.__name__, strategy_params)

        # Calculate statistics
        return self._calculate_backtest_stats(strategy_class.__name__, strategy_params, results)

    def _empty_result(self, strategy_name: str, parameters: Dict[str, Any]) -> BacktestResult:
        """Create empty result for failed backtests."""
        return BacktestResult(
            strategy_name=strategy_name,
            parameters=parameters,
            total_cost=0,
            total_revenue=0,
            net_profit=0,
            win_rate=0,
            avg_matches=0,
            best_match=0,
            total_predictions=0,
            matches_distribution={},
            roi=0,
        )

    def _calculate_backtest_stats(
        self, strategy_name: str, parameters: Dict[str, Any], results: List[Dict[str, Any]]
    ) -> BacktestResult:
        """Calculate comprehensive statistics from backtest results."""
        total_cost = sum(r["cost"] for r in results)
        total_revenue = sum(r["revenue"] for r in results)
        net_profit = total_revenue - total_cost

        matches_list = [r["matches"] for r in results]
        matches_distribution = {}
        for i in range(7):  # 0-6 matches
            matches_distribution[i] = matches_list.count(i)

        win_rate = sum(1 for r in results if r["matches"] >= 3) / len(results) if results else 0
        avg_matches = float(np.mean(matches_list)) if matches_list else 0.0
        best_match = max(matches_list) if matches_list else 0
        roi = (net_profit / total_cost * 100) if total_cost > 0 else 0

        return BacktestResult(
            strategy_name=strategy_name,
            parameters=parameters,
            total_cost=total_cost,
            total_revenue=total_revenue,
            net_profit=net_profit,
            win_rate=win_rate,
            avg_matches=avg_matches,
            best_match=best_match,
            total_predictions=len(results),
            matches_distribution=matches_distribution,
            roi=roi,
        )


class ParameterTuner:
    """
    Parameter tuning system for lottery prediction strategies.
    """

    def __init__(self, backtester: StrategyBacktester):
        """
        Initialize the parameter tuner.

        Args:
            backtester: StrategyBacktester instance
        """
        self.backtester = backtester

    def grid_search(
        self,
        strategy_class: Type[PredictModel],
        param_grid: Dict[str, List[Any]],
        metric: str = "roi",
        max_workers: int = 4,
        **backtest_kwargs,
    ) -> List[BacktestResult]:
        """
        Perform grid search to find optimal parameters.

        Args:
            strategy_class: Strategy class to tune
            param_grid: Dictionary of parameter names to lists of values
            metric: Metric to optimize ('roi', 'win_rate', 'avg_matches', 'net_profit')
            max_workers: Number of parallel workers
            **backtest_kwargs: Additional arguments for backtesting

        Returns:
            List of BacktestResult objects sorted by metric
        """
        # Generate all parameter combinations
        param_names = list(param_grid.keys())
        param_values = list(param_grid.values())
        param_combinations = list(itertools.product(*param_values))

        logger.info(f"Testing {len(param_combinations)} parameter combinations")

        results = []

        # Use parallel processing for faster execution
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            future_to_params = {}

            for param_combo in param_combinations:
                params = dict(zip(param_names, param_combo))
                future = executor.submit(self.backtester.backtest_strategy, strategy_class, params, **backtest_kwargs)
                future_to_params[future] = params

            for future in as_completed(future_to_params):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    params = future_to_params[future]
                    logger.error(f"Failed to backtest parameters {params}: {e}")

        # Sort by metric
        results.sort(key=lambda x: getattr(x, metric), reverse=True)

        logger.info(f"Grid search completed. Best {metric}: {getattr(results[0], metric):.4f}")

        return results

    def random_search(
        self,
        strategy_class: Type[PredictModel],
        param_distributions: Dict[str, Any],
        n_iter: int = 50,
        metric: str = "roi",
        **backtest_kwargs,
    ) -> List[BacktestResult]:
        """
        Perform random search for parameter optimization.

        Args:
            strategy_class: Strategy class to tune
            param_distributions: Dictionary of parameter distributions
            n_iter: Number of random samples
            metric: Metric to optimize
            **backtest_kwargs: Additional arguments for backtesting

        Returns:
            List of BacktestResult objects sorted by metric
        """
        results = []

        for i in range(n_iter):
            # Sample random parameters
            params = {}
            for param_name, distribution in param_distributions.items():
                if isinstance(distribution, list):
                    params[param_name] = np.random.choice(distribution)
                elif isinstance(distribution, tuple) and len(distribution) == 2:
                    # Assume uniform distribution between min and max
                    min_val, max_val = distribution
                    if isinstance(min_val, int) and isinstance(max_val, int):
                        params[param_name] = np.random.randint(min_val, max_val + 1)
                    else:
                        params[param_name] = np.random.uniform(min_val, max_val)
                elif hasattr(distribution, "rvs"):
                    # Scipy distribution object
                    params[param_name] = distribution.rvs()

            try:
                result = self.backtester.backtest_strategy(strategy_class, params, **backtest_kwargs)
                results.append(result)

                if (i + 1) % 10 == 0:
                    logger.info(f"Completed {i + 1}/{n_iter} random samples")

            except Exception as e:
                logger.error(f"Failed to backtest random parameters {params}: {e}")

        # Sort by metric
        results.sort(key=lambda x: getattr(x, metric), reverse=True)

        logger.info(f"Random search completed. Best {metric}: {getattr(results[0], metric):.4f}")

        return results


class StrategyComparator:
    """
    Compare multiple strategies and their configurations.
    """

    def __init__(self, backtester: StrategyBacktester):
        """
        Initialize the strategy comparator.

        Args:
            backtester: StrategyBacktester instance
        """
        self.backtester = backtester

    def compare_strategies(
        self, strategies_configs: List[Tuple[Type[PredictModel], Dict[str, Any]]], **backtest_kwargs
    ) -> pd.DataFrame:
        """
        Compare multiple strategies with their configurations.

        Args:
            strategies_configs: List of (strategy_class, parameters) tuples
            **backtest_kwargs: Additional arguments for backtesting

        Returns:
            DataFrame with comparison results
        """
        results = []

        for strategy_class, params in strategies_configs:
            try:
                result = self.backtester.backtest_strategy(strategy_class, params, **backtest_kwargs)
                results.append(result.to_dict())
            except Exception as e:
                logger.error(f"Failed to backtest {strategy_class.__name__}: {e}")

        df = pd.DataFrame(results)

        # Sort by ROI by default
        if not df.empty:
            df = df.sort_values("roi", ascending=False)

        return df

    def save_results(self, results_df: pd.DataFrame, filepath: str):
        """Save comparison results to file."""
        results_df.to_csv(filepath, index=False)
        logger.info(f"Results saved to {filepath}")

    def generate_report(self, results_df: pd.DataFrame) -> str:
        """Generate a text report from comparison results."""
        if results_df.empty:
            return "No results to report."

        report = "Strategy Comparison Report\n"
        report += "=" * 50 + "\n\n"

        for idx, row in results_df.iterrows():
            report += f"Strategy: {row['strategy_name']}\n"
            report += f"Parameters: {row['parameters']}\n"
            report += f"ROI: {row['roi']:.2f}%\n"
            report += f"Win Rate: {row['win_rate']:.2f}%\n"
            report += f"Avg Matches: {row['avg_matches']:.2f}\n"
            report += f"Net Profit: {row['net_profit']:,.0f} VND\n"
            report += f"Total Predictions: {row['total_predictions']}\n"
            report += "-" * 30 + "\n"

        return report
