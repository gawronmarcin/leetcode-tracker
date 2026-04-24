import pytest
from solution import Solution


@pytest.mark.parametrize("tickets, expected", [
    (
            [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]],
            ["JFK", "BUF", "HOU", "SEA"]
    ),

    (
            [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    ),

    (
            [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
            ["JFK", "NRT", "JFK", "KUL"]
    )
])
def test_findItinerary(tickets, expected):
    sol = Solution()
    assert sol.findItinerary(tickets) == expected