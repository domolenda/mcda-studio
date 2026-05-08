from abc import ABC, abstractmethod

import numpy as np


class BaseNormalization(ABC):
    def __init__(self, matrix: np.ndarray):
        self.matrix = matrix

    @abstractmethod
    def normalize(self) -> np.ndarray:
        pass
