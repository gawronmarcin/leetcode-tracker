"""
Task:
There are n gas stations along a circular route. You are given two integer arrays gas and cost where:

gas[i] is the amount of gas at the ith station.
cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)
You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.

It's guaranteed that at most one solution exists.




This algorithm uses a greedy approach to find the valid starting gas station. 
First, it evaluates if the total available gas is sufficient to cover the total 
route cost by comparing their sums; if not, it returns -1. It then iterates 
through the stations, maintaining a current fuel balance. If the balance drops 
below zero, it means the journey is impossible from the current starting point, 
as well as from any station between the start and the current index. In such 
a case, the starting point is updated to the current station, and the fuel 
balance is reset to zero. The initial global sum check guarantees that if a 
valid start is identified during this single pass, it is the correct answer.
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1

        curr = 0
        start = 0

        for i in range(n):
            if curr < 0:
                start = i
                curr = 0

            curr += gas[i]
            curr -= cost[i]

        return start