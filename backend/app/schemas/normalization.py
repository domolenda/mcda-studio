from pydantic import BaseModel


class NormalizationRequest(BaseModel):
    matrix: list[list[float]]
    types: list[int]

    model_config = {
        "json_schema_extra": {
            "examples": [{"matrix": [[1.0, 2.0], [3.0, 4.0]], "types": [1, -1]}]
        }
    }


class NormalizationResponse(BaseModel):
    normalized_matrix: list[list[float]]

    model_config = {
        "json_schema_extra": {
            "examples": [{"normalized_matrix": [[0.0, 0.5, 1.0], [0.5, 1.0, 1.5]]}]
        }
    }
