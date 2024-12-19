import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    This function loads a CSV file from the given path, prints its dimensions,
    and returns its content as a pandas DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame | None:
        The CSV file's content as a pandas DataFrame if successfully loaded,
        None if there is an error during loading or if the file is not a CSV.
    """
    try:
        assert path.lower().endswith((".csv")), "File must be .csv"
        file = pd.read_csv(path)

        assert file is not None, "Failed to load the dataset from the file"
        print(f"Loading dataset of dimensions {file.shape}")
        return file

    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        return None
