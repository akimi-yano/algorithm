# 1648. Sell Diminishing-Valued Colored Balls
# Medium

# 63

# 13

# Add to List

# Share
# You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

# The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

# You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

# Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

 

# Example 1:


# Input: inventory = [2,5], orders = 4
# Output: 14
# Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
# The maximum total value is 2 + 5 + 4 + 3 = 14.
# Example 2:

# Input: inventory = [3,5], orders = 6
# Output: 19
# Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
# The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
# Example 3:

# Input: inventory = [2,8,4,10,6], orders = 20
# Output: 110
# Example 4:

# Input: inventory = [1000000000], orders = 1000000000
# Output: 21
# Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.
 

# Constraints:

# 1 <= inventory.length <= 105
# 1 <= inventory[i] <= 109
# 1 <= orders <= min(sum(inventory[i]), 109)

# This approach does not work :

# class Solution:
#     MOD  =  10 ** 9 +7
#     def maxProfit(self, inventory: List[int], orders: int) -> int:
#         memo = {}
#         def helper(i, remaining_orders, arr):
#             key = (i,  remaining_orders)
#             if  key in  memo:
#                 return  memo[key]
#             if remaining_orders <= 0 or i > len(inventory)-1:
#                 memo[key] = 0
#                 return 0 
#             max_profit = float('-inf')
    
#             if  arr[i] >=1:
#                 temp = arr
#                 val = temp[i]
#                 temp[i] -=1
#                 max_profit = max(max_profit, val + helper(i, remaining_orders-1, temp))
#             max_profit = max(max_profit, + helper(i+1, remaining_orders, arr))
#             memo[key] = max_profit
#             return max_profit
            
        
#         return helper(0, orders,  inventory) % Solution.MOD
        
# This solution works:

class Solution:
    MOD  =  10 ** 9 +7
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort()
        price = inventory.pop()
        count = 1
        
        ans = 0
        while orders > 0 and price > 0:
            while inventory and inventory[-1] == price:
                inventory.pop()
                count += 1
            # print(inventory, price, count, orders)
            next_price = inventory[-1] if len(inventory) else 0
            num_reduce = min(orders // count, price - next_price)
            ans += self.helper(price, price-num_reduce, count)
            orders -= count * num_reduce
            price -= num_reduce
            if price > next_price:
                ans += price * orders
                orders = 0
        
        return ans % Solution.MOD
            
    def helper(self, upper, lower, count):
        return ((upper*(upper + 1)//2) - (lower*(lower+1)//2)) * count
        
        
        
        
        
        '''
        [100] 20
        
        100 + 99 + 98 + ... + 81
        81 + ... + 100
        
        
        n(n+1)/2
        1 + 2 + 3 + ... + n
        
        n1 = 80, n2 = 100
        
        n1: 1 + ... + 80
        n2: 1 + ... + 100
        
        (1 + ... + 100) - (1 + ... + 80)
        n2(n2+1)/2 - n1(n1+1)/2
        
        [100, 97, 93, 90]
        cur_num = 100
        count = 1
        
        cur_num = 99
        count = 1
        
        ...
        
        cur_num = 97
        count = 2
        
        cur_num = 96
        count = 2
        
        ...
        
        cur_num = 93
        count = 3
        
        ...
        
        
        '''


