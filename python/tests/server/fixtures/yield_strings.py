from typing import Iterator

from boomx import BasePredictor


class Predictor(BasePredictor):
    def predict(self) -> Iterator[str]:
        predictions = ["foo", "bar", "baz"]
        for prediction in predictions:
            yield prediction
