# 633. Sum of Square Numbers
# Medium

# 955

# 420

# Add to List

# Share
# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

# Example 1:

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:

# Input: c = 3
# Output: false
# Example 3:

# Input: c = 4
# Output: true
# Example 4:

# Input: c = 2
# Output: true
# Example 5:

# Input: c = 1
# Output: true
 

# Constraints:

# 0 <= c <= 231 - 1


# This solution works:


import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        a**2 + b**2 = c
        a*a + b*b = c
        if a == b:
        a*a + a*a = c
        2*a*a = c which is the limit of what we need to check
        '''
        a = 0
        while 2*a*a <= c:
            b = math.sqrt(c-a*a) # can do (** 0.5) as well
            if int(b) ** 2 + a ** 2 == c:
                return True
            a += 1
        return False