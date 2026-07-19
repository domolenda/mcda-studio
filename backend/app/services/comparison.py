from itertools import combinations

import numpy as np

from app.schemas.comparison import ComparisonResponse, MethodConfig
from app.services.methods.registry import get_method


def calc_rw(rank_x: np.ndarray, rank_y: np.ndarray) -> float:
    n = len(rank_x)
    d_squared = (rank_x - rank_y) ** 2
    weights = (n - rank_x + 1) + (n - rank_y + 1)
    rw = 1 - (6 * np.sum(d_squared * weights)) / (n**4 + n**3 - n**2 - n)
    return float(round(rw, 4))


def calc_ws(rank_x: np.ndarray, rank_y: np.ndarray) -> float:
    n = len(rank_x)
    exp_weights = 2.0 ** (-rank_x)
    denominators = np.maximum(np.abs(1 - rank_x), np.abs(n - rank_x))
    ws = 1 - np.sum(exp_weights * np.abs(rank_x - rank_y) / denominators)
    return float(round(ws, 4))


def compare_methods(
    matrix: list[list[float]],
    weights: list[float],
    types: list[int],
    methods_config: list[MethodConfig],
) -> ComparisonResponse:
    if len(methods_config) < 2:
        raise ValueError("At least 2 methods are required for comparison")

    rankings = {}
    for method_config in methods_config:
        method_class = get_method(method_config.name)
        params = {p.name: p.value for p in method_config.params}
        method_instance = method_class()
        ranking = method_instance.rank(matrix, weights, types, **params)
        rankings[method_config.id] = ranking

    correlations = []
    for method_a, method_b in combinations(rankings.keys(), 2):
        rank_a = np.array(rankings[method_a])
        rank_b = np.array(rankings[method_b])
        rw = calc_rw(rank_a, rank_b)
        ws = calc_ws(rank_a, rank_b)
        corr_dict = {
            "method_a": method_a,
            "method_b": method_b,
            "rw": rw,
            "ws": ws,
        }
        correlations.append(corr_dict)
    return ComparisonResponse(rankings=rankings, correlations=correlations)
