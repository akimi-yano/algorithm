# 231. Power of Two
# Easy

# 2235

# 260

# Add to List

# Share
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?


# This solution works:


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        1000
        4321

        4: 100
        3: 011
           000
        
        3: 011
        2: 010
           010
        
        '''
        return n > 0 and (n & (n-1)) == 0


# This solution works:


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        1000
        4321
        
        (n&~(n-1)) always return the binary number containing rightmost set bit as 1
        '''
        if n == 0:
            return False
        right_most_bit = n&~(n-1)
        return n == right_most_bit