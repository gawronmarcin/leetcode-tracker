from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Task:
        You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
        You may buy and sell one NeetCoin multiple times with the following restrictions:

        After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
        You may only own at most one NeetCoin at a time.
        You may complete as many transactions as you like.

            Return the maximum profit you can achieve.


        Dynamic Programming solution using a 2D array to track two states for each day:
        - dp[i][0]: Maximum profit on day i while NOT holding a stock.
        - dp[i][1]: Maximum profit on day i while HOLDING a stock.

        Transitions:
        - dp[i][0]: We either didn't hold a stock yesterday (dp[i-1][0]), or we held one yesterday and sold it today (dp[i-1][1] + prices[i]).
        - dp[i][1]: We either already held a stock yesterday (dp[i-1][1]), or we bought one today. To buy today, we must use the non-holding profit from two days ago (dp[i-2][0]) to strictly respect the 1-day cooldown rule.
        """
        n = len(prices)
        if n <= 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][1] -= prices[0]
        dp[1][0] = max(0, prices[1] - prices[0])
        dp[1][1] = max(-prices[0], -prices[1])

        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[n - 1][0]