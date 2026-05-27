import pytest
from solution import Solution

@pytest.mark.parametrize(
    "triplets, target, expected",
    [
        ([[1, 2, 3], [7, 1, 1]], [7, 2, 3], True),
        ([[2, 5, 6], [1, 4, 4], [5, 7, 5]], [5, 4, 6], False),
        ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),
        ([[3, 4, 5], [4, 5, 6]], [3, 2, 5], False),
        ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], True)
    ]
)
def test_merge_triplets(triplets, target, expected):
    sol = Solution()
    assert sol.mergeTriplets(triplets, target) == expected