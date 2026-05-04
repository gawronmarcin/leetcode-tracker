import pytest
from solution import Solution

@pytest.mark.parametrize("cost, expected", [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([1, 2, 3], 2),
    ([0, 0, 0, 1], 0)
])
def test_minCostClimbingStairs(cost, expected):
    sol = Solution()
    assert sol.minCostClimbingStairs(cost) == expected