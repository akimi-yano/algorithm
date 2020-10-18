# 188. Best Time to Buy and Sell Stock IV
# Hard

# 1886

# 116

# Add to List

# Share
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# Design an algorithm to find the maximum profit. You may complete at most k transactions.

# Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


# Constraints:

# 0 <= k <= 109
# 0 <= prices.length <= 104
# 0 <= prices[i] <= 1000



# This approach does not work:

# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         memo = {}
        
#         def helper(remaining, i, status, cur):
#             key = (remaining, i, status, cur)
#             if key in memo:
#                 return memo[key]
            
#             if i > len(prices)-1 or remaining == 0:
#                 memo[key] = 0
#                 return 0
#             max_profit = 0
            
#             if status == 0:
#                 max_profit = max(max_profit, helper(remaining, i+1, status, cur), cur-prices[i] + helper(remaining -1, i+1, 1, cur - prices[i]))
            
#             elif status == 1:
#                 max_profit = max(max_profit, helper(remaining, i+1, status, cur), cur+prices[i] + helper(remaining -1, i+1, 0, cur + prices[i]))
#             memo[key] = max_profit
#             return max_profit
            
#         return helper(k, 0, 0, 0)



# This approach does not work:

# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         memo = {}
        
#         def helper(remaining, i, status):
            
#             if i > len(prices)-1 or remaining == 0:
#                 return 0
            
#             max_profit = 0
            
#             if status == 0:
#                 max_profit = max(max_profit, helper(remaining, i+1, status), max_profit-prices[i] + helper(remaining -1, i+1, 1))
            
#             else:
#                 max_profit = max(max_profit, helper(remaining, i+1, status),  max_profit+prices[i] + helper(remaining -1, i+1, 0))

#             return max_profit
            
#         return helper(k, 0, 0)



# This solution works !

'''
HARD problem requires you to first understand why it is hard ?: 
(1) it's ambigous what it takes to be 1 transaction; 
(2) k is large so it will TLE if we don't handle the case k > len(prices)-1 saparately 
- what does it mean to have k larger than the length of prices ? it means we should use all the transactions as long as
it produces profits (greedy)

There are 2 cases:

if k > len(prices)-1 -> greedy - choose to do all the transactions that creates benefits 
as its unlimited (given the arr of size smaller than k) - no need to keep track of remaining 

else: -> dp - keep track of remaining to choose the one that gives max profit

Note: 1 transaction = buy + sell (dont' double count - buy buying and selling, it counts as 1 transaction)
Note: dont need to compare with max_profit because its initialized as 0
Note: k is large so we need to handle the case of k > len(prices)-1 so that it does not TLE
'''

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