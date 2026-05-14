"""
Task:
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.
A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.
For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Computes the Longest Common Subsequence (LCS) using a 2D Dynamic Programming approach.
It explicitly initializes the first row and column to establish base cases. For the 
remaining cells, it builds the optimal solution by adding 1 to the diagonal if 
characters match, or taking the maximum value from adjacent cells (top or left) 
if they do not.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        DP = [[0 for _ in range(n)] for _ in range(m)]

        if text1[0] == text2[0]:
            DP[0][0] = 1

        for i in range(1, n):
            DP[0][i] = DP[0][i - 1]
            if text2[0] == text1[i]:
                DP[0][i] = 1

        for i in range(1, m):
            DP[i][0] = DP[i - 1][0]
            if text2[i] == text1[0]:
                DP[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if text1[j] == text2[i]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                else:
                    DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])

        return DP[m - 1][n - 1]