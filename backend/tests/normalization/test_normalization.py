import numpy as np

from app.services.normalization.linear import LinearNormalization
from app.services.normalization.min_max import MinMaxNormalization
from app.services.normalization.vector import VectorNormalization


def test_min_max_normalization(monitor_data):
    matrix = np.array(monitor_data["matrix"])
    types = np.array(monitor_data["types"])
    norm = MinMaxNormalization(matrix, types)
    norm_matrix = norm.normalize()
    assert np.all(norm_matrix >= 0.0)
    assert np.all(norm_matrix <= 1.0)
    assert norm_matrix.shape == matrix.shape


def test_linear_normalization(monitor_data):
    matrix = np.array(monitor_data["matrix"])
    types = np.array(monitor_data["types"])
    norm = LinearNormalization(matrix, types)
    norm_matrix = norm.normalize()
    assert np.all(norm_matrix >= 0.0)
    assert np.all(norm_matrix <= 1.0)
    assert norm_matrix.shape == matrix.shape


def test_vector_normalization(monitor_data):
    matrix = np.array(monitor_data["matrix"])
    types = np.array(monitor_data["types"])
    norm = VectorNormalization(matrix, types)
    norm_matrix = norm.normalize()
    assert np.all(norm_matrix >= 0.0)
    assert np.all(norm_matrix <= 1.0)
    assert norm_matrix.shape == matrix.shape
