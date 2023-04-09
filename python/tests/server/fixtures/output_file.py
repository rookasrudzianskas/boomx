import io

from boomx import BasePredictor, File


class Predictor(BasePredictor):
    def predict(self) -> File:
        return io.StringIO("hello")
