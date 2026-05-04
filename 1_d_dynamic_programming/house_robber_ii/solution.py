"""
Task:
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

Breaks the circular arrangement into two separate linear problems: one skipping the first house, and one skipping the last.
Optimizes space complexity to O(1) by using two variables to track the maximum loot instead of allocating full arrays.
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(houses):
            rob1, rob2 = 0, 0
            for money in houses:
                temp = max(rob1 + money, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(helper(nums[:-1]), helper(nums[1:]))