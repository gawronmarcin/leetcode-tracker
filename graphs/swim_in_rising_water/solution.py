"""
Task:
You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).
Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.
You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t.
Starting from the top left square (0, 0), return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).

Solution:
This solution uses a modified Dijkstra's algorithm with a Priority Queue to find the optimal path from the top-left to the bottom-right corner.
Instead of summing edge weights, it tracks the maximum water elevation encountered along a path, greedily exploring the route with the lowest maximum elevation first to guarantee the minimum possible time.
"""
from math import inf
from queue import PriorityQueue
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dist = [[inf] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]
        dist[0][0] = grid[0][0]

        q = PriorityQueue()
        q.put((dist[0][0], 0, 0))
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while not q.empty():
            w, ui, uj = q.get()

            if ui == n - 1 and uj == m - 1:
                return w

            if visited[ui][uj] == 0:
                visited[ui][uj] = 1

                for move in moves:
                    vi = ui + move[0]
                    vj = uj + move[1]

                    if 0 <= vi < n and 0 <= vj < m and visited[vi][vj] == 0:
                        if max(w, grid[vi][vj]) < dist[vi][vj]:
                            dist[vi][vj] = max(w, grid[vi][vj])
                            q.put((dist[vi][vj], vi, vj))

        return dist[n - 1][m - 1]