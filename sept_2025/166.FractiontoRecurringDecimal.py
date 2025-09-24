'''
166. Fraction to Recurring Decimal
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        ans = []
        if (numerator < 0) ^ (denominator < 0):
            ans.append("-")
        
        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient, remainder = divmod(numerator, denominator)
        ans.append(str(quotient))
        if remainder == 0:
            return "".join(ans)
        
        ans.append(".")
        map_dict = {}
        while remainder != 0:
            if remainder in map_dict:
                ans.insert(map_dict[remainder], "(")
                ans.append(")")
                break

            map_dict[remainder] = len(ans)
            remainder *= 10
            ans.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(ans)