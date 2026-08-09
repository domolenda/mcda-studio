import numpy as np

from app.services.methods.base import BaseMCDA


class BaseExtendedMCDA(BaseMCDA):
    def _calc_weighted_matrix(self, normalized_matrix, weights) -> np.ndarray:
        return normalized_matrix * weights
