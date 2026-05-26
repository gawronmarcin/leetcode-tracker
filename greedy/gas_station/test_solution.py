import pytest
from solution import Solution


@pytest.mark.parametrize(
    "gas, cost, expected",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),

        ([5], [4], 0),
        ([4], [5], -1),
        ([2], [2], 0),

        ([1, 2], [2, 1], 1),

        ([0, 0, 0], [0, 0, 0], 0),

        ([5, 8, 2, 8], [6, 5, 6, 6], 3),
    ]
)
def test_can_complete_circuit(gas, cost, expected):
    sol = Solution()
    assert sol.canCompleteCircuit(gas, cost) == expected