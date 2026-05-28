import pytest
from solution import Solution

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 1, 5, 8], 167),
        ([1, 5], 10),
        ([2, 3], 9),
        ([7], 7),
        ([], 0)
    ]
)
def test_solve(nums, expected):
    sol = Solution()
    assert sol.maxCoins(nums) == expected