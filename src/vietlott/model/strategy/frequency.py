import random
from datetime import date, timedelta
from typing import Dict, List

import pandas as pd

from vietlott.model.strategy.base import PredictModel


class FrequencyStrategy(PredictModel):
    """
    Strategy that selects numbers based on their historical frequency.
    Can favor either hot numbers (frequently drawn) or cold numbers (rarely drawn).
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
        lookback_days: int = 365,
        strategy_type: str = "hot",  # "hot", "cold", or "balanced"
        selection_weight: float = 0.8,
    ):
        """
        Initialize FrequencyStrategy.

        Args:
            df: Historical lottery data
            time_predict: Number of predictions per date
            min_val: Minimum number value
            max_val: Maximum number value
            lookback_days: Number of days to analyze for frequency
            strategy_type: "hot" (favor frequent), "cold" (favor rare), "balanced" (mix)
            selection_weight: Weight for frequency-based selection vs random
        """
        super().__init__(df, time_predict, min_val, max_val)
        self.lookback_days = lookback_days
        self.strategy_type = strategy_type
        self.selection_weight = selection_weight
        self._prepare_historical_data()

    def _prepare_historical_data(self):
        """Prepare historical data for frequency analysis."""
        self.df_sorted = self.df.sort_values("date")

    def _get_frequency_data(self, target_date: date) -> Dict[int, int]:
        """
        Get frequency count for each number in the lookback period.

        Args:
            target_date: The date for which we're making predictions

        Returns:
            Dictionary mapping number to frequency count
        """
        start_date = target_date - timedelta(days=self.lookback_days)

        # Filter data for the lookback period
        mask = (self.df_sorted["date"] >= start_date) & (self.df_sorted["date"] < target_date)
        relevant_data = self.df_sorted[mask]

        # Count frequency of each number
        frequency_counts = {}
        all_numbers = list(range(self.min_val, self.max_val + 1))

        # Initialize all numbers with 0 count
        for num in all_numbers:
            frequency_counts[num] = 0

        # Count actual frequencies
        for _, row in relevant_data.iterrows():
            for num in row["result"]:
                if num in frequency_counts:
                    frequency_counts[num] += 1

        return frequency_counts

    def _create_weighted_selection_pool(self, frequency_data: Dict[int, int]) -> List[int]:
        """
        Create a weighted pool based on frequency data and strategy type.

        Args:
            frequency_data: Dictionary of number frequencies

        Returns:
            List of numbers with appropriate weighting
        """
        if self.strategy_type == "hot":
            # Favor frequently drawn numbers
            sorted_nums = sorted(frequency_data.items(), key=lambda x: x[1], reverse=True)
        elif self.strategy_type == "cold":
            # Favor rarely drawn numbers
            sorted_nums = sorted(frequency_data.items(), key=lambda x: x[1])
        else:  # balanced
            # Mix of hot and cold numbers
            sorted_nums = list(frequency_data.items())
            random.shuffle(sorted_nums)

        # Create weighted pool
        weighted_pool = []
        max_freq = max(frequency_data.values()) if frequency_data.values() else 1

        for num, freq in sorted_nums:
            if self.strategy_type == "hot":
                weight = max(1, freq)
            elif self.strategy_type == "cold":
                weight = max(1, max_freq - freq + 1)
            else:  # balanced
                weight = 1

            weighted_pool.extend([num] * weight)

        return weighted_pool

    def predict(self, target_date: date) -> List[int]:
        """
        Predict numbers based on frequency analysis.

        Args:
            target_date: Date for prediction

        Returns:
            List of predicted numbers
        """
        frequency_data = self._get_frequency_data(target_date)
        predicted = []

        # Determine how many numbers to select using frequency vs random
        frequency_count = int(self.number_predict * self.selection_weight)
        random_count = self.number_predict - frequency_count

        # Select numbers based on frequency
        if frequency_count > 0:
            weighted_pool = self._create_weighted_selection_pool(frequency_data)

            while len(predicted) < frequency_count and weighted_pool:
                chosen = random.choice(weighted_pool)
                if chosen not in predicted:
                    predicted.append(chosen)
                # Remove all instances of chosen number to avoid duplicates
                weighted_pool = [n for n in weighted_pool if n != chosen]

        # Fill remaining slots with random selection
        if random_count > 0:
            all_numbers = list(range(self.min_val, self.max_val + 1))
            available = [n for n in all_numbers if n not in predicted]

            if len(available) >= random_count:
                predicted.extend(random.sample(available, random_count))
            else:
                predicted.extend(available)

        return sorted(predicted)


class HotNumbersStrategy(FrequencyStrategy):
    """Convenience class for hot numbers strategy."""

    def __init__(self, df: pd.DataFrame, **kwargs):
        kwargs["strategy_type"] = "hot"
        super().__init__(df, **kwargs)


class ColdNumbersStrategy(FrequencyStrategy):
    """Convenience class for cold numbers strategy."""

    def __init__(self, df: pd.DataFrame, **kwargs):
        kwargs["strategy_type"] = "cold"
        super().__init__(df, **kwargs)
