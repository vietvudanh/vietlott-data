"""
Lottery prediction strategies module.

This module contains various strategies for predicting lottery numbers,
along with backtesting and parameter tuning capabilities.
"""

from .backtest import BacktestResult, ParameterTuner, StrategyBacktester, StrategyComparator
from .base import PredictModel
from .frequency import ColdNumbersStrategy, FrequencyStrategy, HotNumbersStrategy
from .not_repeat import NotRepeatStrategy
from .pattern import PatternStrategy
from .random_strategy import RandomModel

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
