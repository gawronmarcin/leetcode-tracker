import pytest
from solution import Solution

class TestMergeIntervals:

    @pytest.fixture
    def sol(self):
        return Solution()

    @pytest.mark.parametrize("intervals, expected", [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),

        ([[1, 4], [4, 5]], [[1, 5]]),

        ([[1, 4], [2, 3]], [[1, 4]]),

        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),

        ([[8, 10], [1, 3], [15, 18], [2, 6]], [[1, 6], [8, 10], [15, 18]]),

        ([[1, 4], [1, 4], [1, 4]], [[1, 4]]),

        ([[1, 5]], [[1, 5]]),
    ])
    def test_merge(self, sol, intervals, expected):
        assert sol.merge(intervals) == expected