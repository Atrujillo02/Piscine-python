def square(x: int | float) -> int | float:
    """
    Calculates the square of the given number.

    Args:
        x (int | float): The number to be squared.

    Returns:
        int | float: The square of the given number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Calculates the power of the given number raised to itself.

    Args:
        x (int | float): The base number.

    Returns:
        int | float: The result of raising the number to the power of itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns an inner function that computes a result based on
    the provided function.
    The result of the inner function is influenced by a nonlocal counter.

    Args:
        x (int | float): The base number to be used in the function.
        function (function): The function to be applied (e.g., square or pow).

    Returns:
        object: The inner function.
    """
    i = 0

    def inner() -> float:
        """
        Computes the result of the provided function based
        on the current value of count.
        The variable `i` accumulates the result of the function.

        Returns:
            float: The computed result.
        """
        nonlocal i
        i = function(x if i == 0 else i)
        return i

    return inner
