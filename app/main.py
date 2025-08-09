from typing import Callable, Any, Dict, Tuple
from functools import wraps


def cache(func: Callable) -> Callable:
    store: Dict[Tuple[Any, Tuple[Tuple[str, Any], ...]], Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Створюємо хешований ключ з args + впорядковані kwargs
        key = (args, tuple(sorted(kwargs.items())))

        if key in store:
            print("Getting from cache")
            return store[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        store[key] = result
        return result

    return wrapper
