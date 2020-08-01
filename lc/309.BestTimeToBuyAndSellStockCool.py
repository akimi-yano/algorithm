# 309. Best Time to Buy and Sell Stock with Cooldown


# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:

# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]





# this does not work -
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         sell=0
#         buy=0
#         profit=0
#         for i in range(len(prices)):
#             k=i%3
#             if k==0:
#                 buy = prices[i]
#             elif k==1:
#                 sell = prices[i]
#                 # print(k,sell,buy,profit)
#                 profit+=sell-buy
#             else:
#                 buy=0
#                 sell=0
#         return profit if profit>0 else 0



# The series of problems are typical dp. The key for dp is to find the variables to represent the states and deduce the transition function.

# Of course one may come up with a O(1) space solution directly, but I think it is better to be generous when you think and be greedy when you implement.

# The natural states for this problem is the 3 possible transactions : buy, sell, rest. Here rest means no transaction on that day (aka cooldown).

# Then the transaction sequences can end with any of these three states.

# For each of them we make an array, buy[n], sell[n] and rest[n].

# buy[i] means before day i what is the maxProfit for any sequence end with buy.

# sell[i] means before day i what is the maxProfit for any sequence end with sell.

# rest[i] means before day i what is the maxProfit for any sequence end with rest.

# Then we want to deduce the transition functions for buy sell and rest. By definition we have:

# buy[i]  = max(rest[i-1]-price, buy[i-1]) 
# sell[i] = max(buy[i-1]+price, sell[i-1])
# rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
# Where price is the price of day i. All of these are very straightforward. They simply represents :

# (1) We have to `rest` before we `buy` and 
# (2) we have to `buy` before we `sell`
# One tricky point is how do you make sure you sell before you buy, since from the equations it seems that [buy, rest, buy] is entirely possible.

# Well, the answer lies within the fact that buy[i] <= rest[i] which means rest[i] = max(sell[i-1], rest[i-1]). That made sure [buy, rest, buy] is never occurred.

# A further observation is that and rest[i] <= sell[i] is also true therefore

# rest[i] = sell[i-1]
# Substitute this in to buy[i] we now have 2 functions instead of 3:

# buy[i] = max(sell[i-2]-price, buy[i-1])
# sell[i] = max(buy[i-1]+price, sell[i-1])
# This is better than 3, but

# we can do even better

# Since states of day i relies only on i-1 and i-2 we can reduce the O(n) space to O(1). And here we are at our final solution:


# Python

def maxProfit(self, prices):
    if len(prices) < 2:
        return 0
    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell


# # Another solution
# The key is 3 states and 5 edges for state transition. 3 states are notHold (stock), hold (stock), and notHold_cooldown. The initial values of the latter two are negative infinity since they are meaningless, i.e. you won't hold stocks at first and there's no cooldown at first. The 5 edges:

# hold -----do nothing----->hold

# hold -----sell----->notHold_cooldown

# notHold -----do nothing -----> notHold

# notHold -----buy-----> hold

# notHold_cooldown -----do nothing----->notHold

# def maxProfit(self, prices):
#     notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
#     for p in prices:
#         hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
#     return max(notHold, notHold_cooldown)


# def max_profit(prices):
#     if len(prices)<=1:
#         return 0
#     A,B,C=0,-prices[0],0
    
#     for i in range(1, len(prices)):
#         tmp=A
#         A=max(A,C)
#         C=B+prices[i]
#         B=max(B,tmb-prices[i])
#     return max(A,C)
# print(max_profit())


# A  -> B  -> C  -> 
# H (B) H (S)   (H)



# BEST SOLUTION ! MOST INTUITIVE !!!

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(can_buy, i):
            key = (can_buy, i)
            if key in memo:
                return memo[key]

            ans = 0
            if i >= len(prices):
                ans = 0
            elif can_buy:
                bought = -prices[i]+helper(False, i+1)
                waited = helper(True, i+1)
                ans = max(bought, waited)
            else:
                sold = prices[i] + helper(True, i+2)
                waited = helper(False, i+1)
                ans = max(sold, waited)
            
            memo[key] = ans
            return ans
        
        return helper(True, 0)


#            can buy or cannot buy
# bought or waited          sold or waited