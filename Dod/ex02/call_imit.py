from typing import Any, Callable


def callLimit(limit: int) -> Callable:
    """
    A decorator factory that restricts the number of times
    a function can be called.

    Args:
        limit (int): The maximum number of times
        the decorated function can be called.

    Returns:
        Callable: A decorator that limits the calls to the specified function.
    """
    i = 0

    def callLimiter(function: Callable) -> Callable:
        def limit_function(*args: Any, **kwds: Any):
            nonlocal i
            if i >= limit:
                print(f"Error: {function.__name__} called too many times")
                return
            i += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter
