from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Task:
        You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.
        Return true if you can reach the last index starting from index 0, or false otherwise.

        Uses a greedy approach to track the maximum reachable index (max_dist).
        Iterates through the array, updating max_dist if the current index is reachable.
        Returns True early if the last index becomes reachable; otherwise, returns False.
        """
        n = len(nums)
        if n <= 1:
            return True

        max_dist = nums[0]
        for i in range(1, n):
            if i <= max_dist:
                max_dist = max(max_dist, i + nums[i])
                if max_dist >= n - 1:
                    return True

        return False