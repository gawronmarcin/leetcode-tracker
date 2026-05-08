import pytest
from solution import Solution


@pytest.mark.parametrize("s, expected", [
    ("12", 2),
    ("226", 3),

    ("0", 0),
    ("06", 0),
    ("10", 1),
    ("30", 0),
    ("1001", 0),

    ("1123", 5),
    ("27", 1),
    ("1212", 5)
])
def test_numDecodings(s, expected):
    sol = Solution()
    assert sol.numDecodings(s) == expected