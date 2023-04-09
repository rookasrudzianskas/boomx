from pydantic import BaseModel

from boomx import BasePredictor

# Calling this `MyOutput` to test if boomx renames it to `Output` in the schema
class MyOutput(BaseModel):
    foo_number: int = "42"
    foo_string: str = "meaning of life"


class Predictor(BasePredictor):
    def predict(
        self,
    ) -> MyOutput:
        pass
