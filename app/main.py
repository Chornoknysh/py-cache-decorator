from typing import Callable, Any, Dict
from functools import wraps


def cache(func: Callable) -> Callable:
    store: Dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in store:
            print("Getting from cache")
            return store[args]
        print("Calculating new result")
        result = func(*args)
        store[args] = result
        return result

    return wrapper
