# 600. Non-negative Integers without Consecutive Ones
# Hard

# 828

# 96

# Add to List

# Share
# Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

 

# Example 1:

# Input: n = 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
# Example 2:

# Input: n = 1
# Output: 2
# Example 3:

# Input: n = 2
# Output: 3
 

# Constraints:

# 1 <= n <= 109

# This solution works:

class Solution:
    def findIntegers(self, n: int) -> int:
        highest_bit = 1
        while highest_bit << 1 <= n:
            highest_bit <<= 1
        
        '''
        n = 8
            1 0 0 0
            1 0 0...
            1 0 1... x
            0 0...
            0 1...
            
        n = 10
            1 0 1 0
            
            1 0 0...
            1 0 1... o
            1 0 0 0 o
            1 0 0 1 ?
            
            
        95
        90 o
        ...
        95 o
        96 x
        '''
        @lru_cache(None)
        # prev = the last bit value chosen
        def helper(prev, bit):
            nonlocal n
            # base case
            if not bit:
                return 1
    
            if prev:
                if bit & n:
                    return helper2(0, bit >> 1)
                else:
                    return helper(0, bit >> 1)
            else:
                if bit & n:
                    return helper(1, bit >> 1) + helper2(0, bit >> 1)
                else:
                    return helper(0, bit >> 1)
                
        
        @lru_cache(None)
        def helper2(prev, bit):
            if not bit:
                return 1
            if prev:
                return helper2(0, bit >> 1)
            else:
                return helper2(1, bit >> 1) + helper2(0, bit >> 1)
        
        return helper(0, highest_bit)