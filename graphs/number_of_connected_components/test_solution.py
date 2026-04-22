import pytest
from solution import Solution


def test_count_components_example():
    sol = Solution()
    assert sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_count_components_fully_connected():
    sol = Solution()
    assert sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


def test_count_components_no_edges():
    sol = Solution()
    assert sol.countComponents(4, []) == 4


def test_count_components_with_cycle():
    sol = Solution()
    assert sol.countComponents(4, [[0, 1], [1, 2], [2, 3], [3, 0]]) == 1


def test_count_components_single_node():
    sol = Solution()
    assert sol.countComponents(1, []) == 1


def test_count_components_multiple_cycles_and_isolated():
    sol = Solution()
    assert sol.countComponents(6, [[0, 1], [1, 2], [2, 0], [3, 4]]) == 3