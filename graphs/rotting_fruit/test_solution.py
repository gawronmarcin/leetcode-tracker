import pytest
from solution import Solution


@pytest.mark.parametrize(
    "grid, expected",
    [
        # Standardowy przypadek z zadania - owoce gniją w 4 minuty
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),

        # Przypadek z izolowanym owocem w rogu - niemożliwe zarażenie wszystkich
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),

        # Brak świeżych owoców na starcie, tylko zgniły i puste pole
        ([[0, 2]], 0),

        # Sama pusta plansza
        ([[0, 0, 0], [0, 0, 0]], 0),

        # Same świeże owoce, brak źródła zgnilizny
        ([[1, 1], [1, 1]], -1),

        # Przypadki brzegowe (brzegowe wymiary z Constraints: 1x1)
        ([[1]], -1),
        ([[2]], 0),
        ([[0]], 0),
    ]
)
def test_oranges_rotting(grid, expected):
    sol = Solution()
    assert sol.orangesRotting(grid) == expected