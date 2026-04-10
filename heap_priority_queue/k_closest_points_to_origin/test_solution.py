import pytest
from solution import Solution

def test_kClosest_single_point():
    sol = Solution()
    points = [[1, 3], [-2, 2]]
    k = 1
    expected = [[-2, 2]]
    # Używamy sorted(), bo kolejność wyników nie ma znaczenia
    assert sorted(sol.kClosest(points, k)) == sorted(expected)

def test_kClosest_multiple_points():
    sol = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    expected = [[3, 3], [-2, 4]]
    assert sorted(sol.kClosest(points, k)) == sorted(expected)

def test_kClosest_all_points():
    sol = Solution()
    points = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    k = 4
    expected = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    assert sorted(sol.kClosest(points, k)) == sorted(expected)

def test_kClosest_origin_included():
    sol = Solution()
    points = [[1, 3], [-2, 2], [0, 0]]
    k = 2
    expected = [[0, 0], [-2, 2]]
    assert sorted(sol.kClosest(points, k)) == sorted(expected)