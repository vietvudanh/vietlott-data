"""
Exponential-decay frequency strategy.

Rather than applying a hard lookback window (as FrequencyStrategy does),
this strategy assigns each historical draw a weight that decays
exponentially with age: ``w = exp(-ln(2) * days_ago / half_life_days)``.
This gives a smooth, principled recency bias and uses all available
history (very old draws contribute negligibly).
"""

import math
import random
from datetime import date
from typing import Dict, List

import numpy as np
import pandas as pd

from machine_learning.strategies.base import PredictModel


class ExponentialDecayStrategy(PredictModel):
    """
    Selects numbers weighted by exponentially-decaying historical frequency.

    Each draw in history contributes a score of ``exp(-ln(2) * days_ago /
    half_life_days)`` to every number it contained.  Numbers are then
    selected from a pool weighted by these accumulated scores.

    ``hot=True``  → bias toward high-scoring (recently frequent) numbers.
    ``hot=False`` → bias toward low-scoring (recently rare) numbers.

    Why it may beat flat-window strategies
    ---------------------------------------
    * No arbitrary hard cutoff — all history contributes, recent draws
      proportionally more.
    * Smooth decay avoids the "cliff" where a number suddenly loses all
      weight when it ages past the window boundary.
    * Captures momentum (hot=True) or contrarian/mean-reversion (hot=False)
      signals more precisely than FrequencyStrategy.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
        half_life_days: int = 90,
        hot: bool = True,
        selection_weight: float = 0.8,
    ):
        """
        Parameters
        ----------
        half_life_days:
            Days after which a draw's contribution is halved.
            Smaller → stronger recency bias; larger → more history considered.
        hot:
            ``True`` → prefer recently frequent numbers (momentum).
            ``False`` → prefer recently rare numbers (contrarian).
        selection_weight:
            Fraction of the ticket filled from the score-weighted pool.
            The remainder is filled uniformly at random.
        """
        super().__init__(df, time_predict, min_val, max_val)
        self.half_life_days = half_life_days
        self.hot = hot
        self.selection_weight = selection_weight
        self._decay_lambda = math.log(2) / half_life_days
        self._prepare_historical_data()
        self._score_cache: Dict[date, Dict[int, float]] = {}

    def _prepare_historical_data(self) -> None:
        self.df_sorted = self.df.sort_values("date").reset_index(drop=True)

    def _compute_scores(self, target_date: date) -> Dict[int, float]:
        """
        Compute exponentially-weighted frequency scores for each number.

        Uses vectorised pandas explode + groupby to avoid Python-level loops
        over individual draw rows.
        """
        past = self.df_sorted[self.df_sorted["date"] < target_date].copy()
        scores: Dict[int, float] = {n: 0.0 for n in range(self.min_val, self.max_val + 1)}

        if past.empty:
            return scores

        # Vectorised weight per row.
        past["_days_ago"] = past["date"].apply(lambda d: (target_date - d).days)
        past["_weight"] = np.exp(-self._decay_lambda * past["_days_ago"].to_numpy())

        # Explode result lists and sum weights per number in one groupby pass.
        exploded = past[["result", "_weight"]].explode("result").dropna(subset=["result"])
        exploded["result"] = exploded["result"].astype(int)
        grouped = exploded.groupby("result")["_weight"].sum()

        for num, score in grouped.items():
            if num in scores:
                scores[num] = float(score)

        return scores

    def predict(self, target_date: date) -> List[int]:
        """Predict numbers using exponentially-weighted frequency scores."""
        if target_date not in self._score_cache:
            self._score_cache[target_date] = self._compute_scores(target_date)
        scores = self._score_cache[target_date]

        sorted_nums = sorted(scores.keys(), key=lambda n: scores[n], reverse=self.hot)
        max_score = scores[sorted_nums[0]] if sorted_nums else 1.0

        # Build weighted pool (repetition proportional to score / inverse-score).
        weighted_pool: List[int] = []
        for num in sorted_nums:
            s = scores[num]
            if self.hot:
                w = max(1, round(s * 10))
            else:
                w = max(1, round((max_score - s + 0.1) * 10))
            weighted_pool.extend([num] * w)

        freq_count = int(self.number_predict * self.selection_weight)
        random_count = self.number_predict - freq_count

        predicted: List[int] = []
        pool = weighted_pool[:]
        while len(predicted) < freq_count and pool:
            chosen = random.choice(pool)
            if chosen not in predicted:
                predicted.append(chosen)
            pool = [n for n in pool if n != chosen]

        available = [n for n in range(self.min_val, self.max_val + 1) if n not in predicted]
        if len(available) >= random_count:
            predicted.extend(random.sample(available, random_count))
        else:
            predicted.extend(available)

        return sorted(predicted)
