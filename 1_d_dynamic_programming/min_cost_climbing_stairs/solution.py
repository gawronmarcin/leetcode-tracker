"""
Task:
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
You may choose to start at the index 0 or the index 1 floor.
Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

Calculates the minimum cost to reach the top of the staircase using dynamic programming.
An array is used to store the minimum cost to reach each step, computed by taking the minimum of the cost to reach either of the two previous steps plus their respective stair costs.
"""
from math import inf
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [inf] * (n + 1)
        min_cost[0] = 0
        min_cost[1] = 0

        for i in range(2, n + 1):
            min_cost[i] = min(min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2])

        return min_cost[n]