'''
7. Reverse Integer
Medium
10.7K
12.2K
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        '''
        Input: x = 120
        Output: 21
        
        divmod() function returns a tuple which contains a pair of the quotient and the remainder like (quotient, remainder).
        - For integers, the return value is the same as (a // b, a % b).
        - For floating point numbers the return value is (q, a % b), where q is usually math.floor(a / b) which is the whole part of the quotient.
        '''
        MAX = 2**31 - 1
        MIN = -2**31
        
        negative = False
        if x < 0:
            negative = True
            x *= -1
            
        total = 0
        while x:
            total *= 10
            val, remainder = divmod(x, 10)
            total += remainder
            x = val
        
        if negative:
            total = -total
        return total if MIN <= total <= MAX else 0