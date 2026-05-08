from abc import ABC, abstractmethod

import numpy as np


class BaseMCDA(ABC):
    def _validate(
        self, matrix: list[list[float]], weights: list[float], types: list[int]
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        np_matrix = np.array(matrix)
        np_weights = np.array(weights)
        np_types = np.array(types)

        if not np.isclose(np.sum(np_weights), 1.0):
            raise ValueError("Weights must sum to 1.0")

        if len(np_weights) != np_matrix.shape[1]:
            raise ValueError(
                "Number of weights must match the number of columns in the matrix"
            )

        return np_matrix, np_weights, np_types

    @abstractmethod
    def rank(
        self, matrix: list[list[float]], weights: list[float], types: list[int]
    ) -> list[int]:
        pass
