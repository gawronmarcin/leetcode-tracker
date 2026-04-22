from typing import List
"""
Task:
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers,
 return any of them. If it's not possible to finish all courses, return an empty array.

Solution:
Topological sorting using a recursive approach based on in-degrees.
It finds nodes with no incoming edges (in-degree 0), adds them to the result,
and recursively processes their neighbors by decrementing their in-degrees.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            G[pre].append(crs)
            in_degree[crs] += 1

        visited = [0] * numCourses
        res = []

        def dfs_visit(u):
            if visited[u] == 0:
                res.append(u)
                visited[u] = 1
                for v in G[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        dfs_visit(v)

        for i in range(numCourses):
            if in_degree[i] == 0 and visited[i] == 0:
                dfs_visit(i)

        if len(res) != numCourses:
            return []

        return res