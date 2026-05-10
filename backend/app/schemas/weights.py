from pydantic import BaseModel


class WeightsRequest(BaseModel):
    matrix: list[list[float]]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "matrix": [
                        [200.0, 0.5, 250.0],
                        [180.0, 1.0, 300.0],
                        [100.0, 1.0, 400.0],
                    ]
                }
            ]
        }
    }


class WeightsResponse(BaseModel):
    weights: list[float]
    model_config = {
        "json_schema_extra": {"examples": [{"weights": [0.33, 0.33, 0.34]}]}
    }
