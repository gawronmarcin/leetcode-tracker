"""
Task:
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

Calculates the maximum money a robber can steal using dynamic programming. It builds an array to store the maximum loot up to each house,
deciding at each step whether to rob the current house (adding its value to the loot from two houses prior) or to skip it (carrying forward the loot from the previous house).
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]

        dp = [-1] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]