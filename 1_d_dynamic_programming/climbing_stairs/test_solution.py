
import pytest
from solution import Solution

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (10, 89)
])
def test_climbStairs(n, expected):
    sol = Solution()
    assert sol.climbStairs(n) == expected