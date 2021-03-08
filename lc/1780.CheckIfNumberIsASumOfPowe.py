# 1780. Check if Number is a Sum of Powers of Three
# Medium

# 51

# 2

# Add to List

# Share
# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.

 

# Example 1:

# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32
# Example 2:

# Input: n = 91
# Output: true
# Explanation: 91 = 30 + 32 + 34
# Example 3:

# Input: n = 21
# Output: false
 

# Constraints:

# 1 <= n <= 107

# This solution works:
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        '''
        1 make the cur larger than or equal to n by multiplying by 3
        2 if (n-cur) >= 0, meaning that if you can subtract cur from n and the remaining is larger  than or equal to 0, then subtract
        3 divide cur by 3 by integer division
        4 at the end, check if n == 0
        if n is not 0, it means we had to subtract something twice, so it is not "distinct"
        '''
        cur = 1
        while n > cur:
            cur *= 3
        
        while cur:
            if (n - cur) >= 0:
                n -= cur
            cur //= 3
        
        return n == 0