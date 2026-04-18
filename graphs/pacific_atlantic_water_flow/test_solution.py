import pytest
from solution import Solution


@pytest.mark.parametrize("heights, expected", [
    (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4]
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    ),

    (
            [[1]],
            [[0, 0]]
    ),

    (
            [[2, 2], [2, 2]],
            [[0, 0], [0, 1], [1, 0], [1, 1]]
    ),

    (
            [
                [1, 1, 1],
                [1, 5, 1],
                [1, 1, 1]
            ],
            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    ),

    (
            [[1, 2, 3]],
            [[0, 0], [0, 1], [0, 2]]
    )
])
def test_pacificAtlantic(heights, expected):
    sol = Solution()
    result = sol.pacificAtlantic(heights)

    assert sorted(result) == sorted(expected)

