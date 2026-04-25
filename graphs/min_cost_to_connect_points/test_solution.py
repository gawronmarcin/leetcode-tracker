import pytest
from solution import Solution


@pytest.mark.parametrize(
    "points, expected_cost",
    [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),

        ([[3, 12], [-2, 5], [-4, 1]], 18),

        ([[0, 0]], 0),

        ([[0, 0], [1, 1]], 2),

        ([[0, 0], [0, 1], [0, 2], [0, 3]], 3),

        ([[1, 1], [1, 1], [1, 1]], 0)
    ]
)
def test_minCostConnectPoints(points, expected_cost):
    sol = Solution()
    assert sol.minCostConnectPoints(points) == expected_cost

