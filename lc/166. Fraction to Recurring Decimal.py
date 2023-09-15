'''
166. Fraction to Recurring Decimal
Medium
2K
3.5K
Companies
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
        '''
        Notes: 
        When there is a repeating number after a dicimal point, it meants that the fraction has a repeating pattern. It does not end the repetition once it starts, so as soon as we find the end of repetition, we can close it with the closing palenthesis. So in the after dicimal point, as soon as there is a number we have see before, it is looping and it endlessly repeats.

        Approach:
        1) check the edge cases: are numerator zero? (The problem says that the denominator is not zero)
        2) check the edge cases: are numerator and denominator negative?
        3) add the integer part first
        4) handle the after dicimal point:
        5) return
           - find the beginning of the repetition
           - find the end of the repetition
           - add the repetition part with ()
        '''

        # 1) check the edge cases: are numerator zero? (The problem says that the denominator is not zero)
        if numerator == 0:
            return '0'

        # initialize the ans arr
        ans = []
        
        # 2) check the edge cases: are numerator and denominator negative?
        if (numerator < 0) ^ (denominator < 0):
            ans.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)

        # 3) add the integer part first
        ans.append(str(numerator // denominator))

        # check if there is a fractional part
        if numerator % denominator == 0:
            return ''.join(ans)
        
        # add .
        ans.append('.')

        # 4) handle the after dicimal point:
        # the following is for after the dicimal point
        remainder_dict = {} # {num : index}
        remainder = numerator % denominator #4
        
        while remainder != 0 and remainder not in remainder_dict:
            remainder_dict[remainder] = len(ans) # index

            # multiply the remainder with 10 as without that denominator is larger than remainder so no quotient value for this digigt (*visualizing like 筆算 helps)
            remainder *= 10 #40 -> 400 -> 670
            
            # now that the denominator is larger than remainder, we can get the quotient value for this digit, so do the integer divition to get the integer value for this digit and append it to the ans (*visualizing like 筆算 helps)
            ans.append(str(remainder // denominator)) #0 -> 1 -> 2
            
            # get the remainder to do the continuation of the calculation for the next digit by doing % (*visualizing like 筆算 helps)
            remainder %= denominator #40, 333, 40 -> 67, 333, 67-> 4, 333, 4
       
        # {4: 2, 40: 3, 67: 4}

        # 5) return
        # check if there is the repeating part 
        # find the beginning of the repetition
        # find the end of the repetition
        # add the repetion part with ()
        if remainder in remainder_dict:
            return ''.join(ans[:remainder_dict[remainder]]) + '(' + ''.join(ans[remainder_dict[remainder]:]) + ')'
        return ''.join(ans) 