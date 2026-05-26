class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Task:
        You are given two strings word1 and word2, each consisting of lowercase English letters.

        You are allowed to perform three operations on word1 an unlimited number of times:

        Insert a character at any position
        Delete a character at any position
        Replace a character at any position
        Return the minimum number of operations to make word1 equal word2.


        Computes the minimum edit distance (Levenshtein distance) between two strings
        using Dynamic Programming. The dp[i][j] cell holds the minimum number of
        operations (insert, delete, replace) required to transform the prefix
        of word1 of length i into the prefix of word2 of length j.
        """
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i

        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )

        return dp[n][m]