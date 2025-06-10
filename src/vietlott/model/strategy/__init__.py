"""
Lottery prediction strategies module.

This module contains various strategies for predicting lottery numbers,
along with backtesting and parameter tuning capabilities.
"""

from .base import PredictModel
from .random_strategy import RandomModel
from .not_repeat import NotRepeatStrategy
from .frequency import FrequencyStrategy, HotNumbersStrategy, ColdNumbersStrategy
from .pattern import PatternStrategy
from .backtest import StrategyBacktester, ParameterTuner, StrategyComparator, BacktestResult

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
