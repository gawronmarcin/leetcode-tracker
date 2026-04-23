import pytest
from solution import Solution


@pytest.mark.parametrize("times, n, k, expected", [
    ([[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], 4, 1, 3),

    ([[1, 2, 1], [2, 3, 1]], 3, 2, -1),

    ([[1, 2, 1]], 2, 1, 1),

    ([[1, 2, 1]], 2, 2, -1),

    ([[1, 2, 5], [1, 3, 1], [3, 2, 1]], 3, 1, 2),

    ([], 1, 1, 0)
])
def test_network_delay_time(times, n, k, expected):
    sol = Solution()
    assert sol.networkDelayTime(times, n, k) == expected


def test_single_case_template():
    sol = Solution()
    times = [[1, 2, 1]]
    n = 2
    k = 1
    assert sol.networkDelayTime(times, n, k) == 1