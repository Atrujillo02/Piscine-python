import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Generates a plot of life expectancy projections
    for Spain based on data from a CSV file.
    """
    file = load("life_expectancy_years.csv")
    years = np.array(file.columns[1:])

    row = file[file["country"] == "Spain"]
    life = np.array(row.values[0][1:])

    plt.plot(years, life)

    plt.title('Spain Life Expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(years[::40])

    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 100, 10))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
