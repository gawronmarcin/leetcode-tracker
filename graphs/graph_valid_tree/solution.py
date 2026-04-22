"""
Task:
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.


Solution:
Validates a tree by first verifying the necessary mathematical condition (edges == nodes - 1)
to rule out cycles or disjoint forests, and then uses DFS from a single node to confirm the graph is fully connected.
"""
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        G = [[] for _ in range(n)]
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        visited = [0] * n

        def dfs_visit(u):
            visited[u] = 1
            for v in G[u]:
                if visited[v] == 0:
                    dfs_visit(v)

        dfs_visit(0)

        return sum(visited) == n