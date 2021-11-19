# 461. Hamming Distance
# Easy

# 2515

# 186

# Add to List

# Share
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1
 

# Constraints:

# 0 <= x, y <= 231 - 1


# This solution works:


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        1   (0 0 0 1)
        4   (0 1 0 0)
               #   #
        '''
        ans = 0
        cur = 1
        while cur <= max(x, y):
            if x&cur:
                if not y&cur:
                    ans += 1
            else:
                if y&cur:
                    ans += 1
            cur <<= 1
        return ans
                
            
# This solution works - optimization:


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        1   (0 0 0 1)
        4   (0 1 0 0)
               #   #
        '''

        ans = 0
        while x or y:
            if (x ^ y) & 1:
                ans += 1
            x >>= 1
            y >>= 1
        return ans
            
