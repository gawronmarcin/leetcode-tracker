import pytest
from solution import Node, Solution


def test_clone_empty_graph():
    sol = Solution()
    # Pusty graf na wejściu powinien zwrócić None
    assert sol.cloneGraph(None) is None


def test_clone_single_node():
    sol = Solution()
    node = Node(1)

    clone = sol.cloneGraph(node)

    # Aserty sprawdzające głęboką kopię i wartości
    assert clone is not None
    assert clone is not node  # Klon musi być innym obiektem w pamięci
    assert clone.val == 1
    assert len(clone.neighbors) == 0


def test_clone_graph_with_cycle():
    sol = Solution()
    # Budujemy prosty graf z cyklem: 1 <-> 2
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors.append(node2)
    node2.neighbors.append(node1)

    clone1 = sol.cloneGraph(node1)

    # Sprawdzamy pierwszy wierzchołek
    assert clone1 is not None
    assert clone1 is not node1
    assert clone1.val == 1
    assert len(clone1.neighbors) == 1

    # Sprawdzamy sąsiada (wierzchołek 2)
    clone2 = clone1.neighbors[0]
    assert clone2 is not node2
    assert clone2.val == 2
    assert len(clone2.neighbors) == 1

    # Sprawdzamy, czy cykl został poprawnie zamknięty na SKLONOWANYCH obiektach
    assert clone2.neighbors[0] is clone1