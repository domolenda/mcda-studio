import numpy as np

from app.services.methods.base import BaseMCDA


class TOPSIS(BaseMCDA):
    def _calc_weighted_matrix(self) -> np.ndarray:
        return self.normalized_matrix * self.weights

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

    def rank(self) -> list[int]:
        self._validate()
        weighted_matrix = self._calc_weighted_matrix()
        pis, nis = self._calc_pis_nis(weighted_matrix)
        euclidean_pis = self._euclidean_distance(weighted_matrix, pis)
        euclidean_nis = self._euclidean_distance(weighted_matrix, nis)
        scores = self._score(euclidean_pis, euclidean_nis)
        ranked = (np.argsort(scores)[::-1] + 1).tolist()
        return ranked
