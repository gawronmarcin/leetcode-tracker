import pytest
from solution import Solution

@pytest.mark.parametrize("num_courses, prerequisites, expected", [
    (2, [[1, 0]], True),                                   # Prosty graf, brak cyklu
    (2, [[1, 0], [0, 1]], False),                          # Prosty cykl
    (4, [[1, 0], [3, 2]], True),                           # Niespójny graf (dwie wyspy)
    (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),          # Złożony cykl
    (3, [], True),                                         # Brak zależności
    (1, [], True),                                         # Tylko jeden węzeł
    (3, [[0, 1], [0, 2], [1, 2]], True)                    # Krawędź krzyżowa, brak cyklu
])
def test_canFinish(num_courses, prerequisites, expected):
    sol = Solution()
    assert sol.canFinish(num_courses, prerequisites) == expected