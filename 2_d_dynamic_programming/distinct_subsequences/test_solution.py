import pytest
from solution import Solution

@pytest.mark.parametrize("s, t, expected", [
    ("caaat", "cat", 3),
    ("xxyxy", "xy", 5),
    ("rabbbit", "rabbit", 3),
    ("a", "b", 0),
    ("a", "a", 1),
    ("abcde", "ace", 1)
])
def test_solve(s, t, expected):
    sol = Solution()
    assert sol.numDistinct(s, t) == expected