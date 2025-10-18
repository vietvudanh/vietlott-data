import itertools
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import Any, Callable, Dict, List, Optional, Tuple, Type

import numpy as np
import polars as pl
from loguru import logger

# Optional matplotlib import for visualization
try:
    import matplotlib.pyplot as plt

    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    logger.warning("Matplotlib not available. Visualization features will be disabled.")

from vietlott.model.strategy.base import PredictModel


@dataclass
class BacktestResult:
    """Container for backtest results with enhanced metrics and visualization capabilities."""

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

    # Enhanced metrics
    sharpe_ratio: float = 0.0
    max_drawdown: float = 0.0
    consistency_score: float = 0.0
    statistical_significance: Dict[str, Any] = field(default_factory=dict)
    prediction_history: List[Dict[str, Any]] = field(default_factory=list)
    profit_series: List[float] = field(default_factory=list)
    drawdown_series: List[float] = field(default_factory=list)

    # Performance tracking
    execution_time: float = 0.0
    memory_usage: float = 0.0

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
            "sharpe_ratio": self.sharpe_ratio,
            "max_drawdown": self.max_drawdown,
            "consistency_score": self.consistency_score,
            "statistical_significance": self.statistical_significance,
            "execution_time": self.execution_time,
            "memory_usage": self.memory_usage,
        }

    def to_dataframe(self) -> pl.DataFrame:
        """Convert result to DataFrame for analysis."""
        # Create main metrics dataframe
        main_data = {k: [v] for k, v in self.to_dict().items() if not isinstance(v, (dict, list))}
        df = pl.DataFrame(main_data)

        # Add matches distribution as separate columns
        for matches, count in self.matches_distribution.items():
            df = df.with_columns(
                [
                    pl.lit(count).alias(f"matches_{matches}_count"),
                    pl.lit(count / self.total_predictions if self.total_predictions > 0 else 0).alias(
                        f"matches_{matches}_rate"
                    ),
                ]
            )

        return df

    def get_prediction_history_df(self) -> pl.DataFrame:
        """Get prediction history as DataFrame."""
        if not self.prediction_history:
            return pl.DataFrame()

        return pl.DataFrame(self.prediction_history)

    def plot_performance(self, metric: str = "profit", figsize: Tuple[int, int] = (12, 6)) -> None:
        """Generate performance visualization."""
        if not HAS_MATPLOTLIB:
            logger.warning(
                "Matplotlib not available. Cannot generate plots. Install matplotlib to enable visualization."
            )
            return

        if not self.prediction_history:
            logger.warning("No prediction history available for plotting")
            return

        fig, axes = plt.subplots(2, 2, figsize=figsize)
        fig.suptitle(f"Performance Analysis: {self.strategy_name}", fontsize=16)

        # Plot 1: Cumulative profit over time
        if self.profit_series:
            cumulative_profit = np.cumsum(self.profit_series)
            axes[0, 0].plot(cumulative_profit, linewidth=2)
            axes[0, 0].set_title("Cumulative Profit Over Time")
            axes[0, 0].set_xlabel("Prediction Number")
            axes[0, 0].set_ylabel("Cumulative Profit (VND)")
            axes[0, 0].grid(True, alpha=0.3)

        # Plot 2: Drawdown series
        if self.drawdown_series:
            axes[0, 1].fill_between(range(len(self.drawdown_series)), self.drawdown_series, 0, alpha=0.7, color="red")
            axes[0, 1].set_title("Drawdown Over Time")
            axes[0, 1].set_xlabel("Prediction Number")
            axes[0, 1].set_ylabel("Drawdown (%)")
            axes[0, 1].grid(True, alpha=0.3)

        # Plot 3: Matches distribution
        matches = list(self.matches_distribution.keys())
        counts = list(self.matches_distribution.values())
        axes[1, 0].bar(matches, counts, alpha=0.7)
        axes[1, 0].set_title("Distribution of Matches")
        axes[1, 0].set_xlabel("Number of Matches")
        axes[1, 0].set_ylabel("Frequency")
        axes[1, 0].grid(True, alpha=0.3)

        # Plot 4: Key metrics summary
        metrics_data = {
            "ROI (%)": self.roi,
            "Win Rate (%)": self.win_rate * 100,
            "Sharpe Ratio": self.sharpe_ratio,
            "Max Drawdown (%)": self.max_drawdown,
            "Consistency": self.consistency_score,
        }

        metric_names = list(metrics_data.keys())
        metric_values = list(metrics_data.values())

        bars = axes[1, 1].bar(range(len(metric_names)), metric_values, alpha=0.7)
        axes[1, 1].set_title("Key Performance Metrics")
        axes[1, 1].set_xticks(range(len(metric_names)))
        axes[1, 1].set_xticklabels(metric_names, rotation=45, ha="right")
        axes[1, 1].grid(True, alpha=0.3)

        # Color bars based on performance
        for i, (bar, value) in enumerate(zip(bars, metric_values)):
            if i == 0:  # ROI
                bar.set_color("green" if value > 0 else "red")
            elif i == 1:  # Win Rate
                bar.set_color("green" if value > 5 else "orange" if value > 1 else "red")
            else:
                bar.set_color("blue")

        plt.tight_layout()
        plt.show()

    def plot_matches_distribution(self, figsize: Tuple[int, int] = (10, 6)) -> None:
        """Visualize distribution of matches with detailed analysis."""
        if not HAS_MATPLOTLIB:
            logger.warning(
                "Matplotlib not available. Cannot generate plots. Install matplotlib to enable visualization."
            )
            return

        if not self.matches_distribution:
            logger.warning("No matches distribution data available")
            return

        fig, axes = plt.subplots(1, 2, figsize=figsize)
        fig.suptitle(f"Matches Analysis: {self.strategy_name}", fontsize=14)

        matches = list(self.matches_distribution.keys())
        counts = list(self.matches_distribution.values())
        rates = [count / self.total_predictions * 100 for count in counts]

        # Plot 1: Absolute counts
        bars1 = axes[0].bar(matches, counts, alpha=0.7, color="skyblue")
        axes[0].set_title("Absolute Frequency of Matches")
        axes[0].set_xlabel("Number of Matches")
        axes[0].set_ylabel("Frequency")
        axes[0].grid(True, alpha=0.3)

        # Add value labels on bars
        for bar, count in zip(bars1, counts):
            height = bar.get_height()
            axes[0].text(bar.get_x() + bar.get_width() / 2.0, height + 0.1, f"{count}", ha="center", va="bottom")

        # Plot 2: Percentage rates
        bars2 = axes[1].bar(matches, rates, alpha=0.7, color="lightcoral")
        axes[1].set_title("Percentage Rate of Matches")
        axes[1].set_xlabel("Number of Matches")
        axes[1].set_ylabel("Rate (%)")
        axes[1].grid(True, alpha=0.3)

        # Add value labels on bars
        for bar, rate in zip(bars2, rates):
            height = bar.get_height()
            axes[1].text(bar.get_x() + bar.get_width() / 2.0, height + 0.1, f"{rate:.1f}%", ha="center", va="bottom")

        # Highlight winning matches (3+ matches)
        for i, (match_count, bar1, bar2) in enumerate(zip(matches, bars1, bars2)):
            if match_count >= 3:
                bar1.set_color("gold")
                bar2.set_color("gold")

        plt.tight_layout()
        plt.show()

    def get_summary_stats(self) -> Dict[str, Any]:
        """Get comprehensive summary statistics."""
        return {
            "strategy_name": self.strategy_name,
            "total_predictions": self.total_predictions,
            "financial_metrics": {
                "total_cost": self.total_cost,
                "total_revenue": self.total_revenue,
                "net_profit": self.net_profit,
                "roi_percent": self.roi,
            },
            "performance_metrics": {
                "win_rate_percent": self.win_rate * 100,
                "avg_matches": self.avg_matches,
                "best_match": self.best_match,
                "sharpe_ratio": self.sharpe_ratio,
                "max_drawdown_percent": self.max_drawdown,
                "consistency_score": self.consistency_score,
            },
            "matches_analysis": {
                "distribution": self.matches_distribution,
                "winning_predictions": sum(
                    count for matches, count in self.matches_distribution.items() if matches >= 3
                ),
                "winning_rate": sum(count for matches, count in self.matches_distribution.items() if matches >= 3)
                / self.total_predictions
                * 100
                if self.total_predictions > 0
                else 0,
            },
            "execution_info": {
                "execution_time_seconds": self.execution_time,
                "memory_usage_mb": self.memory_usage,
            },
        }

    def compare_with(self, other: "BacktestResult") -> Dict[str, Any]:
        """Compare this result with another BacktestResult."""
        comparison = {
            "strategies": {
                "this": self.strategy_name,
                "other": other.strategy_name,
            },
            "roi_comparison": {
                "this": self.roi,
                "other": other.roi,
                "difference": self.roi - other.roi,
                "better": "this" if self.roi > other.roi else "other" if self.roi < other.roi else "tie",
            },
            "win_rate_comparison": {
                "this": self.win_rate,
                "other": other.win_rate,
                "difference": self.win_rate - other.win_rate,
                "better": "this"
                if self.win_rate > other.win_rate
                else "other"
                if self.win_rate < other.win_rate
                else "tie",
            },
            "sharpe_ratio_comparison": {
                "this": self.sharpe_ratio,
                "other": other.sharpe_ratio,
                "difference": self.sharpe_ratio - other.sharpe_ratio,
                "better": "this"
                if self.sharpe_ratio > other.sharpe_ratio
                else "other"
                if self.sharpe_ratio < other.sharpe_ratio
                else "tie",
            },
            "consistency_comparison": {
                "this": self.consistency_score,
                "other": other.consistency_score,
                "difference": self.consistency_score - other.consistency_score,
                "better": "this"
                if self.consistency_score > other.consistency_score
                else "other"
                if self.consistency_score < other.consistency_score
                else "tie",
            },
        }

        return comparison


class StrategyBacktester:
    """
    Comprehensive backtesting system for lottery prediction strategies.
    """

    def __init__(self, df: pl.DataFrame, ticket_price: float = 10000, min_history_days: int = 365):
        """
        Initialize the backtester.

        Args:
            df: Historical lottery data
            ticket_price: Cost per ticket
            min_history_days: Minimum days of history needed before starting predictions
        """
        # Validate input dataframe
        self._validate_dataframe(df)

        self.df = df.clone()
        # Convert date column to date type if it's not already
        if self.df["date"].dtype != pl.Date:
            self.df = self.df.with_columns(pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date"))
        self.df = self.df.sort("date")
        self.ticket_price = ticket_price
        self.min_history_days = min_history_days

        # Prize structure for Power 6/55
        self.prizes = {
            6: 40_000_000_000,  # Jackpot
            5: 5_000_000_000,  # Second prize
            4: 500_000,  # Third prize
            3: 50_000,  # Fourth prize
        }

    def _validate_dataframe(self, df: pl.DataFrame) -> None:
        """
        Validate the input dataframe structure.

        Args:
            df: DataFrame to validate

        Raises:
            ValueError: If the dataframe doesn't have the required structure
        """
        if df is None or df.is_empty():
            raise ValueError("Input dataframe cannot be None or empty")

        required_columns = ["date", "result"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"Input dataframe is missing required columns: {missing_columns}")

        # Check that result column contains lists of numbers
        result_col = df["result"]
        if result_col.dtype != pl.List:
            raise ValueError("The 'result' column must contain lists of numbers")

        # Check date column can be converted to datetime
        try:
            if df["date"].dtype not in [pl.Date, pl.Datetime]:
                pl.col("date").str.strptime(pl.Date, "%Y-%m-%d")
        except Exception as e:
            raise ValueError(f"The 'date' column must contain valid dates: {e}")

    def _validate_strategy_params(self, strategy_class: Type[PredictModel], params: Dict[str, Any]) -> None:
        """
        Validate strategy parameters.

        Args:
            strategy_class: Strategy class to validate parameters for
            params: Parameters to validate

        Raises:
            ValueError: If the parameters are invalid
        """
        if not issubclass(strategy_class, PredictModel):
            raise ValueError(f"Strategy class must be a subclass of PredictModel, got {strategy_class.__name__}")

        # Check for required parameters by inspecting the __init__ signature
        import inspect

        # Get all parameters from the class hierarchy
        required_params = set()
        current_class = strategy_class

        while current_class is not object:
            if hasattr(current_class, "__init__"):
                try:
                    sig = inspect.signature(current_class.__init__)
                    for name, param in sig.parameters.items():
                        if param.default == inspect.Parameter.empty and name not in ["self", "df"]:
                            required_params.add(name)
                except (ValueError, TypeError):
                    pass
            current_class = current_class.__base__

        missing_params = required_params - set(params.keys())
        if missing_params:
            error_msg = f"Missing required parameters for {strategy_class.__name__}: {missing_params}"
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Check specific parameter types and values if defined by the strategy
        if hasattr(strategy_class, "validate_params"):
            strategy_class.validate_params(params)

    def _calculate_revenue(self, matches_count: int) -> float:
        """Calculate revenue based on number of matches."""
        return self.prizes.get(matches_count, 0)

    def _calculate_sharpe_ratio(self, profit_series: List[float]) -> float:
        """
        Calculate Sharpe ratio equivalent for lottery strategy.

        Args:
            profit_series: List of profit/loss values for each prediction

        Returns:
            Sharpe ratio (risk-adjusted return metric)
        """
        if not profit_series or len(profit_series) < 2:
            return 0.0

        profits = np.array(profit_series)
        mean_profit = np.mean(profits)
        std_profit = np.std(profits, ddof=1)

        if std_profit == 0:
            return 0.0

        # Return annualized Sharpe ratio (assuming weekly draws)
        return (mean_profit / std_profit) * np.sqrt(52)

    def _calculate_drawdown(self, profit_series: List[float]) -> Tuple[float, List[float]]:
        """
        Calculate maximum drawdown and drawdown series.

        Args:
            profit_series: List of profit/loss values for each prediction

        Returns:
            Tuple of (max_drawdown_percentage, drawdown_series)
        """
        if not profit_series:
            return 0.0, []

        cumulative_profits = np.cumsum(profit_series)
        running_max = np.maximum.accumulate(cumulative_profits)
        drawdown = cumulative_profits - running_max

        # Convert to percentage drawdown
        drawdown_pct = []
        for i, dd in enumerate(drawdown):
            if running_max[i] != 0:
                drawdown_pct.append((dd / abs(running_max[i])) * 100)
            else:
                drawdown_pct.append(0.0)

        max_drawdown = abs(min(drawdown_pct)) if drawdown_pct else 0.0

        return max_drawdown, drawdown_pct

    def _calculate_consistency(self, results: List[Dict[str, Any]]) -> float:
        """
        Calculate consistency score based on prediction performance.

        Args:
            results: List of prediction results

        Returns:
            Consistency score (0-1, higher is better)
        """
        if not results:
            return 0.0

        # Calculate consistency based on matches variance and win rate stability
        matches_list = [r["matches"] for r in results]

        if len(matches_list) < 2:
            return 0.0

        # Measure consistency as inverse of coefficient of variation
        mean_matches = np.mean(matches_list)
        std_matches = np.std(matches_list, ddof=1)

        if mean_matches == 0:
            return 0.0

        cv = std_matches / mean_matches

        # Convert to 0-1 score (lower CV = higher consistency)
        consistency = 1 / (1 + cv)

        # Adjust for win rate - strategies with higher win rates get bonus
        win_rate = sum(1 for r in results if r["matches"] >= 3) / len(results)
        consistency_adjusted = consistency * (1 + win_rate)

        return min(consistency_adjusted, 1.0)

    def backtest_strategy(
        self,
        strategy_class: Type[PredictModel],
        strategy_params: Dict[str, Any],
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        min_history_days: Optional[int] = None,
        progress_callback: Optional[Callable[[int, int, str], None]] = None,
    ) -> BacktestResult:
        """
        Backtest a single strategy configuration.

        Args:
            strategy_class: Strategy class to test
            strategy_params: Parameters for the strategy
            start_date: Start date for backtesting
            end_date: End date for backtesting
            min_history_days: Minimum days of history needed before starting predictions
            progress_callback: Optional callback function for progress reporting (current, total, message)

        Returns:
            BacktestResult object
        """
        import time

        start_time = time.time()

        # Validate strategy and parameters
        try:
            self._validate_strategy_params(strategy_class, strategy_params)
        except ValueError as e:
            error_msg = f"Invalid strategy or parameters: {e}"
            logger.error(error_msg)
            return self._empty_result(strategy_class.__name__, strategy_params, error_msg)

        # Use instance default if not provided
        if min_history_days is None:
            min_history_days = self.min_history_days

        # Determine backtest period
        if start_date is None:
            start_date = self.df["date"].min() + timedelta(days=min_history_days)
        if end_date is None:
            end_date = self.df["date"].max()

        # Validate dates
        if start_date > end_date:
            error_msg = f"Start date ({start_date}) is after end date ({end_date})"
            logger.error(error_msg)
            return self._empty_result(strategy_class.__name__, strategy_params, error_msg)

        # Check for sufficient historical data
        earliest_date = self.df["date"].min()
        if (start_date - earliest_date).days < min_history_days:
            logger.warning(
                f"Insufficient historical data. Have {(start_date - earliest_date).days} days, "
                f"but {min_history_days} days recommended. Results may be unreliable."
            )

        # Filter data for backtest period
        test_data = self.df[(self.df["date"] >= start_date) & (self.df["date"] <= end_date)]

        if test_data.empty:
            error_msg = "No data available for backtesting period"
            logger.warning(error_msg)
            return self._empty_result(strategy_class.__name__, strategy_params, error_msg)

        # Initialize strategy
        try:
            strategy = strategy_class(self.df, **strategy_params)
        except Exception as e:
            error_msg = f"Failed to initialize strategy {strategy_class.__name__}: {e}"
            logger.error(error_msg)
            return self._empty_result(strategy_class.__name__, strategy_params, error_msg)

        # Check for potential look-ahead bias
        has_bias, bias_reason = self._check_lookback_bias(strategy, start_date)
        if has_bias:
            logger.warning(f"Potential look-ahead bias detected in {strategy_class.__name__}: {bias_reason}")

        # Run predictions and evaluate
        results = []
        errors = []
        total_rows = len(test_data)

        for i, (_, row) in enumerate(test_data.iterrows()):
            # Report progress if callback provided
            if progress_callback:
                progress_callback(i, total_rows, f"Processing {row['date']}")

            try:
                predicted = strategy.predict(row["date"])
                actual = row["result"]

                # Validate prediction result
                if not isinstance(predicted, list) or len(predicted) != strategy.number_predict:
                    logger.warning(
                        f"Invalid prediction for date {row['date']}: "
                        f"Expected list of {strategy.number_predict} numbers, got {predicted}"
                    )
                    continue

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
                # Handle error gracefully
                diagnostic = self._handle_prediction_error(row["date"], strategy_class.__name__, e)
                errors.append(diagnostic)
                continue

        # Log summary of errors if any occurred
        if errors:
            error_types = {}
            for err in errors:
                error_type = err["error_type"]
                error_types[error_type] = error_types.get(error_type, 0) + 1

            logger.warning(
                f"Encountered {len(errors)} errors during backtest of {strategy_class.__name__}: {error_types}"
            )

        if not results:
            error_msg = "No successful predictions during backtest"
            logger.warning(error_msg)
            return self._empty_result(strategy_class.__name__, strategy_params, error_msg)

        # Calculate statistics
        result = self._calculate_backtest_stats(strategy_class.__name__, strategy_params, results)

        # Add execution time
        result.execution_time = time.time() - start_time

        return result

    def _check_lookback_bias(self, strategy: PredictModel, start_date: date) -> Tuple[bool, str]:
        """
        Check for potential look-ahead bias in the strategy.

        Args:
            strategy: Strategy instance to check
            start_date: Start date of the backtest

        Returns:
            Tuple of (has_bias, reason) where has_bias is True if potential bias detected
        """
        # This is a heuristic check for common sources of look-ahead bias

        # Check 1: Strategy has lookback_days attribute but insufficient history
        if hasattr(strategy, "lookback_days"):
            earliest_date = self.df["date"].min()
            lookback_start = start_date - timedelta(days=strategy.lookback_days)

            if lookback_start < earliest_date:
                days_available = (start_date - earliest_date).days
                days_needed = strategy.lookback_days
                return True, (
                    f"Potential look-ahead bias: Strategy requires {days_needed} days of history "
                    f"but only {days_available} days are available before start_date"
                )

        # Check 2: Strategy has methods that might access future data
        suspicious_methods = ["predict_future", "forecast", "future_trend"]
        for method_name in suspicious_methods:
            if hasattr(strategy, method_name) and callable(getattr(strategy, method_name)):
                return True, f"Potential look-ahead bias: Strategy has suspicious method '{method_name}'"

        # Check 3: Strategy class has warning in its docstring
        if strategy.__class__.__doc__ and "future data" in strategy.__class__.__doc__.lower():
            return True, "Potential look-ahead bias: Strategy documentation mentions 'future data'"

        # Check 4: Strategy has attributes that suggest future knowledge
        future_attrs = ["future_data", "forecast_model", "future_trends"]
        for attr in future_attrs:
            if hasattr(strategy, attr):
                return True, f"Potential look-ahead bias: Strategy has suspicious attribute '{attr}'"

        return False, ""

    def _handle_prediction_error(self, date_val: date, strategy_name: str, error: Exception) -> Dict[str, Any]:
        """
        Handle errors during prediction gracefully.

        Args:
            date_val: Date for which prediction failed
            strategy_name: Name of the strategy
            error: Exception that occurred

        Returns:
            Dictionary with diagnostic information
        """
        error_type = type(error).__name__
        error_msg = str(error)

        logger.warning(f"Prediction failed for date {date_val}: {error_type}: {error_msg}")

        # Create diagnostic information
        diagnostic = {
            "date": date_val,
            "error_type": error_type,
            "error_message": error_msg,
            "strategy": strategy_name,
            "recommendation": self._get_error_recommendation(error_type, error_msg),
        }

        return diagnostic

    def _get_error_recommendation(self, error_type: str, error_msg: str) -> str:
        """
        Get recommendation for fixing common errors.

        Args:
            error_type: Type of error
            error_msg: Error message

        Returns:
            Recommendation string
        """
        if error_type == "KeyError":
            return "Check if the strategy is trying to access a non-existent key in the data"
        elif error_type == "IndexError":
            return "Check if the strategy is trying to access an index out of bounds"
        elif error_type == "TypeError":
            return "Check if the strategy is using the correct data types"
        elif error_type == "ValueError":
            if "time data" in error_msg or "date" in error_msg:
                return "Check if the strategy is handling dates correctly"
            return "Check if the strategy is using valid values"
        elif error_type == "AttributeError":
            return "Check if the strategy is trying to access a non-existent attribute"
        else:
            return "Review the strategy implementation for errors"

    def _empty_result(self, strategy_name: str, parameters: Dict[str, Any], error_msg: str = "") -> BacktestResult:
        """
        Create empty result for failed backtests.

        Args:
            strategy_name: Name of the strategy
            parameters: Strategy parameters
            error_msg: Optional error message explaining the failure

        Returns:
            Empty BacktestResult object
        """
        # Create statistical significance info with error details
        statistical_significance = {
            "error": True,
            "error_message": error_msg or "No successful predictions",
            "timestamp": datetime.now().isoformat(),
        }

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
            statistical_significance=statistical_significance,
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

        # Calculate enhanced metrics
        profit_series = [r["profit"] for r in results]
        sharpe_ratio = self._calculate_sharpe_ratio(profit_series)
        max_drawdown, drawdown_series = self._calculate_drawdown(profit_series)
        consistency_score = self._calculate_consistency(results)

        # Create prediction history for detailed analysis
        prediction_history = [
            {
                "date": r["date"],
                "predicted": r["predicted"],
                "actual": r["actual"],
                "matches": r["matches"],
                "profit": r["profit"],
                "cost": r["cost"],
                "revenue": r["revenue"],
            }
            for r in results
        ]

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
            sharpe_ratio=sharpe_ratio,
            max_drawdown=max_drawdown,
            consistency_score=consistency_score,
            prediction_history=prediction_history,
            profit_series=profit_series,
            drawdown_series=drawdown_series,
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
    ) -> pl.DataFrame:
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

        df = pl.DataFrame(results)

        # Sort by ROI by default
        if not df.is_empty():
            df = df.sort("roi", descending=True)

        return df

    def save_results(self, results_df: pl.DataFrame, filepath: str):
        """Save comparison results to file."""
        results_df.write_csv(filepath)
        logger.info(f"Results saved to {filepath}")

    def generate_report(self, results_df: pl.DataFrame) -> str:
        """Generate a text report from comparison results."""
        if results_df.is_empty():
            return "No results to report."

        report = "Strategy Comparison Report\n"
        report += "=" * 50 + "\n\n"

        for row in results_df.iter_rows(named=True):
            report += f"Strategy: {row['strategy_name']}\n"
            report += f"Parameters: {row['parameters']}\n"
            report += f"ROI: {row['roi']:.2f}%\n"
            report += f"Win Rate: {row['win_rate']:.2f}%\n"
            report += f"Avg Matches: {row['avg_matches']:.2f}\n"
            report += f"Net Profit: {row['net_profit']:,.0f} VND\n"
            report += f"Total Predictions: {row['total_predictions']}\n"
            report += "-" * 30 + "\n"

        return report
