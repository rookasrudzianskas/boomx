from time import sleep

from boomx import BasePredictor


class Predictor(BasePredictor):
    def setup(self):
        raise Exception("Failed during setup")

    def predict(self) -> str:
        return "done"
