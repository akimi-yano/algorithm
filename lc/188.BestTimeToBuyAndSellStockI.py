# 188. Best Time to Buy and Sell Stock IV
# Hard

# 4746

# 167

# Add to List

# Share
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

# Constraints:

# 0 <= k <= 100
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000


# This solution works:


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        def greedy_helper(i, status):
            key = i, status
            if key in greedymemo:
                return greedymemo[key]
            max_profit = 0
            if i > len(prices) - 1:
                pass
            elif status == 0:
                max_profit = max(greedy_helper(i+1, status), -prices[i] + greedy_helper(i+1, 1))
            else:
                max_profit = max(greedy_helper(i+1, status), prices[i] + greedy_helper(i+1, 0))
            greedymemo[key] = max_profit
            return max_profit
        
        def dphelper(remaining, i, status):
            key = remaining, i, status
            if key in dpmemo:
                return dpmemo[key]
            
            max_profit = 0
            if i > len(prices)-1 or remaining == 0:
                pass
            elif status == 0:
                max_profit = max(dphelper(remaining, i+1, status),
                                 -prices[i] + dphelper(remaining, i+1, 1))
            else:
                max_profit = max(dphelper(remaining, i+1, status),
                                 prices[i] + dphelper(remaining -1, i+1, 0))
            dpmemo[key] = max_profit
            return max_profit

        greedymemo = {}
        dpmemo = {}
        if k >= len(prices):
            return greedy_helper(0, 0)
        return dphelper(k, 0, 0)