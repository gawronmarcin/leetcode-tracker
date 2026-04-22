import pytest
from solution import Solution

def test_find_order_simple_path():
    sol = Solution()
    # Najprostszy przypadek: 0 musi być przed 1
    assert sol.findOrder(2, [[1, 0]]) == [0, 1]

def test_find_order_multiple_valid_paths():
    sol = Solution()
    # Wiele ścieżek: 0 -> 1 -> 3 oraz 0 -> 2 -> 3
    result = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    # Sprawdzamy przynależność do zbioru akceptowalnych wyników
    assert result in ([0, 1, 2, 3], [0, 2, 1, 3])

def test_find_order_impossible_cycle():
    sol = Solution()
    # Cykl (1 wymaga 0, 0 wymaga 1) - nie da się skończyć
    assert sol.findOrder(2, [[1, 0], [0, 1]]) == []

def test_find_order_no_prerequisites():
    sol = Solution()
    # Brak zależności - jakakolwiek kolejność zawierająca wszystkie wierzchołki jest ok
    result = sol.findOrder(3, [])
    assert len(result) == 3
    assert set(result) == {0, 1, 2}

def test_find_order_disconnected_graph():
    sol = Solution()
    # Dwa grafy: jeden to 0->1, drugi to niezależny punkt 2
    result = sol.findOrder(3, [[1, 0]])
    assert len(result) == 3
    assert set(result) == {0, 1, 2}
    # Profesjonalne sprawdzenie zależności topologicznej bez twardego kodowania tablic:
    assert result.index(0) < result.index(1)

def test_find_order_complex_cycle():
    sol = Solution()
    # Złożony graf, który ma ukryty cykl: 1->2, 2->3, 3->1
    assert sol.findOrder(4, [[2, 1], [3, 2], [1, 3], [1, 0]]) == []