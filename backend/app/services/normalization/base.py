from abc import ABC, abstractmethod

import numpy as np


class BaseNormalization(ABC):
    def __init__(self, matrix: np.ndarray, types: np.ndarray):
        self.matrix = matrix
        self.types = types

    def _create_types_mask(self) -> np.ndarray:
        if len(self.types) != self.matrix.shape[1]:
            raise ValueError(
                "Number of types must match the number of columns in the matrix"
            )

        return np.tile(self.types, (self.matrix.shape[0], 1))

    @abstractmethod
    def normalize(self) -> np.ndarray:
        pass
