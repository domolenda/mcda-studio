import pytest

from app.services.methods.aras import ARAS


def test_aras_rank(monitor_data):
    aras = ARAS()
    result = aras.rank(
        monitor_data["matrix"], monitor_data["weights"], monitor_data["types"]
    )
    assert result == [9, 3, 5, 1, 8, 6, 2, 7, 4]


def test_aras_invalid_weights(monitor_data):
    aras = ARAS()
    bad_weights = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    with pytest.raises(ValueError):
        aras.rank(monitor_data["matrix"], bad_weights, monitor_data["types"])


def test_aras_weights_too_short(monitor_data):
    aras = ARAS()
    weights_short = [0.24, 0.17, 0.16, 0.03, 0.38]
    with pytest.raises(ValueError):
        aras.rank(monitor_data["matrix"], weights_short, monitor_data["types"])


def test_aras_weights_too_long(monitor_data):
    aras = ARAS()
    weights_long = [0.24, 0.17, 0.16, 0.03, 0.26, 0.1, 0.04]
    with pytest.raises(ValueError):
        aras.rank(monitor_data["matrix"], weights_long, monitor_data["types"])


def test_aras_different_normalization(monitor_data):
    aras = ARAS()
    result = aras.rank(
        monitor_data["matrix"],
        monitor_data["weights"],
        monitor_data["types"],
        normalization_method="linear",
    )
    assert result == [9, 4, 5, 1, 8, 7, 3, 6, 2]
    assert len(result) == len(monitor_data["matrix"])
