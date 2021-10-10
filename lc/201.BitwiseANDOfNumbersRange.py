# 201. Bitwise AND of Numbers Range
# Medium

# 1676

# 153

# Add to List

# Share
# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

# Example 1:

# Input: left = 5, right = 7
# Output: 4
# Example 2:

# Input: left = 0, right = 0
# Output: 0
# Example 3:

# Input: left = 1, right = 2147483647
# Output: 0
 

# Constraints:

# 0 <= left <= right <= 231 - 1


# This solution works:


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        shift = 0
        
        # find the common MSB bits.
        while m != n:
            
            m = m >> 1
            n = n >> 1
        
            shift += 1
        
        
        return m << shift