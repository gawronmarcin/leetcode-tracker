"""
Task:
You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.
We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.


Solution:
Uses Disjoint Set Union (Union-Find) with path compression.
It processes edges to find the first one that connects two nodes already sharing the same root, which indicates the redundant cycle-forming edge.
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return [u, v]

            parent[root_v] = root_u