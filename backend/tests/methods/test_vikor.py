import pytest

from app.services.methods.vikor import VIKOR


def test_vikor_rank(monitor_data):
    vikor = VIKOR()
    result = vikor.rank(
        monitor_data["matrix"], monitor_data["weights"], monitor_data["types"]
    )
    assert result == [8, 2, 1, 3, 6, 5, 9, 4, 7]


def test_vikor_invalid_weights(monitor_data):
    vikor = VIKOR()
    bad_weights = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    with pytest.raises(ValueError):
        vikor.rank(monitor_data["matrix"], bad_weights, monitor_data["types"])


def test_vikor_weights_too_short(monitor_data):
    vikor = VIKOR()
    weights_short = [0.24, 0.17, 0.16, 0.03, 0.38]
    with pytest.raises(ValueError):
        vikor.rank(monitor_data["matrix"], weights_short, monitor_data["types"])


def test_vikor_weights_too_long(monitor_data):
    vikor = VIKOR()
    weights_long = [0.24, 0.17, 0.16, 0.03, 0.26, 0.1, 0.04]
    with pytest.raises(ValueError):
        vikor.rank(monitor_data["matrix"], weights_long, monitor_data["types"])
