import numpy as np

from app.services.methods.base import BaseMCDA


class VIKOR(BaseMCDA):
    def rank(
        self,
        matrix: list[list[float]],
        weights: list[float],
        types: list[int],
        v: float = 0.5,
    ) -> list[int]:
        np_matrix, np_weights, np_types = self._validate(matrix, weights, types)

        f_best = np.where(
            np_types > 0, np.max(np_matrix, axis=0), np.min(np_matrix, axis=0)
        )
        f_worst = np.where(
            np_types > 0, np.min(np_matrix, axis=0), np.max(np_matrix, axis=0)
        )

        distances = (f_best - np_matrix) / (f_best - f_worst)

        S = np.sum(np_weights * distances, axis=1)

        R = np.max(np_weights * distances, axis=1)

        Q_scores = v * (S - np.min(S)) / (np.max(S) - np.min(S)) + (1 - v) * (
            R - np.min(R)
        ) / (np.max(R) - np.min(R))

        ranked = (np.argsort(np.argsort(Q_scores)) + 1).tolist()
        return ranked
