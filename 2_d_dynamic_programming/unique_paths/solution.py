class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Task:
        There is an m x n grid where you are allowed to move either down or to the right at any point in time.
        Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).
        You may assume the output will fit in a 32-bit integer.


        Calculates the number of unique paths in an m x n grid using Dynamic Programming.
        It initializes an m x n matrix where the top row and left column are set to 1.
        For the remaining cells, the number of paths is the sum of the paths from the cell
        directly above and the cell directly to the left.
        The result is stored in the bottom-right corner of the matrix.
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]