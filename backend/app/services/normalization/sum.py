import numpy as np

from app.services.normalization.base import BaseNormalization


class SumNormalization(BaseNormalization):
    def normalize(self) -> np.ndarray:
        matrix_mask = self._create_types_mask()

        sum_profit = np.sum(self.matrix, axis=0)
        sum_cost = np.sum(1 / self.matrix, axis=0)

        norm_matrix = np.where(
            matrix_mask > 0,
            self.matrix / sum_profit,
            (1 / self.matrix) / sum_cost,
        )
        return norm_matrix
