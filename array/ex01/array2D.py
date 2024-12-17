import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
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
    family_np = np.array(family)

    assert family_np.ndim == 2, "Array is not 2D"
    print(f"My shape is : {family_np.shape}")

    nw_family = family_np[start:end]
    print(f"My new shape is : {nw_family.shape}")

    return nw_family.tolist()
