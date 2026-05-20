import pytest
from solution import Solution

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 0, 1, 0], True),
        ([1, 2, 1, 0, 1], False),
        ([0], True),
        ([2, 0], True),
        ([0, 2, 3], False),
        ([3, 2, 1, 0, 4], False),
        ([2, 5, 0, 0], True),
    ]
)
def test_canJump(nums, expected):
    sol = Solution()
    assert sol.canJump(nums) == expected