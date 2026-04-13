from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

"""
Task:

Given a node in a connected undirected graph, return a deep copy of the graph.
Each node in the graph contains an integer value and a list of its neighbors.

Solution:

I use a dictionary (`visited`) to map {original_node: cloned_node}. 
This prevents infinite loops caused by graph cycles and allows us to 
quickly connect already created clones.

Complexity:
- Time: O(V + E) (visits every vertex and edge once)
- Space: O(V) (for the dictionary and recursion stack)
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(curr_node):
            if curr_node in visited:
                return visited[curr_node]

            copy = Node(curr_node.val)
            visited[curr_node] = copy

            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)