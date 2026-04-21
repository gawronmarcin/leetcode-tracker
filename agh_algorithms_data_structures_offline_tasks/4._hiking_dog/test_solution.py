import pytest
from solution import Solution


def test_solve_example_from_task():
    sol = Solution()
    n, m, k = 4, 5, 2
    edges = [
        [1, 2, 5],
        [1, 3, 2],
        [1, 4, 8],
        [2, 3, 2],
        [3, 4, 50]
    ]
    spots = [2, 4]

    expected = [
        [3, 1, 3, 2, 4],
        [2, 1, 4, 8]
    ]
    assert sol.solve(n, m, k, edges, spots) == expected


def test_solve_tie_breaker_shorter_path():
    sol = Solution()
    n, m, k = 5, 5, 1
    edges = [
        [1, 2, 2],
        [2, 3, 1],
        [3, 4, 5],
        [1, 5, 2],
        [5, 4, 5]
    ]
    spots = [4]

    # Oczekujemy trasy B, bo ma mniej schronisk
    expected = [
        [3, 1, 5, 4, 10]
    ]
    assert sol.solve(n, m, k, edges, spots) == expected


def test_solve_linear_graph():
    sol = Solution()
    n, m, k = 4, 3, 1
    edges = [
        [1, 2, 2],
        [2, 3, 3],
        [3, 4, 4]
    ]
    spots = [4]

    # 2 * 3 * 4 = 24
    expected = [
        [4, 1, 2, 3, 4, 24]
    ]
    assert sol.solve(n, m, k, edges, spots) == expected


def test_solve_direct_connection_is_best():
    sol = Solution()
    n, m, k = 3, 3, 1
    edges = [
        [1, 2, 100],
        [2, 3, 100],
        [1, 3, 5]
    ]
    spots = [3]

    expected = [
        [2, 1, 3, 5]
    ]
    assert sol.solve(n, m, k, edges, spots) == expected