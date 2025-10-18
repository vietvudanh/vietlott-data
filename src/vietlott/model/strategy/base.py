import polars as pl


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
        df: pl.DataFrame,
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
        # Explode the series and count values
        return number_series.explode().value_counts().sort("count", descending=True).rename({"count": "times"})

    @classmethod
    def _compare_list(cls, l1, l2):
        l1_s = set(l1)
        l2_s = set(l2)
        inter = l1_s.intersection(l2_s)
        return len(inter) == len(l1), len(inter)

    def predict(self, date):
        pass

    def backtest(self):
        _df = self.df.clone()

        # Process each row to create predictions
        predictions = []
        for row in _df.iter_rows(named=True):
            row_predictions = []
            for i in range(self.time_predict):
                loop_predict = self.predict(row["date"])
                correct, correct_num = self._compare_list(row["result"], loop_predict)
                row_predictions.append(
                    {
                        PredictModel.col_predict + "_idx": i,
                        PredictModel.col_predict: loop_predict,
                        PredictModel.col_correct: correct,
                        PredictModel.col_correct_num: correct_num,
                    }
                )
            predictions.append(row_predictions)

        # Add predictions as a new column
        _df = _df.with_columns(pl.Series(name="predict_metadata", values=predictions))
        self.df_backtest = _df

    def evaluate(self):
        # Explode the predict_metadata column
        self.df_backtest_explode = self.df_backtest.explode(PredictModel.col_predict_metadata)

        # Extract fields from the dictionary in predict_metadata
        metadata_df = self.df_backtest_explode.select(
            [
                pl.col(PredictModel.col_predict_metadata)
                .struct.field(PredictModel.col_predict + "_idx")
                .alias(PredictModel.col_predict + "_idx"),
                pl.col(PredictModel.col_predict_metadata)
                .struct.field(PredictModel.col_predict)
                .alias(PredictModel.col_predict),
                pl.col(PredictModel.col_predict_metadata)
                .struct.field(PredictModel.col_correct)
                .alias(PredictModel.col_correct),
                pl.col(PredictModel.col_predict_metadata)
                .struct.field(PredictModel.col_correct_num)
                .alias(PredictModel.col_correct_num),
            ]
        )

        # Combine with original dataframe columns (excluding predict_metadata)
        original_cols = [col for col in self.df_backtest_explode.columns if col != PredictModel.col_predict_metadata]
        self.df_backtest_evaluate = pl.concat(
            [self.df_backtest_explode.select(original_cols), metadata_df],
            how="horizontal",
        )

        correct_count = self.df_backtest_evaluate.filter(pl.col(PredictModel.col_correct)).height
        correct_num_counts = (
            self.df_backtest_evaluate.group_by(PredictModel.col_correct_num).count().sort(PredictModel.col_correct_num)
        )

        return {
            "correct_time": correct_count,
            "count_correct_num": correct_num_counts,
        }

    def revenue(self):
        cost = len(self.df_backtest_evaluate) * self.ticket_price

        # Map correct_num to prizes
        gain = (
            self.df_backtest_evaluate.with_columns(
                pl.col(PredictModel.col_correct_num).replace(self.prices, default=0).alias("prize")
            )
            .select(pl.col("prize").sum())
            .item()
        )

        return cost, gain, gain - cost
