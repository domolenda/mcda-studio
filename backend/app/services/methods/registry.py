from typing import Any

from app.services.methods.topsis import TOPSIS
from app.services.methods.vikor import VIKOR
from app.services.methods.waspas import WASPAS

RANKING_METADATA: list[dict[str, Any]] = [
    {
        "id": "topsis",
        "name": "TOPSIS",
        "normalization": True,
        "default_normalization": "vector",
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

RANKING__REGISTRY: dict[str, Any] = {
    "topsis": TOPSIS,
    "waspas": WASPAS,
    "vikor": VIKOR,
}


def get_ranking_methods() -> list[dict[str, Any]]:
    return RANKING_METADATA


def get_method(method: str) -> Any:
    if method not in RANKING__REGISTRY:
        raise ValueError(
            f"Unknown normalization method: '{method}'. Available methods: {list(RANKING__REGISTRY.keys())}"
        )
    return RANKING__REGISTRY[method]
