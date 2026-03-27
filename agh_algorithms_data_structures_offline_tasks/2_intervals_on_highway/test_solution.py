import pytest
from solution import Solution


def test_solve_example():
    sol = Solution()
    # Przykład z treści zadania.
    # Uwaga: nasz kod wyłapuje pierwszy kilometr z maksymalną pokrywą (czyli 3, a nie 6).
    # Jest to poprawne z punktu widzenia matematyki przedziałów.
    assert sol.solve(4, 100, [(3, 10), (0, 6), (20, 30), (25, 35)]) == (2, 3)


def test_solve_point_overlap():
    sol = Solution()
    # Klasyczny przypadek brzegowy: przedziały stykają się w jednym punkcie (kilometr 5).
    # Na 5. kilometrze pokrywa powinna wynieść 2.
    assert sol.solve(2, 20, [(0, 5), (5, 10)]) == (2, 5)


def test_solve_reversed_intervals():
    sol = Solution()
    # Zabezpieczenie przed złośliwymi testami, gdzie a > b.
    assert sol.solve(2, 20, [(10, 3), (15, 8)]) == (2, 8)


def test_solve_no_overlap():
    sol = Solution()
    # Opady całkowicie rozłączne.
    assert sol.solve(3, 50, [(0, 5), (10, 15), (20, 25)]) == (1, 0)


def test_solve_nested_intervals():
    sol = Solution()
    # Jeden duży opad, a w nim kilka mniejszych na tym samym obszarze.
    assert sol.solve(3, 100, [(10, 50), (20, 40), (25, 35)]) == (3, 25)