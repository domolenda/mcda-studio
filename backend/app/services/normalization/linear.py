import numpy as np

from app.services.normalization.base import BaseNormalization


class LinearNormalization(BaseNormalization):
    def __init__(self, matrix: np.ndarray, types: np.ndarray):
        super().__init__(matrix, types)

    def normalize(self) -> np.ndarray:
        matrix_mask = self._create_types_mask()

        matrix_min = np.min(self.matrix, axis=0)
        matrix_max = np.max(self.matrix, axis=0)

        norm_matrix = np.where(
            matrix_mask > 0,
            (self.matrix) / (matrix_max),
            (matrix_min) / (self.matrix),
        )
        return norm_matrix
