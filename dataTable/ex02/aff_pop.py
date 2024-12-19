import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def parser_number(number: str) -> float:
    """
    Converts a string with suffixes 'M' (millions) or 'k' (thousands)
    into a float value,
    or returns the original number as a float if no suffix is present.
    """
    if number.endswith("M"):
        return float(number[:-1]) * 1_000_000
    if number.endswith("k"):
        return float(number[:-1]) * 1_000
    return float(number)


def main():
    """
    Reads population data from a CSV file.
    Plots a comparison of projections for Spain and France.
    """
    file = load("population_total.csv")

    parser_num = np.vectorize(parser_number)

    years = np.array(file.columns[1:].astype(int))
    spain_row = parser_num(file[file["country"] == "Spain"].values[0][1:])
    france_row = parser_num(file[file["country"] == "France"].values[0][1:])

    plt.figure(figsize=(10, 6))
    canvas = plt.gcf().canvas
    canvas.manager.set_window_title('Population Projections')
    plt.title('Population Projections')

    plt.plot(years, spain_row, label="Spain", color="blue")
    plt.plot(years, france_row, label="France", color="green")

    plt.xlabel('Year')
    plt.xticks(range(1800, 2041, 40))
    plt.xlim(1790, 2050)

    plt.ylabel('Population')
    y_ticks = range(20_000_000, 80_000_000, 20_000_000)
    plt.yticks(
        y_ticks,
        ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks]
    )
    plt.ylim(0, 80_000_000, 20_000_000)

    plt.legend(loc='lower right')
    plt.show()


if __name__ == "__main__":
    main()
