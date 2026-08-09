from app.services.normalization.base import BaseNormalization

from app.services.normalization.linear import LinearNormalization
from app.services.normalization.min_max import MinMaxNormalization
from app.services.normalization.vector import VectorNormalization
from app.services.normalization.sum import SumNormalization


NORMALIZATION_REGISTRY: dict[str, type[BaseNormalization]] = {
    "min_max": MinMaxNormalization,
    "linear": LinearNormalization,
    "vector": VectorNormalization,
    "sum": SumNormalization,
}

NORMALIZATION_METADATA: list[dict[str, str]] = [
    {
        "id": "min_max",
        "name": "Min-Max",
    },
    {
        "id": "linear",
        "name": "Linear",
    },
    {
        "id": "vector",
        "name": "Vector",
    },
    {
        "id": "sum",
        "name": "Sum",
    },
]


def get_normalization(method: str) -> type[BaseNormalization]:
    if method not in NORMALIZATION_REGISTRY:
        raise ValueError(
            f"Unknown normalization method: '{method}'. Available methods: {list(NORMALIZATION_REGISTRY.keys())}"
        )
    return NORMALIZATION_REGISTRY[method]


def get_normalization_methods() -> list[dict[str, str]]:
    return NORMALIZATION_METADATA
