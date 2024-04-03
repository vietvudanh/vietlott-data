from datetime import date
from typing import List

from vietlott.config.products import get_config
from model.strategy.base import BaseStrategy
from model.dataset import load_dataset, gen_random_list  # noqa: F401


class NotRepeatStrategy(BaseStrategy):
    """
    base strategy for prediction
    """

    allow_product: List[str] = ["power655"]

    def __init__(self, product="power655"):
        super(NotRepeatStrategy, self).__init__()
        if product not in self.allow_product:
            raise ValueError(f"product={product} not allow for {self.__class__}")
        self.product = product
        self.product_config = get_config(self.product)

    def predict(self, input_date: date) -> List[int]:
        """
        predict result for single date
        :param input_date:
        :return: list int
        """
        # dataset = load_dataset(self.product)
        return gen_random_list(
            self.product_config.min_value,
            self.product_config.max_value,
            self.product_config.size_output,
        )
