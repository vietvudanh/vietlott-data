from vietlott.model.strategy.base import PredictModel


class RandomModel(PredictModel):
    def predict(self, *args, **kwargs):
        import random

        nums = list(range(self.min_val, self.max_val))
        random.shuffle(nums)

        return nums[: PredictModel.number_predict]
