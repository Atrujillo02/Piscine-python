import numpy as np


def give_bmi(height: list[int | float],
            weight: list[int | float]) -> list[int | float]:
    """
    This function makes a new array starting in start index
    and finishing in end index.

    Args:
        family (list): A 2D list representing the array.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        list: A new 2D list that is a slice of the original array.
    """
    heights_np = np.array(height)
    weights_np = np.array(weight)


    assert heights_np.size == weights_np.size, "Lists are not of equal length."
    assert (
        np.issubdtype(heights_np.dtype, np.integer)
        or np.issubdtype(heights_np.dtype, np.floating)
    ), "The list has values that are neither integers nor floats."

    assert (
        np.issubdtype(weights_np.dtype, np.integer)
        or np.issubdtype(weights_np.dtype, np.floating)
    ), "The list has values that are neither integers nor floats."

    return np.array(weights_np / (heights_np ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values exceed a given limit.
    
    Args:
        bmi (list[int | float]): List of BMI values (float or int).
        limit (int): Threshold to compare BMI values.
    
    Returns:
        list[bool]: A list of booleans: True if BMI > limit, otherwise False.
    """
    bmi_np = np.array(bmi)
    assert (
        np.issubdtype(bmi_np.dtype, np.integer)
        or np.issubdtype(bmi_np.dtype, np.floating)
    ), "The list have values that not are integer or float."
    return (bmi_np > limit).tolist()
