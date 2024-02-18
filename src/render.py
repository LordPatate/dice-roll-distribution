import matplotlib.pyplot as plt


def create_fig_from_distribution(distribution: dict):
    x, y = list(zip(*distribution.items()))
    fig, ax = plt.subplots()
    ax.bar(x, y)
    return fig
