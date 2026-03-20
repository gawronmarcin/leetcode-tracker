import pytest
from solution import Solution


class TestFindKthLargest:

    @pytest.fixture
    def sol(self):
        return Solution()

    @pytest.mark.parametrize("nums, k, expected", [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),

        ([1], 1, 1),
        ([2, 1], 1, 2),
        ([2, 1], 2, 1),

        ([7, 8, 9, 10], 1, 10),
        ([7, 8, 9, 10], 4, 7),

        ([-1, -2, -3, -4], 2, -2),
        ([-5, -5, -5, -5], 3, -5),
        ([0, 0, 0, 0], 2, 0),

        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 7)
    ])
    def test_find_kth_largest(self, sol, nums, k, expected):
        assert sol.findKthLargest(nums, k) == expected