import pytest
from solution import Solution


@pytest.mark.parametrize("intervals, queries, expected", [
    # 1. Nasz przypadek z debugowania
    ([[2, 3], [1, 3], [6, 6], [3, 7]], [2, 3, 1, 7, 6, 8], [2, 2, 3, 5, 1, -1]),

    # 2. Standardowy przykład z nachodzącymi przedziałami
    ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5], [3, 3, 1, 4]),

    # 3. Przypadki, gdzie niektóre zapytania zwracają -1
    ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22], [2, -1, 4, 6]),

    # 4. Żadne zapytanie nie trafia w żaden przedział
    ([[5, 10], [15, 20]], [1, 4, 11, 25], [-1, -1, -1, -1]),

    # 5. Duże i małe przedziały zaczynające się w tym samym miejscu
    ([[1, 100], [1, 5], [1, 1]], [1, 3, 50], [1, 5, 100])
])
def test_minInterval(intervals, queries, expected):
    sol = Solution()
    assert sol.minInterval(intervals, queries) == expected