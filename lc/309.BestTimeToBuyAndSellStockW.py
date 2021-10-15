# 309. Best Time to Buy and Sell Stock with Cooldown
# Medium

# 4351

# 143

# Add to List

# Share
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0
 

# Constraints:

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000


# This solution works:


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # status: 0 can buy; 1 can sell; 2 cooldown
        @lru_cache(None)
        def helper(i, status):
            if i > len(prices)-1:
                return 0
            best = float('-inf')
            if status == 0:
                best = max(best, - prices[i] + helper(i+1, 1), helper(i+1, status))
            elif status == 1:
                best = max(best, + prices[i] + helper(i+1, 2), helper(i+1, status))
            else:
                best = max(best, helper(i+1, 0))
            return best
        return helper(0, 0)


# This solution works - optimization: one less recursion by only keeping track of 2 states and skipping one more


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # status: 0 can buy; 1 can sell; for cooldown just skip one more
        @lru_cache(None)
        def helper(i, status):
            if i > len(prices)-1:
                return 0
            best = float('-inf')
            if status == 0:
                best = max(best, - prices[i] + helper(i+1, 1), helper(i+1, status))
            elif status == 1:
                best = max(best, + prices[i] + helper(i+2, 0), helper(i+1, status))
            return best
        return helper(0, 0)
                