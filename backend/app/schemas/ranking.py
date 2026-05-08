from pydantic import BaseModel


class RankingRequest(BaseModel):
    normalized_matrix: list[list[float]]
    types: list[int]
    weights: list[float]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "normalized_matrix": [
                        [1.0, 0.0, 1.0],
                        [0.8, 1.0, 0.667],
                        [0.0, 1.0, 0.0],
                    ],
                    "types": [1, 1, -1],
                    "weights": [0.4, 0.35, 0.25],
                }
            ]
        }
    }


class RankingResponse(BaseModel):
    ranking: list[int]

    model_config = {"json_schema_extra": {"examples": [{"ranking": [2, 1, 3]}]}}
