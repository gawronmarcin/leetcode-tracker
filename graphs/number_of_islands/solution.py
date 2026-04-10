from typing import List
class Solution:
    """
    Task:
    Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
    An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.
    You may assume water is surrounding the grid (i.e., all the edges are water).

    Approach: Depth-First Search (DFS)
    We iterate through the grid, and for every piece of land ("1") we find,
    we increment the island count and trigger a DFS.
    The DFS explores all connected land horizontally and vertically,
    sinking it (changing "1" to "0") in-place to avoid using an extra 'visited' set.
    This optimizes auxiliary space complexity to O(1).
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count