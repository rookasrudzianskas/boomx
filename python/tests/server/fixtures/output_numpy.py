import numpy as np

from boomx import BasePredictor


class Predictor(BasePredictor):
    def predict(self) -> np.float64:
        return np.float64(1.0)
