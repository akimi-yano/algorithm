# 121. Best Time to Buy and Sell Stock
# Easy

# 6050

# 265

# Add to List

# Share
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# This solution works :) (after 8 months later ! [I initially could not solve this problem ! 8 months ago]
#  I can solve this now and its very quick !)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        buy at cheaper price
        sell at more expensive price
        buy - > sell
        '''
        if not prices:
            return 0
        buy = sell = prices[0]
        max_profit = sell-buy
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
            else:
                if prices[i] > sell:
                    sell = prices[i]
            max_profit = max(max_profit, sell-buy)
        return max_profit