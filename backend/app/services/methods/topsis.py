import numpy as np

from app.services.methods.base import BaseMCDA
from app.services.normalization.registry import get_normalization


class TOPSIS(BaseMCDA):
    def _calc_weighted_matrix(self, normalized_matrix, weights) -> np.ndarray:
        return normalized_matrix * weights

    def _calc_pis_nis(
        self, weighted_matrix: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        pis = np.max(weighted_matrix, axis=0)
        nis = np.min(weighted_matrix, axis=0)
        return pis, nis

    def _euclidean_distance(
        self, weighted_matrix: np.ndarray, solution: np.ndarray
    ) -> np.ndarray:
        return np.sqrt(np.sum(np.square(weighted_matrix - solution), axis=1))

    def _score(self, euclidean_pis, euclidean_nis) -> np.ndarray:
        scores = euclidean_nis / (euclidean_pis + euclidean_nis)
        return np.round(scores, 3)

    def rank(
        self,
        matrix: list[list[float]],
        weights: list[float],
        types: list[int],
        normalization_method: str | None = None,
    ) -> list[int]:
        method = normalization_method or "min_max"
        np_matrix, np_weights, np_types = self._validate(matrix, weights, types)

        normalization = get_normalization(method)
        normalized_matrix = normalization(np_matrix, np_types).normalize()

        weighted_matrix = self._calc_weighted_matrix(normalized_matrix, np_weights)
        pis, nis = self._calc_pis_nis(weighted_matrix)
        euclidean_pis = self._euclidean_distance(weighted_matrix, pis)
        euclidean_nis = self._euclidean_distance(weighted_matrix, nis)
        scores = self._score(euclidean_pis, euclidean_nis)
        ranked = (np.argsort(scores)[::-1] + 1).tolist()
        return ranked
