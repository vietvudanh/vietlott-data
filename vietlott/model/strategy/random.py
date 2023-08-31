from vietlott.model.strategy.base import PredictModel


class RandomModel(PredictModel):
    def predict(self, *args, **kwargs):
        import random
        nums = list(range(PredictModel.min_val, PredictModel.max_val))
        random.shuffle(nums)

        return nums[:PredictModel.number_predict]
