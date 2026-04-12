import pytest
from solution import Solution


@pytest.mark.parametrize("grid, expected_area", [
    # 1. Standardowy przypadek (przykład z LeetCode)
    (
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
            ],
            6
    ),

    # 2. Brak lądu (sama woda)
    (
            [[0, 0, 0, 0, 0, 0, 0, 0]],
            0
    ),

    # 3. Pojedyncza komórka lądu
    (
            [[1]],
            1
    ),

    # 4. Pojedyncza komórka wody
    (
            [[0]],
            0
    ),

    # 5. Cała plansza to jedna wielka wyspa
    (
            [
                [1, 1],
                [1, 1]
            ],
            4
    ),

    # 6. Komórki połączone po przekątnej (nie tworzą wyspy)
    (
            [
                [1, 0],
                [0, 1]
            ],
            1
    )
])
def test_maxAreaOfIsland(grid, expected_area):
    sol = Solution()
    # Przekazujemy głęboką kopię tablicy, jeśli nie chcemy,
    # aby test modyfikował oryginalne dane (choć tu podajemy je w locie)
    assert sol.maxAreaOfIsland(grid) == expected_area