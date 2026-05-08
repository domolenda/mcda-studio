from abc import ABC, abstractmethod

import numpy as np


class BaseMCDA(ABC):
    def __init__(
        self,
        normalized_matrix: list[list[float]],
        weights: list[float],
        types: list[int],
    ):
        self.normalized_matrix = np.array(normalized_matrix)
        self.weights = np.array(weights)
        self.types = np.array(types)

    def _validate(self) -> None:
        if not np.isclose(np.sum(self.weights), 1.0):
            raise ValueError("Weights must sum to 1.0")

        if len(self.weights) != self.normalized_matrix.shape[1]:
            raise ValueError(
                "Number of weights must match the number of columns in the matrix"
            )

    @abstractmethod
    def rank(self) -> np.ndarray:
        pass
