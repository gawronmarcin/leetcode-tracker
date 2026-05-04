import pytest
from solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
    ([0], 0),
    ([5], 5),
    ([1, 2], 2),
    ([200, 3, 140, 20, 10], 340)
])
def test_rob(nums, expected):
    sol = Solution()
    assert sol.rob(nums) == expected