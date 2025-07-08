import random
from collections import Counter
from datetime import date, timedelta
from typing import Any, Dict, List

import numpy as np
import pandas as pd

from vietlott.model.strategy.base import PredictModel


class PatternStrategy(PredictModel):
    """
    Strategy that analyzes patterns in number distribution and spacing.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
        lookback_days: int = 180,
        pattern_weight: float = 0.6,
    ):
        """
        Initialize PatternStrategy.

        Args:
            df: Historical lottery data
            time_predict: Number of predictions per date
            min_val: Minimum number value
            max_val: Maximum number value
            lookback_days: Number of days to analyze for patterns
            pattern_weight: Weight for pattern-based selection vs random
        """
        super().__init__(df, time_predict, min_val, max_val)
        self.lookback_days = lookback_days
        self.pattern_weight = pattern_weight
        self._prepare_historical_data()

    def _prepare_historical_data(self):
        """Prepare historical data for pattern analysis."""
        self.df_sorted = self.df.sort_values("date")

    def _analyze_spacing_patterns(self, target_date: date) -> Dict[str, Any]:
        """
        Analyze spacing patterns between consecutive numbers.

        Args:
            target_date: The date for which we're making predictions

        Returns:
            Dictionary containing spacing analysis
        """
        start_date = target_date - timedelta(days=self.lookback_days)
        mask = (self.df_sorted["date"] >= start_date) & (self.df_sorted["date"] < target_date)
        relevant_data = self.df_sorted[mask]

        spacing_patterns = []

        for _, row in relevant_data.iterrows():
            sorted_numbers = sorted(row["result"])
            spacings = []
            for i in range(1, len(sorted_numbers)):
                spacing = sorted_numbers[i] - sorted_numbers[i - 1]
                spacings.append(spacing)
            spacing_patterns.append(spacings)

        # Analyze common spacing patterns
        all_spacings = [spacing for pattern in spacing_patterns for spacing in pattern]
        spacing_counter = Counter(all_spacings)

        return {
            "common_spacings": spacing_counter.most_common(10),
            "avg_spacing": np.mean(all_spacings) if all_spacings else 1,
            "spacing_patterns": spacing_patterns,
        }

    def _analyze_range_distribution(self, target_date: date) -> Dict[str, Any]:
        """
        Analyze how numbers are distributed across ranges.

        Args:
            target_date: The date for which we're making predictions

        Returns:
            Dictionary containing range distribution analysis
        """
        start_date = target_date - timedelta(days=self.lookback_days)
        mask = (self.df_sorted["date"] >= start_date) & (self.df_sorted["date"] < target_date)
        relevant_data = self.df_sorted[mask]

        # Divide number range into segments
        range_size = (self.max_val - self.min_val + 1) // 5
        ranges = []
        for i in range(5):
            start = self.min_val + i * range_size
            end = start + range_size - 1 if i < 4 else self.max_val
            ranges.append((start, end))

        range_counts = {i: 0 for i in range(5)}

        for _, row in relevant_data.iterrows():
            for num in row["result"]:
                for i, (start, end) in enumerate(ranges):
                    if start <= num <= end:
                        range_counts[i] += 1
                        break

        return {"ranges": ranges, "range_counts": range_counts, "total_draws": len(relevant_data)}

    def _analyze_odd_even_patterns(self, target_date: date) -> Dict[str, Any]:
        """
        Analyze odd/even number patterns.

        Args:
            target_date: The date for which we're making predictions

        Returns:
            Dictionary containing odd/even analysis
        """
        start_date = target_date - timedelta(days=self.lookback_days)
        mask = (self.df_sorted["date"] >= start_date) & (self.df_sorted["date"] < target_date)
        relevant_data = self.df_sorted[mask]

        odd_even_patterns = []

        for _, row in relevant_data.iterrows():
            odd_count = sum(1 for num in row["result"] if num % 2 == 1)
            even_count = len(row["result"]) - odd_count
            odd_even_patterns.append((odd_count, even_count))

        pattern_counter = Counter(odd_even_patterns)

        return {
            "common_patterns": pattern_counter.most_common(5),
            "avg_odd_count": np.mean([p[0] for p in odd_even_patterns]),
            "avg_even_count": np.mean([p[1] for p in odd_even_patterns]),
        }

    def _generate_pattern_based_numbers(
        self, spacing_analysis: Dict, range_analysis: Dict, odd_even_analysis: Dict
    ) -> List[int]:
        """
        Generate numbers based on pattern analysis.

        Args:
            spacing_analysis: Spacing pattern analysis
            range_analysis: Range distribution analysis
            odd_even_analysis: Odd/even pattern analysis

        Returns:
            List of predicted numbers
        """
        predicted = []

        # Start with a random number in a preferred range
        range_probs = []
        total_counts = sum(range_analysis["range_counts"].values())
        for i in range(5):
            count = range_analysis["range_counts"][i]
            prob = count / total_counts if total_counts > 0 else 0.2
            range_probs.append(prob)

        # Select first number from a weighted range
        selected_range = random.choices(range(5), weights=range_probs)[0]
        range_start, range_end = range_analysis["ranges"][selected_range]
        first_num = random.randint(range_start, range_end)
        predicted.append(first_num)

        # Generate remaining numbers using spacing patterns
        common_spacings = [spacing[0] for spacing in spacing_analysis["common_spacings"][:5]]
        if not common_spacings:
            common_spacings = [1, 2, 3, 4, 5]

        while len(predicted) < self.number_predict:
            last_num = predicted[-1]
            spacing = random.choice(common_spacings)

            # Try both directions
            candidates = []
            if last_num + spacing <= self.max_val:
                candidates.append(last_num + spacing)
            if last_num - spacing >= self.min_val:
                candidates.append(last_num - spacing)

            valid_candidates = [c for c in candidates if c not in predicted]

            if valid_candidates:
                predicted.append(random.choice(valid_candidates))
            else:
                # Fallback to random selection
                available = [n for n in range(self.min_val, self.max_val + 1) if n not in predicted]
                if available:
                    predicted.append(random.choice(available))
                else:
                    break

        return sorted(predicted)

    def predict(self, target_date: date) -> List[int]:
        """
        Predict numbers based on pattern analysis.

        Args:
            target_date: Date for prediction

        Returns:
            List of predicted numbers
        """
        # Analyze patterns
        spacing_analysis = self._analyze_spacing_patterns(target_date)
        range_analysis = self._analyze_range_distribution(target_date)
        odd_even_analysis = self._analyze_odd_even_patterns(target_date)

        # Determine how many numbers to select using patterns vs random
        pattern_count = int(self.number_predict * self.pattern_weight)
        random_count = self.number_predict - pattern_count

        predicted = []

        # Select numbers based on patterns
        if pattern_count > 0:
            pattern_numbers = self._generate_pattern_based_numbers(spacing_analysis, range_analysis, odd_even_analysis)
            predicted.extend(pattern_numbers[:pattern_count])

        # Fill remaining slots with random selection
        if random_count > 0:
            all_numbers = list(range(self.min_val, self.max_val + 1))
            available = [n for n in all_numbers if n not in predicted]

            if len(available) >= random_count:
                predicted.extend(random.sample(available, random_count))
            else:
                predicted.extend(available)

        return sorted(predicted[: self.number_predict])
