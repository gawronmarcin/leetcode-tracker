import pytest
from solution import Solution


class TestLongestCommonSubsequence:

    @pytest.fixture
    def sol(self):
        return Solution()

    @pytest.mark.parametrize("text1, text2, expected", [
        ("cat", "crabt", 3),
        ("abcd", "abcd", 4),
        ("abcd", "efgh", 0),

        ("abcde", "ace", 3),
        ("a", "a", 1),
        ("a", "b", 0),
        ("abc", "def", 0),
        ("oxcpqrsvwf", "shmtulqrypy", 2)
    ])
    def test_longest_common_subsequence(self, sol, text1, text2, expected):
        assert sol.longestCommonSubsequence(text1, text2) == expected