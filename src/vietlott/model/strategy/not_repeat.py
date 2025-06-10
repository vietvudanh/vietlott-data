from datetime import date, timedelta
from typing import List
import random
import pandas as pd

from vietlott.model.strategy.base import PredictModel


class NotRepeatStrategy(PredictModel):
    """
    Strategy that avoids recently drawn numbers based on the assumption
    that numbers are less likely to repeat in consecutive draws.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
        lookback_days: int = 30,
        avoid_weight: float = 0.7,
    ):
        """
        Initialize NotRepeatStrategy.

        Args:
            df: Historical lottery data
            time_predict: Number of predictions per date
            min_val: Minimum number value
            max_val: Maximum number value
            lookback_days: Number of days to look back for recent numbers
            avoid_weight: Probability of avoiding recently drawn numbers (0-1)
        """
        super().__init__(df, time_predict, min_val, max_val)
        self.lookback_days = lookback_days
        self.avoid_weight = avoid_weight
        self._prepare_historical_data()

    def _prepare_historical_data(self):
        """Prepare historical data for quick lookups."""
        self.df_sorted = self.df.sort_values("date")
        # Create a dictionary for fast date-based lookups
        self.date_to_results = {}
        for _, row in self.df_sorted.iterrows():
            self.date_to_results[row["date"]] = row["result"]

    def _get_recent_numbers(self, target_date: date) -> set:
        """
        Get numbers that appeared in recent draws before the target date.

        Args:
            target_date: The date for which we're making predictions

        Returns:
            Set of recently drawn numbers
        """
        recent_numbers = set()
        start_date = target_date - timedelta(days=self.lookback_days)

        for draw_date, results in self.date_to_results.items():
            if start_date <= draw_date < target_date:
                recent_numbers.update(results)

        return recent_numbers

    def predict(self, target_date: date) -> List[int]:
        """
        Predict numbers by avoiding recently drawn ones.

        Args:
            target_date: Date for prediction

        Returns:
            List of predicted numbers
        """
        recent_numbers = self._get_recent_numbers(target_date)
        all_numbers = list(range(self.min_val, self.max_val + 1))

        # Separate numbers into recent and non-recent
        non_recent = [n for n in all_numbers if n not in recent_numbers]
        recent = list(recent_numbers)

        predicted = []

        # First, try to select from non-recent numbers
        if len(non_recent) >= self.number_predict:
            predicted = random.sample(non_recent, self.number_predict)
        else:
            # If not enough non-recent numbers, use all non-recent + some recent
            predicted.extend(non_recent)
            remaining_needed = self.number_predict - len(non_recent)

            # Apply avoid_weight probability
            for _ in range(remaining_needed):
                if random.random() > self.avoid_weight and recent:
                    # Choose from recent numbers
                    chosen = random.choice(recent)
                    if chosen not in predicted:
                        predicted.append(chosen)
                        recent.remove(chosen)
                else:
                    # Choose from any remaining numbers
                    available = [n for n in all_numbers if n not in predicted]
                    if available:
                        predicted.append(random.choice(available))

            # Fill remaining slots if needed
            while len(predicted) < self.number_predict:
                available = [n for n in all_numbers if n not in predicted]
                if available:
                    predicted.append(random.choice(available))
                else:
                    break

        return sorted(predicted)
