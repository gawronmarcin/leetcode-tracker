import pytest
from solution import Solution

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([0], 0),
        ([2, 1], 1),
        ([3, 4, 1, 1, 1, 1, 1], 3),
        ([5, 1, 2, 3, 4, 1, 1, 1, 1], 2),
        ([1, 2, 1, 1, 1], 3),
        ([4, 3, 2, 1, 1], 1),
        ([1, 1, 1, 1], 3)
    ]
)
def test_jump(nums, expected):
    sol = Solution()
    assert sol.jump(nums) == expected