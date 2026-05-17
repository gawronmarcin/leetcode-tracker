from typing import List

class Solution:
    """
    Task:
    You are given an array of integers nums and an integer target.

    For each number in the array, you can choose to either add or subtract it to a total sum.

    For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
    If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

    Return the number of different ways that you can build the expression such that the total sum equals target.


    Algorithm: Dynamic Programming with Offset (0/1 Knapsack variant).

    This approach uses a 2D array where dp[i][j] stores the number of ways to
    assign '+' and '-' symbols to the first 'i' numbers to reach a sum 'j'.
    Because intermediate sums can be negative, an offset equal to the total sum
    of the array is added to all column indices. This shifts the possible sum
    range from [-total, total] to [0, 2 * total], allowing the use of a standard
    0-indexed array. The table is populated iteratively by pulling the number
    of valid expressions from the previous row (i-1) based on either adding
    or subtracting the current number.
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        sumsize = total * 2

        if abs(target) > total:
            return 0

        dp = [[0] * (sumsize + 1) for _ in range(n)]

        dp[0][nums[0] + total] += 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, n):
            for j in range(sumsize + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]
                if j + nums[i] < sumsize + 1:
                    dp[i][j] += dp[i - 1][j + nums[i]]

        return dp[n - 1][target + total]