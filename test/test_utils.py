import itertools
import numpy as np
import pytest

from utils import cartesian_product, result_iter_for_multiple_dices


@pytest.mark.parametrize(
    "number_of_dices, number_of_sides, output",
    (
        (1, 6, [1, 2, 3, 4, 5, 6]),
        (2, 4, [2, 3, 4, 5,
                3, 4, 5, 6,
                4, 5, 6, 7,
                5, 6, 7, 8]),
    )
)
def test_result_list(number_of_dices, number_of_sides, output):
    assert list(result_iter_for_multiple_dices(number_of_dices, number_of_sides)) == output


@pytest.mark.parametrize(
    "number_of_arrays, array_size",
    ((3, 2), (2, 3), (1, 3))
)
def test_cartesian_product(number_of_arrays, array_size):
    arrays = [
        np.array(range(10*i, 10*i + array_size))
        for i in range(number_of_arrays)
    ]
    reference = [list(item) for item in itertools.product(*arrays)]

    assert cartesian_product(*arrays).tolist() == reference
