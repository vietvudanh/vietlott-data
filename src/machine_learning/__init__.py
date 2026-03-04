"""
Machine Learning module for Vietlott lottery prediction and analysis.

This module contains various strategies for predicting lottery numbers,
along with backtesting and parameter tuning capabilities.

This is an optional module that requires additional ML dependencies.
Install with: pip install vietlott-data[ml]
"""

from .backtest import BacktestResult, ParameterTuner, StrategyBacktester, StrategyComparator
from .strategies import (
    ColdNumbersStrategy,
    ExponentialDecayStrategy,
    FrequencyStrategy,
    HotNumbersStrategy,
    LongAbsenceStrategy,
    NotRepeatStrategy,
    PairFrequencyStrategy,
    PatternStrategy,
    RandomModel,
)
from .strategies.base import PredictModel

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
    "ExponentialDecayStrategy",
    "PairFrequencyStrategy",
    # Backtesting and tuning
    "StrategyBacktester",
    "ParameterTuner",
    "StrategyComparator",
    "BacktestResult",
]
