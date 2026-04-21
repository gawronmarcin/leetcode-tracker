"""
Task:
Evil knight has a dog (the one who ate the plot of the previous offline task) who loves mountain hiking.
The mountains consist of n shelters connected by m undirected paths.
These mountains are unusual: the time to travel from shelter i to j through k is the product of their times, meaning d(i,j) = d(i,k) * d(k,j). Zlycerz lives next to shelter 1.
The dog recently overheard Algosi and Bajtek talking about a new list of k most interesting shelters and wants to find the minimum time to reach each of them from shelter 1.
If there are multiple paths with the same minimum time, the dog prefers the one passing through the fewest shelters.
For each interesting shelter, output the number of shelters on the path, the sequence of shelters from start to finish, and the total time.

Solution:
Modified Dijkstra's algorithm using multiplication for path costs.
A Priority Queue stores tuples of (current_cost, path_length, vertex) to automatically break cost ties by favoring paths with fewer vertices.
A parent array is used to reconstruct the exact path for each query.
"""
from queue import PriorityQueue
from math import inf

class Solution:
    def solve(self, n, m, k, edges, spots):
        G = [[] for _ in range(n + 1)]
        visited = [0] * (n + 1)
        parent = [None] * (n + 1)
        costs = [inf] * (n + 1)
        road_len = [inf] * (n + 1)

        for u, v, cost in edges:
            G[u].append((v, cost))
            G[v].append((u, cost))

        costs[1] = 1
        road_len[1] = 1

        pq = PriorityQueue()
        pq.put((costs[1], road_len[1], 1))

        while not pq.empty():
            curr_cost, curr_road, u = pq.get()

            if visited[u] == 0:
                visited[u] = 1

                for neighbor, weight in G[u]:
                    new_cost = curr_cost * weight
                    new_road = curr_road + 1

                    if new_cost < costs[neighbor] or (new_cost == costs[neighbor] and new_road < road_len[neighbor]):
                        pq.put((new_cost, new_road, neighbor))
                        road_len[neighbor] = new_road
                        costs[neighbor] = new_cost
                        parent[neighbor] = u

        results = []
        for spot in spots:
            res = [road_len[spot]]
            bufor = [spot]
            par = parent[spot]

            for _ in range(road_len[spot] - 1):
                bufor.append(par)
                par = parent[par]

            bufor = bufor[::-1]
            res.extend(bufor)
            res.append(costs[spot])

            results.append(res)

        return results