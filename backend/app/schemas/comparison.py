from pydantic import BaseModel


class ParamsConfig(BaseModel):
    name: str
    value: str | float


class MethodConfig(BaseModel):
    id: str
    name: str
    params: list[ParamsConfig]


class ComparisonRequest(BaseModel):
    matrix: list[list[float]]
    types: list[int]
    weights: list[float]
    methods_config: list[MethodConfig]

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
                    "methods_config": [
                        {
                            "name": "topsis",
                            "params": [
                                {"name": "normalization_method", "value": "min_max"}
                            ],
                        },
                        {
                            "name": "waspas",
                            "params": [
                                {"name": "normalization_method", "value": "linear"},
                                {"name": "lambda_", "value": 0.5},
                            ],
                        },
                        {
                            "name": "vikor",
                            "params": [{"name": "v", "value": 0.5}],
                        },
                    ],
                }
            ]
        }
    }


class CorrelationResponse(BaseModel):
    method_a: str
    method_b: str
    rw: float
    ws: float


class ComparisonResponse(BaseModel):
    rankings: dict[str, list[int]]
    correlations: list[CorrelationResponse]
