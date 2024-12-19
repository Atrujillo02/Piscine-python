import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Plots a scatterplot showing the relationship between
    GDP per capita (income) and life expectancy in 1900.
    """
    life_data = load("life_expectancy_years.csv")
    gdp_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    gdp_1900 = gdp_data['1900']
    life_expectancy_1900 = life_data['1900']

    plt.figure(figsize=(15, 10))
    plt.scatter(gdp_1900, life_expectancy_1900)
    plt.title("1900")

    plt.xlabel("Gross domestic product")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])

    plt.ylabel("Life expectancy")

    canvas = plt.gcf().canvas
    canvas.manager.set_window_title('Life in relation to the income of 1900')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
