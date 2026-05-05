from machine_learning.strategies.base import PredictModel


class RandomModel(PredictModel):
    def predict(self, *args, **kwargs):
        import random

        nums = list(range(self.min_val, self.max_val + 1))
        random.shuffle(nums)

        return sorted(nums[: PredictModel.number_predict])
