from typing import Callable, Tuple

import numpy as np
from joblib import Parallel, delayed


def simulate(algorithm: Callable[[np.ndarray], np.ndarray], array_size: int, num_of_runs: int, n_jobs: int = 4) -> np.ndarray:
    result = Parallel(n_jobs=n_jobs)(delayed(algorithm)(np.arange(array_size)) for _ in range(num_of_runs))
    return np.stack(result)


def distribution(simulation_results: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    num_runs, array_size = simulation_results.shape
    actual_distr = np.zeros((array_size, array_size))
    for pos in range(array_size):
        element_distr = simulation_results[:, pos]
        values, counts = np.unique(element_distr, return_counts=True)
        actual_distr[pos, values] = counts
    actual_distr = actual_distr / num_runs
    uniform_distr = np.ones_like(actual_distr) / array_size
    return actual_distr, uniform_distr


def average_cosine_similarity(actual_distr: np.ndarray, target_distr: np.ndarray) -> float:
    p = target_distr
    q = actual_distr
    magnitude_p = np.sqrt(np.sum(p * p, axis=1))
    magnitude_q = np.sqrt(np.sum(q * q, axis=1))
    cosine_sim = np.sum(p * q, axis=1) / (magnitude_p * magnitude_q)
    return np.average(cosine_sim)


def euclidian_distance(actual_distr: np.ndarray, target_distr: np.ndarray) -> float:
    return np.sqrt(np.sum(np.power(actual_distr - target_distr, 2)))
