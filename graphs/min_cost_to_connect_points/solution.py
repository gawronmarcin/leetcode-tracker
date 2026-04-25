"""
Task:
You are given a 2-D integer array points, where points[i] = [xi, yi].
Each points[i] represents a distinct point on a 2-D plane.
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
between the two points, i.e. |xi - xj| + |yi - yj|.
Return the minimum cost to connect all points together,
 such that there exists exactly one path between each pair of points.

Solution:
Prim's algorithm optimized for dense graphs (O(V^2) time complexity).
It calculates the Minimum Spanning Tree (MST) for a fully connected graph 
(points on a 2D plane) using an array-based approach to find the minimum 
edge, completely avoiding the overhead of a priority queue.
"""
from math import inf
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        dist = [inf] * n
        dist[0] = 0

        for _ in range(n):
            min_u = -1
            min_dist = inf

            for u in range(n):
                if not visited[u]:
                    if min_dist > dist[u]:
                        min_u = u
                        min_dist = dist[u]

            visited[min_u] = True

            for v in range(n):
                if not visited[v]:
                    d = abs(points[min_u][0] - points[v][0]) + abs(points[min_u][1] - points[v][1])
                    if d < dist[v]:
                        dist[v] = d

        return sum(dist)