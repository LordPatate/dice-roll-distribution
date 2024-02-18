from argparse import ArgumentParser
from pathlib import Path
from src.render import create_fig_from_distribution
from src.utils import probability_distribution


DICE_TYPES = {
    4, 6, 8, 10, 12
}
OUTPUT_DIR = "figures"


def main(number_of_dices):
    for number_of_sides in DICE_TYPES:
        distribution = probability_distribution(number_of_dices, number_of_sides)
        fig = create_fig_from_distribution(distribution)
        fig.savefig(
            Path(
                OUTPUT_DIR,
                f"{number_of_dices}d{number_of_sides}",
            ),
        )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "dices",
        type=int,
        help="Number of dices to roll. Note: complexity grows exponentially, stay below 8."
    )
    args = parser.parse_args()
    main(args.dices)
