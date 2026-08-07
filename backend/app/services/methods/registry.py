from typing import Any

from app.services.methods.base import BaseMCDA

from app.services.methods.topsis import TOPSIS
from app.services.methods.vikor import VIKOR
from app.services.methods.waspas import WASPAS
from app.services.methods.aras import ARAS


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
    {
        "id": "aras",
        "name": "ARAS",
        "normalization": True,
        "default_normalization": "sum",
        "parameters": [],
    },
]

RANKING_REGISTRY: dict[str, type[BaseMCDA]] = {
    "topsis": TOPSIS,
    "waspas": WASPAS,
    "vikor": VIKOR,
    "aras": ARAS,
}


def get_ranking_methods() -> list[dict[str, Any]]:
    return RANKING_METADATA


def get_method(method: str) -> type[BaseMCDA]:
    if method not in RANKING_REGISTRY:
        raise ValueError(
            f"Unknown normalization method: '{method}'. Available methods: {list(RANKING_REGISTRY.keys())}"
        )
    return RANKING_REGISTRY[method]
