from collections import Counter
import functools
import numpy as np
import itertools


@functools.cache
def probability_distribution(number_of_dices, number_of_sides):
    results = result_iter_for_multiple_dices(number_of_dices, number_of_sides)
    frequencies = Counter(results)
    number_of_cases = number_of_sides**number_of_dices
    return {
        result: frequency / number_of_cases
        for result, frequency in frequencies.items()
    }


def result_iter_for_multiple_dices(numbers_of_dices, number_of_sides):
    result_list_for_one_dice = np.arange(1, number_of_sides + 1)
    cartesian_product_of_results = itertools.product(
        *(
            result_list_for_one_dice
            for _ in range(numbers_of_dices)
        )
    )
    return (
        sum(results)
        for results in cartesian_product_of_results
    )
