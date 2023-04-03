import random
from datetime import date
from typing import List

import pandas as pd

from vietlott.model.strategy.base import BaseStrategy


class RandomStrategy(BaseStrategy):
    def predict(self, dataset: pd.DataFrame, input_date: date) -> List[int]:
        nums = list(range(self.product_config.min_value,
                          self.product_config.max_value))
        random.shuffle(nums)

        return nums[:self.product_config.size_output]
