import functools
import numpy as np
import itertools


@functools.cache
def probability_distribution(number_of_dices, number_of_sides):
    results = _result_list_for_multiple_dices(number_of_dices, number_of_sides)
    frequencies = _frequency_map(results)
    number_of_cases = number_of_sides**number_of_dices
    return {
        result: frequency / number_of_cases
        for result, frequency in frequencies.items()
    }


def _result_list_for_multiple_dices(numbers_of_dices, number_of_sides):
    result_list_for_one_dice = np.arange(1, number_of_sides + 1)
    cartesian_product_of_results = itertools.product(
        *(
            result_list_for_one_dice
            for _ in range(numbers_of_dices)
        )
    )
    return [
        sum(results)
        for results in cartesian_product_of_results
    ]


def _frequency_map(result_list):
    freq_map = dict()
    for result in result_list:
        freq_map[result] = freq_map.get(result, 0) + 1
    return freq_map
