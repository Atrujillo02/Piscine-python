from typing import Any


def ft_mean(numbers: list) -> float:
    """
    Calculates the mean (average) of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The mean of the numbers.
    """
    return sum(numbers) / len(numbers)


def ft_median(numbers: list) -> float:
    """
    Calculates the median of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The median of the numbers.
    """
    len_num = len(numbers)
    numbers.sort()
    if len_num % 2 == 0:
        result = numbers[len_num // 2 - 1] + numbers[len_num // 2]
    else:
        result = numbers[len_num // 2]

    return result


def ft_quartile(numbers: list) -> list:
    """
    Calculates the first and third quartiles (Q1 and Q3) of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        list: A list containing Q1 and Q3 as float values.
    """
    len_num = len(numbers)
    numbers.sort()
    return [float(numbers[len_num // 4]), float(numbers[len_num * 3 // 4])]


def ft_var(numbers: list) -> float:
    """
    Calculates the variance of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The variance of the numbers.
    """
    len_num = len(numbers)
    mean = ft_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len_num


def ft_std(numbers: list) -> float:
    """
    Calculates the standard deviation of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The standard deviation of the numbers.
    """
    std = ft_var(numbers) ** 0.5
    return std


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculates various statistics for a list of numbers.

    Valid statistics include: mean, median, quartile, std, var.
    Any other statistics will be ignored.

    Args:
        *args: The numbers for which to calculate statistics.
        **kwargs: Keywords indicating which statistics to calculate.

    Returns:
        None: Prints the results or an error message.
    """
    numbers = list(args)
    valid_operations = list(filter(
        lambda x: x in ['mean', 'median', 'quartile', 'std', 'var'],
        kwargs.values()
    ))

    if not valid_operations:
        return

    valid_numbers = [x for x in numbers
                     if isinstance(x, (int, float)) and x >= 0]

    if len(numbers) != len(valid_numbers):
        print("ERROR")

    for x in valid_operations:
        func = globals().get(f"ft_{x}")
        if func and len(valid_numbers) > 0:
            print(f"{x} : {func(valid_numbers)}")
        else:
            print("ERROR")
