import pytest
from solution import Solution

@pytest.mark.parametrize("input_s, expected", [
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a", "c"]),
    ("racecar", ["racecar"]),
    ("abbcccbbb", ["bbcccbb"]),
    ("", [""]),
    ("aaaa", ["aaaa"]),
])
def test_solve(input_s, expected):
    sol = Solution()
    assert sol.longestPalindrome(input_s) in expected