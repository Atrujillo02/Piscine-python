def ft_tqdm(lst: range) -> None:
    """
    This function mimics tqdm using the yield operator, with a dynamically
    resizing progress bar based on the terminal width.

    Parameters:
        lst (range): The range to iterate over.

    Returns:
        None
    """
    lst_len = len(lst)
    bar_len = 20

    for i, item in enumerate(lst, start=1):
        progress = i / lst_len
        bar_fill = int(progress * bar_len)
        bar = "█" * bar_fill + " " * (bar_len - bar_fill)

        print(
            f"\r{int(progress * 100):3}%|[{bar}]| {i}/{lst_len}",
            end="",
        )

        yield item

    print()
