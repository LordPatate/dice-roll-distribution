from collections import Counter

import numpy as np


def probability_distribution(number_of_dices, number_of_sides):
    results = result_iter_for_multiple_dices(number_of_dices, number_of_sides)
    frequencies = Counter(results)
    number_of_cases = number_of_sides**number_of_dices
    return {
        result: frequency / number_of_cases
        for result, frequency in frequencies.items()
    }


def result_iter_for_multiple_dices(number_of_dices, number_of_sides):
    result_list_for_one_dice = np.arange(1, number_of_sides + 1)
    cartesian_product_of_results = cartesian_product(
        *([result_list_for_one_dice] * number_of_dices)
    )
    return np.sum(cartesian_product_of_results, axis=1)


def best_of_multiple_dices(number_of_dices, number_of_sides):
    result_list_for_one_dice = np.arange(1, number_of_sides + 1)
    cartesian_product_of_results = cartesian_product(
        *([result_list_for_one_dice] * number_of_dices)
    )
    return np.max(cartesian_product_of_results, axis=1)


def cartesian_product(*arrays):
    """Alternative to itertools.product.
    
    Copied from senderle's answer on
    https://stackoverflow.com/questions/11144513/cartesian-product-of-x-and-y-array-points-into-single-array-of-2d-points
    """
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)
