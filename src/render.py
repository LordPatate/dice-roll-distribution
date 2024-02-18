import matplotlib.pyplot as plt

from src.utils import probability_distribution


def show_roll(number_of_dices, number_of_sides):
    distribution = probability_distribution(number_of_dices, number_of_sides)
    x, y = list(zip(*distribution.items()))
    _, ax = plt.subplots()
    ax.bar(x, y)
    plt.show()
