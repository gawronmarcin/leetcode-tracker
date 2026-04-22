import pytest
from solution import Solution

def test_find_redundant_connection_simple_triangle():
    sol = Solution()
    # Najprostszy możliwy cykl (trójkąt): 1 połączone z 2, 2 z 3, i nadmiarowa 1-3
    assert sol.findRedundantConnection([[1, 2], [2, 3], [1, 3]]) == [1, 3]

def test_find_redundant_connection_square():
    sol = Solution()
    # Przykład 1 z zadania (kwadrat)
    assert sol.findRedundantConnection([[1, 2], [1, 3], [3, 4], [2, 4]]) == [2, 4]

def test_find_redundant_connection_larger_graph():
    sol = Solution()
    # Przykład z większym grafem (często podawany jako Przykład 2 na LeetCode)
    # 1-2, 2-3, 3-4, nadmiarowa 1-4 zamyka cykl, a do 1 jest jeszcze podpięte 5
    assert sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]

def test_find_redundant_connection_line_with_loop():
    sol = Solution()
    # Linia z pętlą na końcu: 1-2-3-4-5, gdzie 3 łączy się dodatkowo z 5
    assert sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [4, 5], [3, 5]]) == [3, 5]

def test_find_redundant_connection_inner_cycle():
    sol = Solution()
    # Sytuacja, w której cykl pojawia się bardzo wcześnie w tablicy (indeksy 1,2,3),
    # a po nim następują inne poprawne gałęzie.
    assert sol.findRedundantConnection([[1, 2], [2, 3], [1, 3], [3, 4], [4, 5]]) == [1, 3]