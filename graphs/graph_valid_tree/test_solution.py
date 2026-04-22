import pytest
from solution import Solution

def test_valid_tree_correct_path():
    sol = Solution()
    # Poprawne drzewo (prosta linia / rozgałęzienia)
    assert sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True

def test_valid_tree_with_cycle():
    sol = Solution()
    # Graf zawiera cykl: 1-2-3-1
    assert sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False

def test_valid_tree_too_few_edges():
    sol = Solution()
    # 5 wierzchołków, ale tylko 3 krawędzie (od razu odrzucone przez len(edges) != n-1)
    assert sol.validTree(5, [[0, 1], [1, 2], [2, 3]]) == False

def test_valid_tree_too_many_edges():
    sol = Solution()
    # 5 wierzchołków, 5 krawędzi (od razu odrzucone, musi zawierać cykl)
    assert sol.validTree(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == False

def test_valid_tree_disconnected_components():
    sol = Solution()
    # Właściwa liczba krawędzi (n-1 = 4), ale graf jest niespójny
    # (cykl 0-1-2-0 oraz osobny komponent 3-4)
    assert sol.validTree(5, [[0, 1], [1, 2], [2, 0], [3, 4]]) == False

def test_valid_tree_single_node():
    sol = Solution()
    # Przypadek brzegowy: 1 wierzchołek, brak krawędzi to poprawne drzewo
    assert sol.validTree(1, []) == True