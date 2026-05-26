class Solution:
    """
    Task:
    You are given two strings s and t, both consisting of english letters.

    Return the number of distinct subsequences of s which are equal to t.


    This algorithm uses 2D Dynamic Programming to find the number of distinct subsequences.
    The state dp[i][j] represents the number of times the prefix of string t up to index j
    appears as a subsequence in the prefix of string s up to index i.

    It first initializes the matrix and processes the first column (where j=0). Then, it fills
    the rest of the matrix iteratively. For any given cell (i, j), the count inherently includes
    dp[i-1][j] (which represents ignoring the current character in s). If the characters match
    (s[i] == t[j]), it additionally adds the count from dp[i-1][j-1], representing a new match
    formed by pairing these two characters.
    """

    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = [[0] * m for _ in range(n)]

        if s[0] == t[0]:
            dp[0][0] = 1

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            if s[i] == t[0]:
                dp[i][0] += 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[n - 1][m - 1]