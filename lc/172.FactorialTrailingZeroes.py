# 172. Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:

# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.


class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        don't do factorial cuz its expensive (its almost worse than exponential)
        5's multiplier * even
        so just add the # of how many times you can divide the number by 5^i accendingly
        '''
        zeroes = 0
        factor = 5
        while n // factor > 0:
            zeroes += n // factor
            factor *= 5
        return zeroes
    
'''

//5
//25
//125
...

'''
