import pytest
from solution import Solution

@pytest.mark.parametrize("hand, groupSize, expected", [
    ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
    ([1, 2, 3, 4, 5], 4, False),
    ([1, 1, 2, 2, 3, 3], 2, False),
    ([1, 1, 2, 2, 3, 3], 3, True),
    ([8, 10, 12], 3, False),
    ([5], 1, True)
])
def test_solve(hand, groupSize, expected):
    sol = Solution()
    assert sol.isNStraightHand(hand, groupSize) == expected