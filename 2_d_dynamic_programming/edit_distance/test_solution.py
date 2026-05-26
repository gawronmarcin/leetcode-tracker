import pytest
from solution import Solution

@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "", 0),
        ("a", "", 1),
        ("", "a", 1),
        ("abc", "abc", 0),
        ("kitten", "sitting", 3),
        ("flaw", "lawn", 2),
        ("a", "b", 1)
    ]
)
def test_minDistance(word1, word2, expected):
    sol = Solution()
    assert sol.minDistance(word1, word2) == expected