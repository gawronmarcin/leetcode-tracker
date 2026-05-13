import pytest
from solution import Solution

def test_solve_simple_path_within_limit():
    sol = Solution()
    edges = [(1, 2, 10), (2, 3, 12)]
    queries = [(1, 3)]
    assert sol.solve(3, 2, edges, queries) == ["TAK"]

def test_solve_path_exceeds_limit():
    sol = Solution()
    edges = [(1, 2, 10), (2, 3, 12)]
    queries = [(1, 3)]
    assert sol.solve(3, 1, edges, queries) == ["NIE"]

def test_solve_disconnected_components():
    sol = Solution()
    edges = [(1, 2, 5), (3, 4, 10)]
    queries = [(1, 2), (1, 3), (3, 4)]
    assert sol.solve(4, 5, edges, queries) == ["TAK", "NIE", "TAK"]

def test_solve_alternative_routes():
    sol = Solution()
    edges = [(1, 2, 10), (2, 4, 15), (1, 3, 10), (3, 4, 11)]
    queries = [(1, 4)]
    assert sol.solve(4, 2, edges, queries) == ["TAK"]

def test_solve_no_edges():
    sol = Solution()
    edges = []
    queries = [(1, 2)]
    assert sol.solve(2, 5, edges, queries) == ["NIE"]

def test_solve_same_vertex():
    sol = Solution()
    edges = [(1, 2, 10)]
    queries = [(1, 1)]
    assert sol.solve(2, 5, edges, queries) == ["TAK"]