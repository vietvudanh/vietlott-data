from datetime import date
from typing import List

import pandas as pd

from vietlott.config.products import get_config


class BaseStrategy:
    """
    base strategy for prediction
    """
    allow_product: List[str] = None

    def __init__(self, product):
        if self.allow_product and product not in self.allow_product:
            raise ValueError(f'product={product} not allow for {self.__class__}')
        self.product = product
        self.product_config = get_config(self.product)

    def predict(self, dataset: pd.DataFrame, input_date: date) -> List[int]:
        """
        predict result for single date
        :param dataset:
        :param input_date:
        :return: list int
        """
        pass
