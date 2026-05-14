import pytest
from solution import Solution


@pytest.mark.parametrize(
    "queries, expected",
    [
        ([], []),
        ([0], [1]),

        ([1], [2]),
        ([2], [7]),
        ([3], [22]),
        ([4], [4]),
        ([5], [27]),


        ([1, 2, 3, 4, 5], [2, 7, 22, 4, 27]),


        ([4, 1, 3, 2], [4, 2, 22, 7]),

        ([2, 2, 2], [7, 7, 7]),
    ]
)
def test_solve(queries, expected):
    sol = Solution()
    assert sol.solve(queries) == expected