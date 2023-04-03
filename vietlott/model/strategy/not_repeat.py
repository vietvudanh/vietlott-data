from collections import Counter
from datetime import date, timedelta
from typing import List

import pandas as pd

from vietlott.model.strategy.base import BaseStrategy


class NotRepeatStrategy(BaseStrategy):
    """
    base strategy for prediction
    """

    def predict(self,
                dataset: pd.DataFrame,
                input_date: date,
                window_date: int = 10000) -> List[int]:
        """
        predict result for single date
        :param dataset:
        :param window_date:
        :param input_date:
        :return: list int
        """
        df_before = dataset[
            (dataset.date < input_date)
            & (dataset.date >= (input_date - timedelta(days=window_date)))
            ]
        df_before_explode = df_before.explode('result')
        all_results = Counter(df_before_explode['result'].value_counts().to_dict())
        least_common_results = all_results.most_common()[-self.product_config.size_output:]
        return [value for value, value_count in least_common_results]
