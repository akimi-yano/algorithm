'''
121. Best Time to Buy and Sell Stock
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        since it is guarangteed to have at least 1 elem, lets buy on the very first day
        if the price is larger than the bought one, then sell (dont sell the diff is 0)
        if the price is smaller than the prev bought one, then lets buy that one
        '''
        best_profit = 0 # as we can also not do any transaction
        bought = prices[0] # since there is at least one elem
        for price in prices[1:]:
            if price > bought:
                # sell
                best_profit = max(best_profit, price-bought)
            elif price < bought:
                # buy this one
                bought = price
        return best_profit
