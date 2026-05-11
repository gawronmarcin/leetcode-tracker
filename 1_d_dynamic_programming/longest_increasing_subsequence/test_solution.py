import pytest
from solution import Solution


class TestSolution:
    @pytest.fixture
    def sol(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        ([9, 1, 4, 2, 3, 3, 7], 4),
        ([0, 3, 1, 3, 2, 3], 4),

        ([], 0),
        ([10], 1),
        ([7, 7, 7, 7, 7], 1),
        ([5, 4, 3, 2, 1], 1),
        ([1, 2, 3, 4, 5], 5),

        ([-500, -100, 0, 200, 1000], 5),
        ([2, -1, 4, -5, 6, -7, 8], 4)
    ])
    def test_lengthOfLIS(self, sol, nums, expected):
        assert sol.lengthOfLIS(nums) == expected