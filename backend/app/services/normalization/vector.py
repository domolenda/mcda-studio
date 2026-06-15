import numpy as np

from app.services.normalization.base import BaseNormalization


class VectorNormalization(BaseNormalization):
    def normalize(self) -> np.ndarray:
        matrix_mask = self._create_types_mask()

        norm_matrix = np.where(
            matrix_mask > 0,
            self.matrix / np.sqrt(np.sum(self.matrix**2, axis=0)),
            1 - (self.matrix / np.sqrt(np.sum(self.matrix**2, axis=0))),
        )
        return norm_matrix
