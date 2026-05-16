import pytest
from solution import Solution

@pytest.mark.parametrize("amount, coins, expected", [
    (5, [1, 2, 5], 4),
    (3, [2], 0),
    (0, [7], 1),
    (10, [10], 1)
])
def test_change(amount, coins, expected):
    sol = Solution()
    assert sol.change(amount, coins) == expected