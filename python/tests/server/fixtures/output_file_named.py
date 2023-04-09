import io

from boomx import BasePredictor, File


class Predictor(BasePredictor):
    def predict(self) -> File:
        fh = io.StringIO("hello")
        fh.name = "foo.txt"
        return fh
