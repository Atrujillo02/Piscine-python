import numpy as np


def ft_invert(array: np.array) -> np.array:
    """
    Given an image, return a new one with the colors inverted
    """
    return 255 - array.copy()


def ft_red(array: np.array) -> np.array:
    """
    Given an image, return a new one with a red mask
    """
    filtered = array.copy()
    filtered[:, :, 1] = 0
    filtered[:, :, 2] = 0
    return filtered.astype(np.uint8)


def ft_green(array: np.array) -> np.array:
    """
    Given an image, return a new one with a green mask
    """
    filtered = array.copy()
    filtered[:, :, 0] = 0
    filtered[:, :, 2] = 0
    return filtered.astype(np.uint8)


def ft_blue(array: np.array) -> np.array:
    """
    Given an image, return a new one with a blue mask
    """
    filtered = array.copy()
    filtered[:, :, 0] = 0
    filtered[:, :, 1] = 0
    return filtered.astype(np.uint8)


def ft_grey(array) -> np.array:
    """
    Given an image, return a new one in grayscale
    """
    filtered = array.copy()
    return (np.sum(filtered, axis=2) / 3).astype(np.uint8)
