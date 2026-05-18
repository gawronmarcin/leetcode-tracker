import pytest
from solution import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, -3, 4, -2, 2, 1, -1, 4], 8),
        ([-1], -1),

        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),

        ([-5, -2, -9, -1], -1),

        ([1, 2, 3, 4, 5], 15),

        ([5], 5),
        ([0], 0),

        ([10, -50, 20], 20),
        ([10, -2, 20], 28)
    ]
)
def test_solve(nums, expected):
    sol = Solution()
    assert sol.maxSubArray(nums) == expected