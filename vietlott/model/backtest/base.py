"""backtest base"""
from datetime import datetime
from typing import Dict

import pandas as pd

from vietlott.config.products import get_config
from vietlott.model.dataset import load_dataset
from vietlott.model.strategy.base import BaseStrategy

prices = {
    6: 50000000000,
    5: 5000000000,
    4: 500000,
    3: 50000
}
ticket_price = 10000


def _compare_list(l1, l2):
    l1_s = set(l1)
    l2_s = set(l2)
    inter = l1_s.intersection(l2_s)
    return len(inter) == len(l1), len(inter)


class Backtest(object):
    def __init__(self,
                 product: str,
                 strategy: type[BaseStrategy]):
        self.product = product
        self.strategy = strategy(product)

        self.product_config = get_config(self.product)
        self.dataset = load_dataset(self.product)

    def evaluate(self, input_date) -> float:
        """evaluate result, returns a float show ratio of correct result
        0 = all false
        1 = all correct"""
        actual = self.dataset.evaluate(input_date)

    def backtest(self,
                 start_date_gte: datetime = None,
                 end_date_lt: datetime = None,
                 ) -> Dict:
        """"""
        if start_date_gte or end_date_lt:
            df_backtest = self.dataset[
                (self.dataset.date >= start_date_gte)
                & (self.dataset.date < end_date_lt)
                ].copy()
        else:
            df_backtest = self.dataset.copy()
        df_backtest['predictions'] = df_backtest.apply(lambda row: self.strategy.predict(self.dataset, row.date),
                                                       axis='columns')
        df_backtest[['is_correct', 'correct_times']] = df_backtest.apply(
            lambda row: pd.Series(_compare_list(row.result, row.predictions)),
            axis='columns')
        correct = df_backtest['is_correct'].sum()
        correct_times = df_backtest['correct_times'].value_counts().to_dict()
        total_dates = len(df_backtest)
        df_backtest['revenue'] = df_backtest['correct_times'].apply(lambda v: prices.get(v))
        revenue = df_backtest['revenue'].sum()
        cost = len(df_backtest) * ticket_price
        profit = revenue - cost

        print(f"""start={start_date_gte}, end={end_date_lt}
num dates       = {total_dates}
correct         = {correct}
correct_times   = {correct_times}
ratio           = {correct / total_dates * 100}%
cost            = {cost}
revenue         = {revenue}
profit          = {profit}""")

        return {
            'total_dates': total_dates,
            'correct': correct,
            'ratio': correct / total_dates,
        }
