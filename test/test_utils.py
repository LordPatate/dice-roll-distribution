import pytest

from utils import frequency_map, result_iter_for_multiple_dices


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
    "number_of_dices, number_of_sides, output",
    (
        (1, 6, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        (2, 4, {2: 1, 3: 2, 4: 3, 5: 4, 6: 3, 7: 2, 8: 1}),
    )
)
def test_freq_map(number_of_dices, number_of_sides, output):
    results = result_iter_for_multiple_dices(number_of_dices, number_of_sides)
    assert frequency_map(results) == output
