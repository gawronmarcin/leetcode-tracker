"""
Task:
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.

Solves the Climbing Stairs problem using a 1D dynamic programming array.
The number of ways to reach step i is calculated as the sum of ways to reach the two preceding steps (i-1 and i-2).
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]