from abc import ABC, abstractmethod

import numpy as np


class BaseNormalization(ABC):
    def __init__(self, matrix: list[list[float]]):
        self.matrix = np.array(matrix)

    @abstractmethod
    def normalize(self) -> np.ndarray:
        pass
