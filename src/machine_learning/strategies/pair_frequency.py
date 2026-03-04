"""
Pair co-occurrence frequency strategy.

All existing strategies treat numbers independently and only consider
individual frequency signals.  This strategy captures second-order
correlations by counting how often pairs of numbers appear *together*
in the same draw.  Predictions are assembled greedily: pick the first
number by individual frequency, then iteratively pick the number with
the highest average co-occurrence score with the already-selected set.
"""

import random
from collections import defaultdict
from datetime import date, timedelta
from typing import Dict, List, Tuple

import pandas as pd

from machine_learning.strategies.base import PredictModel


class PairFrequencyStrategy(PredictModel):
    """
    Selects numbers based on pairwise co-occurrence frequency.

    Builds a co-occurrence matrix within a rolling lookback window:
    ``cooccurrence[a][b]`` = number of historical draws where both
    ``a`` and ``b`` appeared.  Predictions are assembled iteratively:

    1. The first number is sampled proportional to individual frequency
       (with Laplace smoothing so all numbers are eligible).
    2. Each subsequent slot is filled by sampling from remaining numbers
       with probability proportional to their *average co-occurrence score*
       with the numbers already chosen.

    Why this may outperform single-number strategies
    -------------------------------------------------
    * Captures second-order correlations ignored by all other strategies.
    * Numbers that frequently cluster together are preferred, generating
      "cohesive" tickets rather than statistically independent selections.
    * The greedy assembly still has randomness (via weighted sampling) so
      ``time_predict`` tickets diversify the predictions.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
        lookback_days: int = 365,
    ):
        """
        Parameters
        ----------
        lookback_days:
            Rolling window (days) used to compute co-occurrence counts.
            Longer window = more stable but less responsive to recent shifts.
        """
        super().__init__(df, time_predict, min_val, max_val)
        self.lookback_days = lookback_days
        self._prepare_historical_data()
        self._cooccurrence_cache: Dict[date, Tuple] = {}

    def _prepare_historical_data(self) -> None:
        self.df_sorted = self.df.sort_values("date").reset_index(drop=True)

    def _compute_cooccurrence(self, target_date: date) -> Tuple[Dict[int, int], Dict[int, Dict[int, int]]]:
        """
        Compute individual frequency and symmetric co-occurrence counts.

        Uses ``.tolist()`` iteration (avoiding ``iterrows()``) over the
        filtered window; the inner pairwise loop is O(k²) where k=6
        (fixed draw size), so it scales linearly with the number of draws.

        Returns
        -------
        (individual_freq, cooccurrence)
            ``individual_freq[n]`` = draw count for number n.
            ``cooccurrence[a][b]`` = joint draw count for numbers a and b.
        """
        start_date = target_date - timedelta(days=self.lookback_days)
        mask = (self.df_sorted["date"] >= start_date) & (self.df_sorted["date"] < target_date)
        results_list: List[List[int]] = self.df_sorted.loc[mask, "result"].tolist()

        individual_freq: Dict[int, int] = defaultdict(int)
        cooccurrence: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))

        for nums in results_list:
            valid = [n for n in nums if self.min_val <= n <= self.max_val]
            for n in valid:
                individual_freq[n] += 1
            # All (i,j) pairs — O(k²) = O(36) per draw, negligible.
            for i in range(len(valid)):
                for j in range(i + 1, len(valid)):
                    cooccurrence[valid[i]][valid[j]] += 1
                    cooccurrence[valid[j]][valid[i]] += 1

        return dict(individual_freq), {k: dict(v) for k, v in cooccurrence.items()}

    def predict(self, target_date: date) -> List[int]:
        """Predict numbers using greedy co-occurrence assembly."""
        if target_date not in self._cooccurrence_cache:
            self._cooccurrence_cache[target_date] = self._compute_cooccurrence(target_date)
        individual_freq, cooccurrence = self._cooccurrence_cache[target_date]

        all_numbers = list(range(self.min_val, self.max_val + 1))
        # Laplace smoothing: every number has weight >= 1.
        freqs = [individual_freq.get(n, 0) + 1 for n in all_numbers]

        # Step 1: pick first number weighted by individual frequency.
        first = random.choices(all_numbers, weights=freqs)[0]
        predicted: List[int] = [first]

        # Step 2: greedily extend using average co-occurrence with chosen set.
        remaining = [n for n in all_numbers if n != first]
        while len(predicted) < self.number_predict and remaining:
            scores = [
                sum(cooccurrence.get(p, {}).get(n, 0) for p in predicted) / len(predicted) + 0.1 for n in remaining
            ]
            chosen = random.choices(remaining, weights=scores)[0]
            predicted.append(chosen)
            remaining.remove(chosen)

        return sorted(predicted)
