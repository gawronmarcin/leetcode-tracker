import pytest
from solution import Solution

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("(*)", True),
    ("(*))", True),
    (")(", False),
    ("*", True),
    (")*(", False),
    ("((*)", True),
    ("(((", False),
    ("**))", True),
    ("(*()", True),
    ("", True)
])
def test_checkValidString(s, expected):
    sol = Solution()
    assert sol.checkValidString(s) == expected