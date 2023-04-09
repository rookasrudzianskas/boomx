from pydantic import BaseModel

from boomx import BasePredictor


class Output(BaseModel):
    hello: str
    goodbye: str


class Predictor(BasePredictor):
    def predict(self, name: str) -> Output:
        return Output(
            hello="hello " + name,
            goodbye="goodbye " + name,
        )
