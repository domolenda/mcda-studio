from pydantic import BaseModel


class NormalizationRequest(BaseModel):
    matrix: list[list[float]]
    types: list[int]

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
                }
            ]
        }
    }


class NormalizationResponse(BaseModel):
    normalized_matrix: list[list[float]]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "normalized_matrix": [
                        [1.0, 0.0, 1.0],
                        [0.8, 1.0, 0.667],
                        [0.0, 1.0, 0.0],
                    ]
                }
            ]
        }
    }
