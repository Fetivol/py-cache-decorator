from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_values = {}

    def wrapper(*args, **kwargs) -> Any:

        if args not in cache_values:
            cache_values[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_values[args]

    return wrapper
