import pytest
from solution import Solution


@pytest.mark.parametrize("coins, amount, expected", [
    ([1, 5, 10], 12, 3),
    ([2], 3, -1),
    ([1], 0, 0),

    ([2], 1, -1),
    ([1, 2, 5], 11, 3),
    ([2, 5, 10, 1], 27, 4),
    ([186, 419, 83, 408], 6249, 20)
])
def test_coin_change(coins, amount, expected):
    sol = Solution()
    assert sol.coinChange(coins, amount) == expected