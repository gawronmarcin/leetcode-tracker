
from collections import deque
from typing import List
"""
Task:
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Solution: 
 
Uses a Multi-Source Breadth-First Search (BFS) to simulate the rotting process layer by layer, tracking the maximum time elapsed and decrementing the count of fresh oranges to detect unreachable cells.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
        fresh_num = 0
        max_step = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_num += 1

        while q:
            r, c, step = q.popleft()
            max_step = step

            for dr, dc in moves:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, step + 1))
                    fresh_num -= 1

        if fresh_num > 0:
            return -1

        return max_step