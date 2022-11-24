
from typing import Optional

import numpy as np


def fisher_yates_shuffle(array: np.ndarray) -> np.ndarray:
    res = np.copy(array)
    for i in range(len(array)):
        new_i = np.random.randint(0, i + 1, size=1)
        res[i], res[new_i] = res[new_i], res[i]
    return res


def wrong_sequential_swap_shuffle(array: np.ndarray) -> np.ndarray:
    res = np.copy(array)
    for i in range(len(array)):
        new_i = np.random.randint(0, len(array), size=1)
        res[i], res[new_i] = res[new_i], res[i]
    return res


def wrong_random_pairs_shuffle(array: np.ndarray, swap_num: Optional[int] = None) -> np.ndarray:
    res = np.copy(array)
    swap_num = swap_num or len(array)
    for _ in range(swap_num):
        new_i, new_j = np.random.randint(0, len(array), size=2)
        res[[new_i, new_j]] = res[[new_j, new_i]]
    return res
