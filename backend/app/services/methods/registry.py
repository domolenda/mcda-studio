from typing import Any

RANKING_METADATA: list[dict[str, Any]] = [
    {
        "id": "topsis",
        "name": "TOPSIS",
        "normalization": True,
        "default_normalization": "min_max",
        "parameters": [],
    },
    {
        "id": "waspas",
        "name": "WASPAS",
        "normalization": True,
        "default_normalization": "linear",
        "parameters": [
            {"name": "lambda_", "type": "float", "default": 0.5, "min": 0.0, "max": 1.0}
        ],
    },
    {
        "id": "vikor",
        "name": "VIKOR",
        "normalization": False,
        "default_normalization": None,
        "parameters": [
            {"name": "v", "type": "float", "default": 0.5, "min": 0.0, "max": 1.0}
        ],
    },
]


def get_ranking_methods() -> list[dict[str, Any]]:
    return RANKING_METADATA
