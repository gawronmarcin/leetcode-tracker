import pytest
from solution import Solution

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("board, expected", [
    (
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "X", "O"]
        ],
        [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "O"]
        ]
    ),
    (
        [],
        []
    ),
    (
        [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ],
        [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]
    ),
    (
        [
            ["O", "O"],
            ["O", "O"]
        ],
        [
            ["O", "O"],
            ["O", "O"]
        ]
    ),
    (
        [
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"]
        ],
        [
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"]
        ]
    )
])
def test_solve(sol, board, expected):
    sol.solve(board)
    assert board == expected