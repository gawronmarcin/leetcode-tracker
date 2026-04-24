from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Task:
        You are given a list of flight tickets tickets where tickets[i] = [from_i, to_i] represent the source airport and the destination airport.
        Each from_i and to_i consists of three uppercase English letters.
        Reconstruct the itinerary in order and return it.
        All of the tickets belong to someone who originally departed from "JFK". Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.
        If there are multiple valid flight paths, return the lexicographically smallest one.
        For example, the itinerary ["JFK", "SEA"] has a smaller lexical order than ["JFK", "SFO"].
        You may assume all the tickets form at least one valid flight path.

        Solution:
        Finds an Eulerian path in a directed graph.
        Sorts edges in reverse lexicographical order to allow O(1) popping.
        Traverses via DFS, adding nodes to the result only when no outgoing edges remain,
        then reverses the final path to construct the correct itinerary.
        """
        keys = {}
        tickets.sort(reverse=True)

        for src, dst in tickets:
            if src not in keys:
                keys[src] = len(keys)
            if dst not in keys:
                keys[dst] = len(keys)

        graph = [[] for _ in range(len(keys))]

        for src, dst in tickets:
            graph[keys[src]].append(dst)

        res = []

        def dfs_visit(u):
            while graph[keys[u]]:
                v = graph[keys[u]].pop()
                dfs_visit(v)
            res.append(u)

        dfs_visit("JFK")

        return res[::-1]