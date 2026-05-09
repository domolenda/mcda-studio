import pytest

from app.services.methods.topsis import TOPSIS


def test_topsis_rank(monitor_data):
    topsis = TOPSIS()
    result = topsis.rank(
        monitor_data["matrix"], monitor_data["weights"], monitor_data["types"]
    )
    assert result == [9, 2, 1, 3, 8, 6, 7, 4, 5]


def test_topsis_invalid_weights(monitor_data):
    topsis = TOPSIS()
    bad_weights = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    with pytest.raises(ValueError):
        topsis.rank(monitor_data["matrix"], bad_weights, monitor_data["types"])


def test_topsis_weights_too_short(monitor_data):
    topsis = TOPSIS()
    weights_short = [0.24, 0.17, 0.16, 0.03, 0.38]
    with pytest.raises(ValueError):
        topsis.rank(monitor_data["matrix"], weights_short, monitor_data["types"])


def test_topsis_weights_too_long(monitor_data):
    topsis = TOPSIS()
    weights_long = [0.24, 0.17, 0.16, 0.03, 0.26, 0.1, 0.04]
    with pytest.raises(ValueError):
        topsis.rank(monitor_data["matrix"], weights_long, monitor_data["types"])
