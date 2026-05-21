import pytest
from solution import Solution

@pytest.mark.parametrize("matrix, expected", [
    ([[9,9,4],[6,6,8],[2,1,1]], 4),
    ([[3,4,5],[3,2,6],[2,2,1]], 4),
    ([[1]], 1),
    ([[1,2]], 2),
    ([[2,1]], 2),
    ([[1],[2]], 2),
    ([[2],[1]], 2),
    ([[1,2,3],[6,5,4],[7,8,9]], 9),
    ([[1,2,3],[8,9,4],[7,6,5]], 9),
    ([[9,8,7],[2,1,6],[3,4,5]], 9),
    ([[1,1,1],[1,1,1],[1,1,1]], 1),
    ([[1,2,3],[3,2,1],[1,2,3]], 3),
    ([], 0),
    ([[]], 0)
])
def test_longestIncreasingPath(matrix, expected):
    sol = Solution()
    assert sol.longestIncreasingPath(matrix) == expected