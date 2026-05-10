import numpy as np
import pytest

from app.services.weights import entropy_weights, equal_weights


def test_equal_weights(monitor_data):
    matrix = monitor_data["matrix"]
    weights = equal_weights(matrix)
    assert len(weights) == len(matrix[1])
    assert np.isclose(sum(weights), 1.0)


def test_entropy_weights(monitor_data):
    matrix = monitor_data["matrix"]
    weights = entropy_weights(matrix)
    assert len(weights) == len(matrix[1])
    assert np.isclose(sum(weights), 1.0)


def test_entropy_weights_empty_matrix():
    with pytest.raises(ValueError):
        entropy_weights([])


def test_entropy_weights_column_sums_to_zero():
    with pytest.raises(ValueError):
        entropy_weights([[1.0, 0.0], [-1.0, 0.0]])
