# 441. Arranging Coins
# We need 1 coin for first level, 2 coins for second level and so on. So, 
# if we have s layers, we need exactly 1+2+...+s = s*(s+1)/2 coins. 
# Reformulating problem statement, we need to find the biggest s, 
# such that s*(s+1)/2 <= n or s^2 + s - 2n <= 0. This is quadratic inequality, 
# and to solve it we need to find roots of s^2 + s - 2n = 0 equation first:
# 

# Complexity: both time and space is O(1).

# Other solutions: we can do it in O(n) with linear search, if we just add level by level. 
# We can also use binary search with O(log n) complexity.

class Solution:
    def arrangeCoins(self, n):
        return int(sqrt(2*n + 0.25) - 0.5)