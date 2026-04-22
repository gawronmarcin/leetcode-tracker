"""
Task:
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.
Return the number of connected components in the graph.

Solution:
Uses Depth-First Search (DFS) to traverse the undirected graph and counts the number of disjoint connected components by tracking visited nodes.
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = [[] for _ in range(n)]
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        counter = 0
        visited = [False] * n

        def dfs_visit(u):
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    dfs_visit(v)

        for i in range(n):
            if not visited[i]:
                dfs_visit(i)
                counter += 1

        return counter