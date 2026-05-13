import pytest
from solution import Solution

@pytest.mark.parametrize("m, n, expected", [
    (3, 6, 21),
    (3, 2, 3),
    (3, 7, 28),
    (1, 1, 1),
    (1, 10, 1),
    (10, 1, 1),
])
def test_uniquePaths(m, n, expected):
    sol = Solution()
    assert sol.uniquePaths(m, n) == expected