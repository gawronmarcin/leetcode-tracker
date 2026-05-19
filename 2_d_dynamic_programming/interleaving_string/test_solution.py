import pytest
from solution import Solution


@pytest.mark.parametrize(
    "s1, s2, s3, expected",
    [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),

        ("", "", "", True),
        ("a", "", "c", False),
        ("", "abc", "abc", True),
        ("abc", "", "abc", True),

        ("a", "b", "a", False),
        ("abc", "def", "abcdefg", False),

        ("a", "b", "ab", True),
        ("a", "b", "ba", True),
        ("ab", "bc", "babc", True)
    ]
)
def test_isInterleave(s1, s2, s3, expected):
    sol = Solution()
    assert sol.isInterleave(s1, s2, s3) == expected