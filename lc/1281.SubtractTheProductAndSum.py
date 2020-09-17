# 1281. Subtract the Product and Sum of Digits of an Integer
# Easy

# 350

# 103

# Add to List

# Share
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# Example 2:

# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
 

# Constraints:

# 1 <= n <= 10^5


# This solution works !!!
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summation = 0 
        while n:
            val =  n%10
            prod *= val
            summation += val
            n //= 10
        return prod - summation
    
    
# Simplification :

    def subtractProductAndSum(self, n: int) -> int:
        sum, prod = 0, 1
        while n:
            n, digit = divmod(n, 10)
            sum += digit
            prod *= digit
        return prod - sum
# Analysis:
# Time: O(logn)    ---  because we are diving by something every time (10 in this case) (keep dividing) <-> opposite of exponential (keep multiplying)
# Space: O(1)