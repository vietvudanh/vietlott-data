"""
Lottery prediction strategy implementations.

Available strategies
--------------------
PredictModel
    Abstract base class all strategies inherit from.
RandomModel
    Pure random baseline — numbers are selected uniformly at random with no
    use of historical data.
FrequencyStrategy
    Selects numbers weighted by their draw frequency over a configurable
    lookback window.  Use ``strategy_type="hot"`` to favour the most
    frequently drawn numbers or ``"cold"`` to favour the least frequent.
HotNumbersStrategy
    Convenience subclass of ``FrequencyStrategy`` locked to ``"hot"`` mode.
ColdNumbersStrategy
    Convenience subclass of ``FrequencyStrategy`` locked to ``"cold"`` mode.
LongAbsenceStrategy
    Favours numbers that have not appeared for the longest time, under the
    assumption that overdue numbers are more likely to appear.
NotRepeatStrategy
    Avoids numbers that appeared in recent draws, preferring numbers that
    have not been drawn in the most recent ``lookback_days`` window.
PatternStrategy
    Analyses spacing between consecutive drawn numbers and range distribution
    across five equal sub-ranges to generate structurally plausible tickets.
ExponentialDecayStrategy
    Like FrequencyStrategy but uses exponentially-decaying weights so recent
    draws contribute more than old ones, with no hard window cutoff.
PairFrequencyStrategy
    Builds a co-occurrence matrix and greedily selects numbers that
    historically appear together, capturing second-order correlations.
"""

from .base import PredictModel
from .exponential_decay import ExponentialDecayStrategy
from .frequency import ColdNumbersStrategy, FrequencyStrategy, HotNumbersStrategy
from .long_absence import LongAbsenceStrategy
from .not_repeat import NotRepeatStrategy
from .pair_frequency import PairFrequencyStrategy
from .pattern import PatternStrategy
from .random_strategy import RandomModel

__all__ = [
    "PredictModel",
    "RandomModel",
    "FrequencyStrategy",
    "HotNumbersStrategy",
    "ColdNumbersStrategy",
    "NotRepeatStrategy",
    "PatternStrategy",
    "LongAbsenceStrategy",
    "ExponentialDecayStrategy",
    "PairFrequencyStrategy",
]
