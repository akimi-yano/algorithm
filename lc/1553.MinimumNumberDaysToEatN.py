# 1553. Minimum Number of Days to Eat N Oranges

# There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

# Eat one orange.
# If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
# If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
# You can only choose one of the actions per day.

# Return the minimum number of days to eat n oranges.

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: You have 10 oranges.
# Day 1: Eat 1 orange,  10 - 1 = 9.  
# Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
# Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
# Day 4: Eat the last orange  1 - 1  = 0.
# You need at least 4 days to eat the 10 oranges.
# Example 2:

# Input: n = 6
# Output: 3
# Explanation: You have 6 oranges.
# Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
# Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
# Day 3: Eat the last orange  1 - 1  = 0.
# You need at least 3 days to eat the 6 oranges.
# Example 3:

# Input: n = 1
# Output: 1
# Example 4:

# Input: n = 56
# Output: 6

# Constraints:

# 1 <= n <= 2*10^9

'''
This solution works !

Intuition
As pleasant as it seems, it does not make sense to just keep eating oranges one by one.

So, the real choice we have is to eat n % 2 oranges one-by-one and then swallow n / 2, or eat n % 3 oranges so that we can gobble 2 * n / 3.

As usual, we use DP to avoid re-computation. Since our numbers can be large, it's better to use a hash map instead of an array.

'''

class Solution:
    @lru_cache()
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min( n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3) )
    
    
'''
１＋　二個食べても　三個食べても　１日かかるから
二で割り切れる数にしてから二で割る　（その分たす：n % ２）か
三で割り切れる数にしてから三で割る　（その分たす：n % ３）か
'''

# Yay this works ! with helper and memo !

class Solution:
    def minDays(self, n: int) -> int:
        memo = {}
        def helper(num):   
            if num in memo:
                return memo[num]
            if num<=1:
                res = num
            else:
                res = 1 + min(num%2+helper(num//2),num%3+helper(num//3))
            memo[num] = res
            return res
        
        return helper(n)