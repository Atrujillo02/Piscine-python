
def ft_filter(function, iterable):
    """
    This function filters the elements of
    an iterable based on the given function.

    Parameters:
        function: The function to apply to each element.
        iterable: The iterable (e.g., list, tuple) to filter.

    Returns:
        list: A list of elements for which the function returns True.
    """
    return [element for element in iterable if function(element)]
