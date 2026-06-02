import pytest
from solution import Solution


@pytest.mark.parametrize(
    "s, p, expected",
    [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "", True),
        ("", "a*", True),
        ("a", "ab*", True),
        ("bbbba", ".*a*a", True),
        ("ab", ".b", True),
    ],
)
def test_is_match(s, p, expected):
    sol = Solution()
    assert sol.isMatch(s, p) == expected