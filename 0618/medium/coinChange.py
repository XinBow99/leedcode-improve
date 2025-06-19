"""
322. Coin Change
Solved
Medium
Topics
premium lock icon
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Returns the minimum number of coins needed to make up a given amount.

        Uses bottom-up dynamic programming to solve the classic coin change problem.

        Args:
            coins: List of available coin denominations.
            amount: Total amount to make change for.

        Returns:
            Minimum number of coins needed to make up the amount.
            Returns -1 if no combination can produce the amount.
        """
        # Initialize DP array with a value greater than the maximum possible (amount + 1)
        # min_coins[i] = minimum number of coins needed to get amount i
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0  # base case: 0 coins needed to make amount 0

        for change in range(1, amount + 1):
            for coin in coins:
                if change - coin >= 0:
                    # If we can use this coin, check if it gives a better result
                    min_coins[change] = min(min_coins[change], min_coins[change - coin] + 1)

        # If we never updated the value, it means amount is not reachable
        # Let dp[i] be the minimum number of coins needed to make amount i. 
        # The transition is: dp[i] = min(dp[i - coin] + 1) 
        # for every coin where i - coin >= 0.
        # time: O(amount * c)
        # space: O(amount)
        return min_coins[amount] if min_coins[amount] != amount + 1 else -1
