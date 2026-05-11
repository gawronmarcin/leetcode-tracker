from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Task:
        Given an integer array nums, return the length of the longest strictly increasing subsequence.
        A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.


        Computes the length of the longest strictly increasing subsequence 
        using a standard O(n^2) dynamic programming approach.
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)