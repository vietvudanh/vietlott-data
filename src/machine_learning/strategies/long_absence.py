import random
from datetime import date
from typing import List

import pandas as pd

from machine_learning.strategies.base import PredictModel


class LongAbsenceStrategy(PredictModel):
    """
    Strategy that selects numbers based on how long they have been absent.

    For each prediction, it computes the number of days since each lottery number
    last appeared (using only data strictly before the target date), then picks
    `number_predict` numbers from the `top_n` numbers that have been absent the
    longest.  Numbers that have never appeared are treated as having been absent
    the most days.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
        top_n: int = 10,
    ):
        """
        Initialize LongAbsenceStrategy.

        Args:
            df: Historical lottery data with 'date' and 'result' columns.
            time_predict: Number of predictions per draw date.
            min_val: Minimum number value (inclusive).
            max_val: Maximum number value (inclusive).
            top_n: Pool size – the N numbers absent the longest are candidates;
                   `number_predict` numbers are then sampled from this pool.
        """
        super().__init__(df, time_predict, min_val, max_val)
        self.top_n = top_n
        self._absence_cache: dict = {}
        self._prepare_historical_data()

    def _prepare_historical_data(self):
        """Sort historical data for efficient date-based filtering."""
        self.df_sorted = self.df.sort_values("date")

    def _days_since_last_appearance(self, target_date: date) -> List[int]:
        """
        Return numbers sorted by days-since-last-appearance (most absent first).

        Results are cached per target_date.
        """
        if target_date in self._absence_cache:
            return self._absence_cache[target_date]

        past_data = self.df_sorted[self.df_sorted["date"] < target_date]

        # Build mapping: number -> most recent date it appeared (vectorised)
        last_seen: dict = {}
        if not past_data.empty:
            exploded = past_data.explode("result")
            last_seen = exploded.groupby("result")["date"].max().to_dict()

        all_numbers = list(range(self.min_val, self.max_val + 1))

        def _days_absent(n: int) -> float:
            if n not in last_seen:
                return float("inf")
            delta = target_date - last_seen[n]
            return delta.days

        result = sorted(all_numbers, key=_days_absent, reverse=True)
        self._absence_cache[target_date] = result
        return result

    def predict(self, target_date: date) -> List[int]:
        """
        Predict numbers by selecting from those absent the longest.

        Args:
            target_date: Date for prediction.

        Returns:
            Sorted list of predicted numbers.
        """
        sorted_by_absence = self._days_since_last_appearance(target_date)
        candidate_pool = sorted_by_absence[: self.top_n]

        # Sample number_predict numbers from the candidate pool
        pick_count = min(self.number_predict, len(candidate_pool))
        predicted = random.sample(candidate_pool, pick_count)

        # If the pool is smaller than required (shouldn't happen in practice),
        # fill the remainder from the remaining numbers
        if pick_count < self.number_predict:
            remaining = [n for n in sorted_by_absence[self.top_n :] if n not in predicted]
            extra_needed = self.number_predict - pick_count
            predicted.extend(random.sample(remaining, min(extra_needed, len(remaining))))

        return sorted(predicted)
