from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Task:
        You are given an array of positive integers nums.
        Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.


        This algorithm uses a 1D Dynamic Programming approach to solve the subset sum problem.
        If the total sum of the array is odd, partitioning into two equal subsets is impossible.
        Otherwise, the target sum is exactly half of the total sum. The boolean 'dp' array tracks 
        achievable sums, updating backwards to ensure each element is used at most once.
        """
        t = sum(nums)

        if t % 2 != 0:
            return False

        t //= 2
        dp = [False] * (t + 1)
        dp[0] = True

        for num in nums:
            for j in range(t, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[t]