"""
Lottery prediction strategies module.

This module contains various strategies for predicting lottery numbers,
along with backtesting and parameter tuning capabilities.

DEPRECATED: This module is deprecated. Please use 'machine_learning' module instead.
The ML functionality has been moved to a separate module to keep the core crawler lightweight.
Install ML dependencies with: pip install vietlott-data[ml]
"""

# Re-export from machine_learning module for backwards compatibility
from machine_learning.backtest import BacktestResult, ParameterTuner, StrategyBacktester, StrategyComparator
from machine_learning.base import PredictModel
from machine_learning.frequency import ColdNumbersStrategy, FrequencyStrategy, HotNumbersStrategy
from machine_learning.not_repeat import NotRepeatStrategy
from machine_learning.pattern import PatternStrategy
from machine_learning.random_strategy import RandomModel

__all__ = [
    # Base classes
    "PredictModel",
    # Strategy implementations
    "RandomModel",
    "NotRepeatStrategy",
    "FrequencyStrategy",
    "HotNumbersStrategy",
    "ColdNumbersStrategy",
    "PatternStrategy",
    # Backtesting and tuning
    "StrategyBacktester",
    "ParameterTuner",
    "StrategyComparator",
    "BacktestResult",
]
