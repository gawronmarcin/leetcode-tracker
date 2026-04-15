from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Task:
        You are given a m×n @D grid initialized with these three possible values:
        -1 - A water cell that can not be traversed.
        0 - A treasure chest.
        INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
        Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.
        Assume the grid can only be traversed up, down, left, or right.
        Modify the grid in-place.

        Solution:
        Multi-source BFS: Start from all treasures (0) at once and expand outwards. 
        The first time we reach a land cell (INF), it is guaranteed to be the shortest path.
        """
        n = len(grid)
        m = len(grid[0])
        de = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    de.append((i, j, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while de:
            r, c, dist = de.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = dist + 1
                    de.append((nr, nc, dist + 1))