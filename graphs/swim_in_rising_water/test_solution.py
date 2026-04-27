import pytest
from solution import Solution


class TestSolution:
    @pytest.fixture
    def sol(self):
        return Solution()

    @pytest.mark.parametrize("grid, expected", [
        (
                [[0, 1],
                 [2, 3]],
                3
        ),

        (
                [[0, 1, 2, 3, 4],
                 [24, 23, 22, 21, 5],
                 [12, 13, 14, 15, 16],
                 [11, 17, 18, 19, 20],
                 [10, 9, 8, 7, 6]],
                16
        ),

        (
                [[0]],
                0
        ),

        (
                [[10, 1],
                 [2, 3]],
                10
        ),

        (
                [[0, 10, 10],
                 [1, 2, 10],
                 [10, 3, 4]],
                4
        )
    ])
    def test_swimInWater(self, sol, grid, expected):
        assert sol.swimInWater(grid) == expected