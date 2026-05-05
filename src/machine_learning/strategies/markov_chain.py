"""
Markov Chain strategy.

All existing strategies treat each draw in isolation, selecting numbers based
on static aggregate statistics (frequency, absence, co-occurrence within a draw,
etc.).  This strategy is different: it models the **sequential dependency
between consecutive draws**.

Core idea
---------
Define a transition matrix ``T[a][b]`` = number of times that number ``a``
appeared in draw ``t`` **and** number ``b`` appeared in the *next* draw
``t+1`` within a rolling lookback window.

To predict for date ``d``:

1. Identify the most recent draw *before* ``d`` — call it the "Markov state".
2. For every candidate number ``n`` in ``[min_val, max_val]``, compute an
   aggregate score by summing transition counts ``T[s][n]`` over every
   number ``s`` in the state draw.  This answers: *"Given that these
   specific numbers were drawn last time, how often has each candidate
   number followed them in history?"*
3. Sample ``number_predict`` distinct numbers without replacement, with
   probability proportional to (score + Laplace smoothing constant).

Why this may outperform existing strategies
-------------------------------------------
* Captures **cross-draw temporal correlations** that every other strategy
  ignores.  Frequency, exponential-decay and pattern strategies only look at
  how often a number appeared in the past, not *what came after* specific
  preceding draws.
* The Markov state is concrete and interpretable: the last known draw acts
  as a "fingerprint" that biases the next prediction.
* Laplace smoothing ensures every number retains a small non-zero chance,
  preventing the model from permanently ruling out any number.

Limitations
-----------
For a fair lottery the draws are independent, so no true first-order Markov
dependency exists.  However, if the observed data exhibits any subtle
correlation (e.g., due to physical ball-selection mechanisms), this strategy
may detect it.  The strategy is included for rigorous empirical comparison.
"""

import random
from collections import defaultdict
from datetime import date, timedelta
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from machine_learning.strategies.base import PredictModel


class MarkovChainStrategy(PredictModel):
    """
    Selects numbers using a first-order Markov chain transition matrix.

    For each pair of consecutive draws ``(draw_t, draw_{t+1})`` in the
    lookback window, every ``(number_in_t, number_in_{t+1})`` ordered pair
    increments ``transition_matrix[a][b]``.

    Prediction for date ``d``:

    * Look up the immediately preceding draw (the "Markov state").
    * Score each candidate number by summing its transition counts from
      every number in the state draw.
    * Sample ``number_predict`` numbers weighted by (score + smoothing).

    Parameters
    ----------
    lookback_days:
        Rolling window (days) used to build the transition matrix.
        Longer window → more stable statistics; shorter → more responsive
        to recent draw sequences.
    smoothing:
        Laplace smoothing constant added to every transition count before
        sampling.  Prevents zero-probability numbers from being permanently
        excluded.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
        lookback_days: int = 365,
        smoothing: float = 0.5,
    ):
        super().__init__(df, time_predict, min_val, max_val)
        self.lookback_days = lookback_days
        self.smoothing = smoothing
        self._prepare_historical_data()
        # Cache: date → (prev_draw, transition_matrix)
        self._cache: Dict[date, Tuple[Optional[List[int]], Dict[int, Dict[int, float]]]] = {}

    # ------------------------------------------------------------------
    # Preparation
    # ------------------------------------------------------------------

    def _prepare_historical_data(self) -> None:
        """Sort draws once; later calls filter by date."""
        self.df_sorted = self.df.sort_values("date").reset_index(drop=True)

    # ------------------------------------------------------------------
    # Transition matrix construction
    # ------------------------------------------------------------------

    def _build_transition_matrix(
        self,
        target_date: date,
    ) -> Tuple[Optional[List[int]], Dict[int, Dict[int, float]]]:
        """
        Compute the transition matrix and the most-recent preceding draw.

        Returns
        -------
        (prev_draw, matrix)
            ``prev_draw``  – list of numbers from the draw immediately before
                             ``target_date``, or ``None`` if no prior draw exists.
            ``matrix``     – ``matrix[a][b]`` = count of consecutive draw pairs
                             where ``a`` appeared in draw ``t`` and ``b`` appeared
                             in draw ``t+1``, within the lookback window and
                             strictly before ``target_date``.
        """
        start_date = target_date - timedelta(days=self.lookback_days)
        past = self.df_sorted[self.df_sorted["date"] < target_date]

        if past.empty:
            return None, defaultdict(lambda: defaultdict(float))

        # Most-recent draw before target_date is the Markov state.
        prev_draw: List[int] = past.iloc[-1]["result"]

        # Build transition matrix over the lookback window.
        window = past[past["date"] >= start_date]
        if window.empty:
            return prev_draw, defaultdict(lambda: defaultdict(float))

        results_list: List[List[int]] = window["result"].tolist()
        matrix: Dict[int, Dict[int, float]] = defaultdict(lambda: defaultdict(float))

        for i in range(len(results_list) - 1):
            draw_t = results_list[i]
            draw_t1 = results_list[i + 1]
            for a in draw_t:
                if self.min_val <= a <= self.max_val:
                    for b in draw_t1:
                        if self.min_val <= b <= self.max_val:
                            matrix[a][b] += 1.0

        return prev_draw, matrix

    # ------------------------------------------------------------------
    # Prediction
    # ------------------------------------------------------------------

    def predict(self, target_date: date) -> List[int]:
        """
        Predict numbers using Markov chain transition probabilities.

        Parameters
        ----------
        target_date:
            Date for which to generate a prediction.  Only draws strictly
            *before* this date are used (no look-ahead bias).

        Returns
        -------
        Sorted list of ``number_predict`` distinct integers in
        ``[min_val, max_val]``.
        """
        if target_date not in self._cache:
            self._cache[target_date] = self._build_transition_matrix(target_date)

        prev_draw, matrix = self._cache[target_date]
        all_numbers = list(range(self.min_val, self.max_val + 1))

        if prev_draw is None or not matrix:
            # No history: fall back to uniform random.
            return sorted(random.sample(all_numbers, self.number_predict))

        # Aggregate transition scores for each candidate number.
        raw_scores = np.array(
            [
                sum(matrix[s].get(n, 0.0) for s in prev_draw if self.min_val <= s <= self.max_val) + self.smoothing
                for n in all_numbers
            ]
        )

        # Normalise to a probability distribution and sample without replacement.
        probs = raw_scores / raw_scores.sum()
        chosen_indices = np.random.choice(len(all_numbers), size=self.number_predict, replace=False, p=probs)
        predicted = [all_numbers[i] for i in chosen_indices]

        return sorted(predicted)
