import pytest
from solution import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, -3, 4], 4),
    ([-2, -1], 2),

    ([-2], -2),
    ([0], 0),
    ([5], 5),

    ([-2, 0, -1], 0),
    ([0, 2, 0], 2),
    ([2, -5, 0, -2, -4, 3], 24),

    ([-2, -3, 7], 42),
    ([-2, 3, -4], 24),
    ([-1, -2, -3], 6),
    ([-1, -2, -3, -4], 24),

    ([-2, 3, -2, 4, -2], 48)
])
def test_maxProduct(nums, expected):
    sol = Solution()
    assert sol.maxProduct(nums) == expected