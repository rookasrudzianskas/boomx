import sys
from boomx import BasePredictor


class Predictor(BasePredictor):
    def predict(self, text: str) -> str:
        sys.exit(1)
