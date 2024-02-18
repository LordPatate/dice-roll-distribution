from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def create_fig_from_distribution(distribution: dict) -> Figure:
    x, y = list(zip(*distribution.items()))
    ax: Axes
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel("Roll result")
    ax.set_ylabel("Probability")
    return fig
