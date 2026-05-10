import numpy as np


def equal_weights(matrix: list[list[float]]) -> np.ndarray:
    np_matrix = np.array(matrix)
    if np_matrix.size == 0 or np_matrix.shape[1] == 0:
        raise ValueError("Matrix must not be empty")
    return np.ones(np_matrix.shape[1]) / np_matrix.shape[1]


def entropy_weights(matrix: list[list[float]]) -> np.ndarray:
    np_matrix = np.array(matrix)
    if np_matrix.size == 0 or np_matrix.shape[1] == 0:
        raise ValueError("Matrix must not be empty")
    if np.any(np_matrix.sum(axis=0) == 0):
        raise ValueError("Matrix columns must not sum to zero")
    m = np_matrix.shape[0]
    if m < 2:
        raise ValueError("Matrix must have at least 2 alternatives for entropy weights")
    norm_matrix = np_matrix / np_matrix.sum(axis=0)
    norm_matrix = np.clip(norm_matrix, 1e-10, None)
    entropy = -np.sum(norm_matrix * np.log(norm_matrix), axis=0) / np.log(m)
    weights = (1 - entropy) / np.sum(1 - entropy)
    return weights
