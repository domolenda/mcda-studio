from typing import Any

from app.services.normalization.linear import LinearNormalization
from app.services.normalization.min_max import MinMaxNormalization

NORMALIZATION_REGISTRY: dict[str, Any] = {
    "min_max": MinMaxNormalization,
    "linear": LinearNormalization,
}

NORMALIZATION_METADATA: list[dict[str, Any]] = [
    {
        "id": "min_max",
        "name": "Min-Max",
    },
    {
        "id": "linear",
        "name": "Linear",
    },
]


def get_normalization(method: str) -> Any:
    if method not in NORMALIZATION_REGISTRY:
        raise ValueError(
            f"Unknown normalization method: '{method}'. Available methods: {list(NORMALIZATION_REGISTRY.keys())}"
        )
    return NORMALIZATION_REGISTRY[method]


def get_normalization_methods() -> list[dict[str, Any]]:
    return NORMALIZATION_METADATA
