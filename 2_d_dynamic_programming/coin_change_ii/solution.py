from typing import List

class Solution:
    """
    Task:
    You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc)
    and an integer amount representing a target amount of money.
    Return the number of distinct combinations that total up to amount.
    If it's impossible to make up the amount, return 0.
    You may assume that you have an unlimited number of each coin and that each value in coins is unique.

    Calculates the number of distinct combinations that sum up to a specific amount using 2D Dynamic Programming.
    The dp[i][j] state represents the number of ways to form the amount 'j' using a subset of coins from index 0 to 'i'.
    The state transition relies on two scenarios:
    1. Excluding the current coin (dp[i - 1][j]).
    2. Including the current coin at least once, provided it fits in the current amount (dp[i][j - coins[i]]).
    Base cases initialize combinations for an amount of 0 and the multiples of the first coin.
    """

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for i in range(1, amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = 1

        for i in range(1, n):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i]:
                    dp[i][j] += dp[i][j - coins[i]]

        return dp[n - 1][amount]