"""
Base class for all lottery prediction strategies.

All concrete strategy classes must inherit from ``PredictModel`` and override
the :meth:`predict` method.  The base class provides:

* shared constants (number range, prize table, column names);
* generic :meth:`backtest` that calls ``predict`` once per row in the dataset;
* :meth:`evaluate` that flattens the backtest results and computes accuracy
  statistics; and
* :meth:`revenue` that estimates profit/loss given the prize structure.
"""

import pandas as pd


class PredictModel:
    """
    Abstract base model for Vietlott lottery number prediction.

    Sub-classes implement :meth:`predict` with their own selection logic.
    The remaining methods (:meth:`backtest`, :meth:`evaluate`, :meth:`revenue`)
    are generic and work unchanged for every strategy.

    Class-level constants
    ---------------------
    POWER_655_MIN_VAL / POWER_655_MAX_VAL
        Inclusive number range for Power 6/55 (1–55).
    number_predict
        How many distinct numbers form a single ticket (6).
    ticket_price
        Cost of a single ticket in VND (10,000).
    prices
        Mapping from ``correct_num`` → prize amount in VND.
    col_*
        Column name constants used across backtest / evaluate DataFrames.
    """

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
        """
        Parameters
        ----------
        df:
            Historical lottery draw data.  Must contain at least a ``date``
            column and a ``result`` column where each cell is a list of drawn
            numbers.
        time_predict:
            Number of independent tickets to generate per draw date during
            backtesting.  Higher values increase cost but give the model more
            chances to match any given draw.
        min_val:
            Smallest valid lottery number (inclusive).
        max_val:
            Largest valid lottery number (inclusive).
        """
        self.df = df
        self.df_backtest = None
        self.df_backtest_explode = None
        self.df_backtest_evaluate = None
        self.time_predict = time_predict
        self.min_val = min_val
        self.max_val = max_val

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @classmethod
    def _count_number(cls, number_series):
        """Return a frequency table for numbers across all draw rows."""
        return number_series.explode().value_counts().to_frame("times")

    @classmethod
    def _compare_list(cls, l1, l2):
        """
        Compare two number lists.

        Returns
        -------
        (is_full_match, intersection_size)
            ``is_full_match`` is ``True`` only when every element of ``l1``
            appears in ``l2``.
        """
        l1_s = set(l1)
        l2_s = set(l2)
        inter = l1_s.intersection(l2_s)
        return len(inter) == len(l1), len(inter)

    # ------------------------------------------------------------------
    # Core interface
    # ------------------------------------------------------------------

    def predict(self, date):
        """
        Predict lottery numbers for the given draw date.

        Sub-classes **must** override this method.

        Parameters
        ----------
        date:
            The draw date for which predictions should be generated.
            Only data strictly *before* this date should be used to avoid
            look-ahead bias.

        Returns
        -------
        list[int]
            A sorted list of ``number_predict`` distinct integers in
            ``[min_val, max_val]``.
        """
        pass

    def backtest(self):
        """
        Run the strategy over every row in ``self.df``.

        For each row the strategy generates ``time_predict`` tickets.  Each
        ticket is compared against the actual draw result and the outcome is
        stored as a list of dicts under the ``predict_metadata`` column.

        Results are saved to ``self.df_backtest``.
        """
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
        """
        Flatten backtest metadata and compute accuracy statistics.

        Populates ``self.df_backtest_explode`` and
        ``self.df_backtest_evaluate``, then returns a summary dict with:

        * ``correct_time`` – total number of fully-correct tickets.
        * ``count_correct_num`` – frequency distribution of match counts.
        """
        self.df_backtest_explode = self.df_backtest.explode(PredictModel.col_predict_metadata)
        self.df_backtest_evaluate = pd.concat(
            [
                self.df_backtest_explode.reset_index(drop=True),
                pd.json_normalize(self.df_backtest_explode[PredictModel.col_predict_metadata]).reset_index(drop=True),
            ],
            axis="columns",
        )

        return {
            "correct_time": self.df_backtest_evaluate[PredictModel.col_correct].sum(),
            "count_correct_num": self.df_backtest_evaluate.value_counts(PredictModel.col_correct_num),
        }

    def revenue(self):
        """
        Estimate financial outcome of the backtest.

        Returns
        -------
        (cost, gain, profit)
            All values in VND.  ``profit = gain - cost``.
        """
        cost = len(self.df_backtest_evaluate) * self.ticket_price
        gain = self.df_backtest_evaluate[PredictModel.col_correct_num].map(self.prices).fillna(0).astype(int).sum()

        return cost, gain, gain - cost
