import pytest
import sys
import io
from solution import Solution


@pytest.mark.parametrize("input_data, expected_output", [
    ("3\n1\n2\n5\n2\n1\n3\n", "5\n1\n"),
    ("5\n7\n7\n7\n7\n7\n3\n1\n3\n5\n", "7\n7\n7\n"),
    ("4\n10\n20\n30\n40\n2\n1\n4\n", "40\n10\n"),
    ("3\n9\n8\n7\n3\n1\n2\n3\n", "9\n8\n7\n")
])
def test_solve_logic(monkeypatch, capsys, input_data, expected_output):
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))

    sol = Solution()
    sol.solve()

    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_solve_empty_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(""))
    sol = Solution()

    assert sol.solve() is None