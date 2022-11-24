
import time
from typing import Callable, Any, List, Dict


def time_execution(fun: Callable, profiles: List[Dict[Any, Any]]) -> List[float]:
    results = []
    for profile in profiles:
        tic = time.perf_counter()
        _ = fun(**profile)
        toc = time.perf_counter()
        # add repeats to get more accurate results
        results.append(toc - tic)
        return results
