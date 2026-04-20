from typing import List

"""
Task:
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
The pair [0, 1], indicates that must take course 1 before taking course 0.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.

Solution: Depth-First Search (DFS) for cycle detection in a directed graph.
It uses a 3-state tracking array: 0 (unvisited), 1 (visiting/in current path), and 2 (visited/safe).
If DFS encounters a node in state 1, a cycle is detected, meaning the courses cannot be finished.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = [[] for _ in range(numCourses)]
        states = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        def has_cycle(node: int) -> bool:
            states[node] = 1

            for neighbor in adj_list[node]:
                if states[neighbor] == 1:
                    return True
                if states[neighbor] == 0:
                    if has_cycle(neighbor):
                        return True

            states[node] = 2
            return False

        for course in range(numCourses):
            if states[course] == 0:
                if has_cycle(course):
                    return False

        return True