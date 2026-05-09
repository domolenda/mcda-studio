import numpy as np

from app.services.comparison import calc_rw, calc_ws


def test_calc_rw():
    rank_x = np.array([9, 2, 1, 3, 8, 6, 7, 4, 5])
    rank_y = np.array([9, 2, 3, 1, 8, 6, 4, 7, 5])
    rw = calc_rw(rank_x, rank_y)
    assert isinstance(rw, float)
    assert rw == 0.7583


def test_calc_rw_identical_rankings():
    rank = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert calc_rw(rank, rank) == 1.0


def test_calc_ws():
    rank_x = np.array([9, 2, 1, 3, 8, 6, 7, 4, 5])
    rank_y = np.array([9, 2, 3, 1, 8, 6, 4, 7, 5])
    ws = calc_ws(rank_x, rank_y)
    assert isinstance(ws, float)
    assert ws == 0.7919


def test_calc_ws_identical_rankings():
    rank = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert calc_ws(rank, rank) == 1.0
