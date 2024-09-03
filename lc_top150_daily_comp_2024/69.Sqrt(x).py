'''
69. Sqrt(x)
Easy
Topics
Companies
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
'''

# This approach works:

class Solution:
    def mySqrt(self, x: int) -> int:

        def is_invalid(val):
            return (val * val) > x

        left = 0
        right = x
        while left < right:
            mid = (left+right+1)//2
            if is_invalid(mid):
                right = mid-1
            else:
                left = mid
        return left
    
# Time: O(logX)
# Space: O(1)