from time import sleep

from boomx import BasePredictor


class Predictor(BasePredictor):
    def setup(self):
        sleep(5)

    def predict(self) -> str:
        sleep(15)
        return "done"
