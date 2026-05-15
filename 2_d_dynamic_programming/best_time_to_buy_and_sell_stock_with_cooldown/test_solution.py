import pytest
from solution import Solution

@pytest.mark.parametrize("prices, expected", [
    ([1, 2, 3, 0, 2], 3),
    ([], 0),
    ([1], 0),
    ([5, 4, 3, 2, 1], 0),
    ([1, 2, 3, 4, 5], 4),
    ([1, 5], 4),
    ([5, 1], 0),
])
def test_maxProfit(prices, expected):
    sol = Solution()
    assert sol.maxProfit(prices) == expected