import pytest
from solution import Solution

@pytest.mark.parametrize(
    "P, n, A, B, C, leaves, expected",
    [
        (10, 3, 1, 0, 0, [(0, 50), (4, 10), (7, 10)], 2),
        (10, 2, 1, 0, 0, [(0, 10), (5, 0)], -1),
        (10, 2, 1, 0, 0, [(0, 200), (5, 10)], 1),
        (5, 4, 0, 1, 1, [(0, 5), (1, 2), (2, 2), (3, 2)], 2)
    ]
)
def test_solve(P, n, A, B, C, leaves, expected):
    sol = Solution()
    assert sol.solve(P, n, A, B, C, leaves) == expected