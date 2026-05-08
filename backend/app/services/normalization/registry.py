from typing import Any

from app.services.normalization.min_max import MinMaxNormalization

NORMALIZATION_REGISTRY: dict[str, Any] = {
    "min_max": MinMaxNormalization,
}


def get_normalization(method: str) -> Any:
    if method not in NORMALIZATION_REGISTRY:
        raise ValueError(
            f"Unknown normalization method: '{method}'. Available methods: {list(NORMALIZATION_REGISTRY.keys())}"
        )
    return NORMALIZATION_REGISTRY[method]
