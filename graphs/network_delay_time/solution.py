from math import inf
from queue import PriorityQueue
from typing import List
""" 
Task:
You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.


Solution:
Dijkstra's algorithm to find the shortest paths from a source node to 
all other nodes in a weighted directed graph. 
"""

class Solution:


    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for source, target, weight in times:
            adj[source].append((target, weight))

        distances = [inf] * (n + 1)
        distances[k] = 0

        visited = [False] * (n + 1)
        pq = PriorityQueue()
        pq.put((0, k))

        while not pq.empty():
            current_dist, u = pq.get()

            if current_dist > distances[u]:
                continue

            visited[u] = True

            for v, weight in adj[u]:
                if not visited[v]:
                    new_dist = distances[u] + weight
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        pq.put((new_dist, v))

        max_delay = max(distances[1:])

        return max_delay if max_delay != inf else -1