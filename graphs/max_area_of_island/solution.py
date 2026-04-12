from typing import List

"""
TasK:
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
The area of an island is defined as the number of cells within the island.
Return the maximum area of an island in grid. If no island exists, return 0.

Solution:
Finds the maximum area of an island in a given 2D grid using Depth-First Search (DFS).

The algorithm iterates through each cell in the grid. When an unvisited land cell (1) 
is found, it triggers a DFS to calculate the total area of that specific island. 
The DFS recursively explores all four adjacent directions (up, down, left, right), 
accumulating the count of connected land cells. To prevent infinite loops and 
redundant checks, visited land cells are immediately mutated into water (0). 
The maximum area encountered across all islands is tracked and returned.

Time Complexity: O(N * M), where N is the number of rows and M is the number of columns.
Space Complexity: O(N * M) in the worst-case scenario for the recursion call stack.

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        n = len(grid)
        m = len(grid[0])
        def dfs_visit(i, j):
            if (i < 0 or i >= n) or (j < 0 or j >= m) or grid[i][j] == 0:
                return 0
            curr = 1
            grid[i][j] = 0
            curr += dfs_visit(i - 1, j)
            curr += dfs_visit(i + 1, j)
            curr += dfs_visit(i, j - 1)
            curr += dfs_visit(i, j + 1)
            return curr

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_island = max(max_island, dfs_visit(i, j))
        return max_island