import pytest
from solution import Solution

@pytest.mark.parametrize("s, expected", [
    ("xyxxyzbzbbisl", [5, 5, 1, 1, 1]),
    ("ababcbacadefegdehijhklij", [9, 7, 8]),
    ("eccbbbbdec", [10]),
    ("a", [1]),
    ("abcdef", [1, 1, 1, 1, 1, 1]),
    ("aaaaaa", [6])
])
def test_solve(s, expected):
    sol = Solution()
    assert sol.partitionLabels(s) == expected