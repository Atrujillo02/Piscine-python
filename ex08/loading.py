import shutil

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

    for i, item in enumerate(lst, start=1):
        terminal_width = shutil.get_terminal_size().columns

        info_width = len(f" 100%| | {lst_len}/{lst_len}")
        bar_len = max(1, terminal_width - info_width)

        progress = i / lst_len
        bar_fill = int(progress * bar_len)
        bar = "█" * bar_fill + " " * (bar_len - bar_fill)

        print(
            f"\r{int(progress * 100):3}%|[{bar}]| {i}/{lst_len}",
            end="",
        )

        yield item

    print()

from time import sleep
from tqdm import tqdm
from loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

for elem in tqdm(range(333)):
    sleep(0.005)
print()