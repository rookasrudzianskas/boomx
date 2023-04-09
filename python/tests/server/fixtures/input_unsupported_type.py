from pydantic import BaseModel
from boomx import BasePredictor


class Input(BaseModel):
    text: str


class Predictor(BasePredictor):
    def predict(self, input: Input) -> str:
        return input.text
