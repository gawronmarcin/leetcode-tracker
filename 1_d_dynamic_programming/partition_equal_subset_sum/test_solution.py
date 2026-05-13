import pytest
from solution import Solution


def test_solve():
    sol = Solution()

    assert sol.canPartition([1, 5, 11, 5]) is True

    assert sol.canPartition([1, 2, 3, 5]) is False

    assert sol.canPartition([1, 2, 3, 4]) is True

    assert sol.canPartition([1, 2, 5]) is False

    assert sol.canPartition([2, 2, 2, 2]) is True