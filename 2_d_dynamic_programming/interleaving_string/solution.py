class Solution:
    """
    Task:
    You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

    Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met


    This algorithm uses 2D Dynamic Programming to determine if s3 is formed by an interleaving of s1 and s2.
    The DP table dp[i][j] stores a boolean indicating whether the first i characters of s1 and the first j characters of s2
    can form the first i+j characters of s3. We initialize the base cases for single-string prefixes, and then iteratively
    fill the table. For each cell dp[i][j], it becomes True if the current character in s1 matches the target in s3 and
    the state above it (dp[i-1][j]) is True, OR if the current character in s2 matches the target in s3 and the state
    to its left (dp[i][j-1]) is True. The final result is evaluated at dp[len(s1)][len(s2)].
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, m + 1):
            if s2[i - 1] == s3[i - 1]:
                dp[0][i] = dp[0][i - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                if s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[n][m]