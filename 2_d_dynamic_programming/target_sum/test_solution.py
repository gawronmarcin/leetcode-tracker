import pytest
from solution import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 1, 1, 1, 1], 3, 5),

        ([1], 1, 1),

        ([2, 2, 2], 2, 3),

        ([1, 1], -2, 1),

        ([1, 2, 3], 10, 0),

        ([0, 1], 1, 2),
    ]
)
def test_find_target_sum_ways(nums, target, expected):
    sol = Solution()
    assert sol.findTargetSumWays(nums, target) == expected