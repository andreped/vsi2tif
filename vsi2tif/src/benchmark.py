from functools import wraps
from time import perf_counter


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        result = func(*args, **kwargs)
        time_duration = perf_counter() - time_start
        print(f"Processing took {time_duration:.3f} seconds")
        return result

    return wrapper
