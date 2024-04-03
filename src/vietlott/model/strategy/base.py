import pandas as pd


class PredictModel:
    POWER_655_MIN_VAL = 1
    POWER_655_MAX_VAL = 55  # assume we are using power655
    number_predict = 6
    ticket_price = 10000

    prices = {6: 40_000_000_000, 5: 5_000_000_000, 4: 500000, 3: 50000}

    col_date = "date"
    col_result = "result"
    col_predict = "predicted"
    col_predict_time = "predict_time"
    col_predict_metadata = "predict_metadata"
    col_correct = "is_correct"
    col_correct_num = "correct_num"

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = POWER_655_MIN_VAL,
        max_val: int = POWER_655_MAX_VAL,
    ):
        self.df = df
        self.df_backtest = None
        self.df_backtest_explode = None
        self.df_backtest_evaluate = None
        self.time_predict = time_predict
        self.min_val = min_val
        self.max_val = max_val

    @classmethod
    def _count_number(cls, number_series):
        return number_series.explode().value_counts().to_frame("times")

    @classmethod
    def _compare_list(cls, l1, l2):
        l1_s = set(l1)
        l2_s = set(l2)
        inter = l1_s.intersection(l2_s)
        return len(inter) == len(l1), len(inter)

    def predict(self, date):
        pass

    def backtest(self):
        _df = self.df.copy()

        def fn_apply(row):
            predicted = []
            for i in range(self.time_predict):
                loop_predict = self.predict(row.date)
                correct, correct_num = self._compare_list(row.result, loop_predict)
                predicted.append(
                    {
                        PredictModel.col_predict + "_idx": i,
                        PredictModel.col_predict: loop_predict,
                        PredictModel.col_correct: correct,
                        PredictModel.col_correct_num: correct_num,
                    }
                )

            return predicted

        _df["predict_metadata"] = _df.apply(fn_apply, axis=1)
        self.df_backtest = _df

    def evaluate(self):
        self.df_backtest_explode = self.df_backtest.explode(PredictModel.col_predict_metadata)
        self.df_backtest_evaluate = pd.concat(
            [
                self.df_backtest_explode.reset_index(drop=True),
                pd.json_normalize(self.df_backtest_explode[PredictModel.col_predict_metadata]),
            ],
            axis="columns",
        )

        return {
            "correct_time": self.df_backtest_evaluate[PredictModel.col_correct].sum(),
            "count_correct_num": self.df_backtest_evaluate.value_counts(PredictModel.col_correct_num),
        }

    def revenue(self):
        cost = len(self.df_backtest_evaluate) * self.ticket_price
        gain = self.df_backtest_evaluate[PredictModel.col_correct_num].apply(lambda v: self.prices.get(v, 0)).sum()

        return cost, gain, gain - cost
