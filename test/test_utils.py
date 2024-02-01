import pytest

from utils import result_iter_for_multiple_dices


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
