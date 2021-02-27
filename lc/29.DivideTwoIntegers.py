# 29. Divide Two Integers
# Medium

# 1625

# 6496

# Add to List

# Share
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Note:

# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.


# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
# Example 3:

# Input: dividend = 0, divisor = 1
# Output: 0
# Example 4:

# Input: dividend = 1, divisor = 1
# Output: 1


# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0


# This solution  works:
'''
use stack
add twice to make it 2's multiple
if its  2'smultiple, the state is either use it or not use it - which is easier
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # the only edge case with the constraints
        if dividend == -(1<<31) and divisor == -1:
            return (1<<31)-1
        
        pos = True
        if min(dividend, divisor) < 0 and max(dividend,divisor) > 0:
            pos = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        # keep checking and making possible options until the number is larger than the dividend
        stack = [(divisor, 1)]
        while stack[-1][0] + stack[-1][0] <= dividend:
            old_val,  old_add = stack[-1]
            stack.append((old_val+old_val,old_add+old_add))

        # for each option, keep checking if we should use it or not use it
        count = 0
        while stack:
            val, add = stack.pop()
            if dividend >= val:
                dividend -= val
                count += add
        return count if pos else -count