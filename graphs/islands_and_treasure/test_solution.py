import pytest
from solution import Solution

INF = 2147483647

TEST_CASES = [
    (
        [
            [INF, -1,  0,  INF],
            [INF, INF, INF, -1],
            [INF, -1,  INF, -1],
            [  0, -1,  INF, INF]
        ],
        [
            [3, -1, 0,  1],
            [2,  2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3,  4]
        ]
    ),
    (
        [
            [0, -1],
            [INF, INF]
        ],
        [
            [0, -1],
            [1, 2]
        ]
    ),
    (
        [
            [0, -1, INF],
            [-1, -1, -1],
            [INF, INF, INF]
        ],
        [
            [0, -1, INF],
            [-1, -1, -1],
            [INF, INF, INF]
        ]
    )
]

@pytest.mark.parametrize("input_grid, expected", TEST_CASES)
def test_islandsAndTreasure(input_grid, expected):
    sol = Solution()
    sol.islandsAndTreasure(input_grid)
    assert input_grid == expected