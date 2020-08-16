# 123. Best Time to Buy and Sell Stock III

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# Example 2:

# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.



# yay this works ! - there might be better solutions !

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        state 0: trying to buy 1st stock
        state 1: trying to sell 1st stock
        state 2: trying to buy 2st stock
        state 3: trying to sell 2st stock
        '''
        memo = {}
        def helper(i,state):
            key = (i,state)
            if key in memo:
                return memo[key]
            ans = 0
            if 0<=i<=len(prices)-1 and 0<=state<=4:
                ans = max(helper(i+1,state),(prices[i]*(-1 if state%2==0 else 1))+helper(i+1,state+1))
            memo[key] = ans
            return ans
        return helper(0,0)


'''
Time O(N)
Space O(1)

The thinking is simple and is inspired by the best solution from Single Number II 
(I read through the discussion after I use DP).
Assume we only have 0 money at first;
4 Variables to maintain some interested 'ceilings' so far:
The maximum of if we've just buy 1st stock, if we've just sold 1nd stock, 
if we've just buy 2nd stock, if we've just sold 2nd stock.
Very simple code too and work well. I have to say the logic is simple than those in Single Number II.


public class Solution {
    public int maxProfit(int[] prices) {
        int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE;
        int release1 = 0, release2 = 0;
        for(int i:prices){                              // Assume we only have 0 money at first
            release2 = Math.max(release2, hold2+i);     // The maximum if we've just sold 2nd stock so far.
            hold2    = Math.max(hold2,    release1-i);  // The maximum if we've just buy  2nd stock so far.
            release1 = Math.max(release1, hold1+i);     // The maximum if we've just sold 1nd stock so far.
            hold1    = Math.max(hold1,    -i);          // The maximum if we've just buy  1st stock so far. 
        }
        return release2; ///Since release1 is initiated as 0, so release2 will always higher than release1.
    }
}

'''