from typing import Iterator

from boomx import BasePredictor


class Predictor(BasePredictor):
    def predict(
        self,
    ) -> Iterator[str]:
        pass
