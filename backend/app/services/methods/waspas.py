import numpy as np

from app.services.methods.base import BaseMCDA
from app.services.normalization.registry import get_normalization


class WASPAS(BaseMCDA):
    def rank(
        self,
        matrix: list[list[float]],
        weights: list[float],
        types: list[int],
        normalization_method: str | None = None,
        lambda_: float = 0.5,
    ) -> list[int]:
        method = normalization_method or "linear"
        np_matrix, np_weights, np_types = self._validate(matrix, weights, types)

        normalization = get_normalization(method)
        normalized_matrix = normalization(np_matrix, np_types).normalize()

        wsm_scores = np.sum(normalized_matrix * np_weights, axis=1)
        wpm_scores = np.prod(np.power(normalized_matrix, np_weights), axis=1)
        scores = lambda_ * wsm_scores + (1 - lambda_) * wpm_scores

        ranked = (np.argsort(np.argsort(scores)[::-1]) + 1).tolist()
        return ranked
