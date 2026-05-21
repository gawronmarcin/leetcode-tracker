from typing import List


class Solution:
    """
    You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.

    Return the length of the longest strictly increasing path within matrix.

    From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.


    Calculates the length of the longest strictly increasing path in a 2D matrix.

    The algorithm uses Depth-First Search (DFS) combined with Memoization. 
    For each unvisited cell, it recursively explores all valid, strictly increasing 
    paths to its adjacent neighbors (down, left, right, up). To avoid redundant 
    calculations, the maximum path length starting from each cell is stored in a 
    2D 'dp' array. The overall time and space complexity is O(N * M), where N and 
    M are the dimensions of the matrix.
    """

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n<=0:
            return 0
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i, j):
            longest = 1

            if 0 <= i + 1 < n and 0 <= j < m and matrix[i + 1][j] > matrix[i][j]:
                if dp[i + 1][j] == 0:
                    longest = max(longest, dfs(i + 1, j) + 1)
                else:
                    longest = max(longest, dp[i + 1][j] + 1)

            if 0 <= i < n and 0 <= j - 1 < m and matrix[i][j - 1] > matrix[i][j]:
                if dp[i][j - 1] == 0:
                    longest = max(longest, dfs(i, j - 1) + 1)
                else:
                    longest = max(longest, dp[i][j - 1] + 1)

            if 0 <= i < n and 0 <= j + 1 < m and matrix[i][j + 1] > matrix[i][j]:
                if dp[i][j + 1] == 0:
                    longest = max(longest, dfs(i, j + 1) + 1)
                else:
                    longest = max(longest, dp[i][j + 1] + 1)

            if 0 <= i - 1 < n and 0 <= j < m and matrix[i - 1][j] > matrix[i][j]:
                if dp[i - 1][j] == 0:
                    longest = max(longest, dfs(i - 1, j) + 1)
                else:
                    longest = max(longest, dp[i - 1][j] + 1)

            dp[i][j] = longest
            return longest

        for i in range(n):
            for j in range(m):
                if dp[i][j] == 0:
                    dfs(i, j)

        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dp[i][j])

        return res