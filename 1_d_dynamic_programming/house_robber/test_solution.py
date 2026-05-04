import pytest
from solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([0], 0),
    ([2, 1], 2),
    ([2, 1, 1, 2], 4),
    ([10, 2, 2, 100], 110)
])
def test_rob(nums, expected):
    sol = Solution()
    assert sol.rob(nums) == expected