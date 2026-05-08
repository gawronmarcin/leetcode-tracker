from math import inf
from typing import List

class Solution:
    """
    You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
    Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.
    You may assume that you have an unlimited number of each coin.

    Solves the coin change problem using a bottom-up dynamic programming strategy. 
    The algorithm iteratively determines the minimum number of coins required for 
    every amount up to the target by evaluating all available denominations.
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != inf else -1