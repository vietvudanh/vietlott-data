"""
Machine Learning module for Vietlott lottery prediction and analysis.

This module contains various strategies for predicting lottery numbers,
along with backtesting and parameter tuning capabilities.

This is an optional module that requires additional ML dependencies.
Install with: pip install vietlott-data[ml]
"""

from .backtest import BacktestResult, ParameterTuner, StrategyBacktester, StrategyComparator
from .base import PredictModel
from .frequency import ColdNumbersStrategy, FrequencyStrategy, HotNumbersStrategy
from .long_absence import LongAbsenceStrategy
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
    "LongAbsenceStrategy",
    # Backtesting and tuning
    "StrategyBacktester",
    "ParameterTuner",
    "StrategyComparator",
    "BacktestResult",
]
