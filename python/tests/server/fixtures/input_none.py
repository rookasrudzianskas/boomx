from boomx import BasePredictor


class Predictor(BasePredictor):
    def predict(self) -> str:
        return "foobar"
