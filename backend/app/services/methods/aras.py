import numpy as np

from app.services.methods.base_extended import BaseExtendedMCDA
from app.services.normalization.registry import get_normalization


class ARAS(BaseExtendedMCDA):
    def _calc_optimal_values(self, matrix: np.ndarray, types: np.ndarray) -> np.ndarray:
        return np.where(types == 1, matrix.max(axis=0), matrix.min(axis=0))

    def rank(
        self,
        matrix: list[list[float]],
        weights: list[float],
        types: list[int],
        normalization_method: str | None = None,
    ) -> list[int]:
        method = normalization_method or "sum"
        np_matrix, np_weights, np_types = self._validate(matrix, weights, types)

        optimal_values = self._calc_optimal_values(np_matrix, np_types)
        ext_matrix = np.vstack([optimal_values, np_matrix])
        normalization = get_normalization(method)
        normalized_matrix = normalization(ext_matrix, np_types).normalize()

        weighted_matrix = self._calc_weighted_matrix(normalized_matrix, np_weights)

        S_all = np.sum(weighted_matrix, axis=1)
        S_0 = S_all[0]
        S = S_all[1:]
        K = S / S_0

        ranked = (np.argsort(np.argsort(K)[::-1]) + 1).tolist()
        return ranked
