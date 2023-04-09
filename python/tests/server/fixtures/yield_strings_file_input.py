from typing import Iterator
from boomx import BasePredictor, Path


class Predictor(BasePredictor):
    def predict(self, file: Path) -> Iterator[str]:
        with file.open() as f:
            prefix = f.read()
        predictions = ["foo", "bar", "baz"]
        for prediction in predictions:
            yield prefix + " " + prediction
