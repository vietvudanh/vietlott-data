from datetime import date
from typing import List


class BaseStrategy:
    """
    base strategy for prediction
    """
    allow_product: List[str] = None

    def __init__(self):
        pass

    def predict(self, input_date: date) -> List[int]:
        """
        predict result for single date
        :param input_date:
        :return: list int
        """
        pass