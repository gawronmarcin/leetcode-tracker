from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.

        If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.

        Return the maximum number of coins you can receive by bursting all of the balloons.


        Dynamic Programming approach using Interval DP.
        The algorithm calculates the maximum coins obtainable by bursting balloons within the subarray from index 'left' to 'right'.
        It pads the original array with 1s at both ends to handle boundary conditions seamlessly.
        For each interval [left, right], it iterates through every possible balloon 'i' to be the *last* one burst in that interval.
        Choosing 'i' as the last balloon decouples the problem into two independent subproblems: [left, i-1] and [i+1, right].
        The DP table stores the optimal results for these subproblems, correctly resolving dependencies by building up from the bottom.
        """
        n = len(nums)
        new_nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for left in range(n, 0, -1):
            for right in range(left, n + 1):
                for i in range(left, right + 1):
                    coins = new_nums[left - 1] * new_nums[i] * new_nums[right + 1]
                    coins += dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][n]