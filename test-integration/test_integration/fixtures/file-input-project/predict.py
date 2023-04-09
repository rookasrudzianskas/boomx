from boomx import BasePredictor, Path


class Predictor(BasePredictor):
    def predict(self, path: Path) -> str:
        with open(path) as f:
            return f.read()
