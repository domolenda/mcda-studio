from pydantic import BaseModel


class RankingRequest(BaseModel):
    matrix: list[list[float]]
    types: list[int]
    weights: list[float]
    normalization_method: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "matrix": [
                        [200.0, 0.5, 250.0],
                        [180.0, 1.0, 300.0],
                        [100.0, 1.0, 400.0],
                    ],
                    "types": [1, 1, -1],
                    "weights": [0.4, 0.35, 0.25],
                    "normalization_method": "min_max",
                }
            ]
        }
    }


class RankingResponse(BaseModel):
    ranking: list[int]

    model_config = {"json_schema_extra": {"examples": [{"ranking": [2, 1, 3]}]}}
