from argparse import ArgumentParser
from enum import Enum
from pathlib import Path
from src.render import create_fig_from_distribution
from src.utils import probability_distribution, best_of_multiple_dices, result_iter_for_multiple_dices


DICE_TYPES = {
    4, 6, 8, 10, 12
}
OUTPUT_DIR = "figures"


class AggregationMode(Enum):
    SUM = 0
    MAX = 1


def main(number_of_dices, sides=None, mode=AggregationMode.SUM):
    result_list_genarator = {
        AggregationMode.SUM: result_iter_for_multiple_dices,
        AggregationMode.MAX: best_of_multiple_dices,
    }
    dice_types = [sides] if sides else DICE_TYPES

    for number_of_sides in dice_types:
        distribution = probability_distribution(
            number_of_dices,
            number_of_sides,
            result_list_genarator[mode],
        )
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
        "number_of_dices",
        type=int,
        help="Number of dices to roll. Note: complexity grows exponentially, stay below 8."
    )
    parser.add_argument(
        "--sides",
        type=int,
        help="Will throw dices with that many sides instead of using the default dices."
    )
    parser.add_argument(
        "--best-of",
        action="store_const",
        const=AggregationMode.MAX,
        dest="mode",
        help="Keep the best result from dices rolled instead of adding results together."
    )
    args = parser.parse_args()
    main(**vars(args))
