# 12. Integer to Roman
# Medium

# 1611

# 3068

# Add to List

# Share
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

 

# Example 1:

# Input: num = 3
# Output: "III"
# Example 2:

# Input: num = 4
# Output: "IV"
# Example 3:

# Input: num = 9
# Output: "IX"
# Example 4:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= num <= 3999

# This solution works:

class Solution:
    def intToRoman(self, num: int) -> str:
        memo = {
        1 : 'I',
        5 : 'V',
        10 : 'X',
        50 : 'L',
        100 : 'C',
        500 : 'D',
        1000 : 'M',
        4: 'IV',
        9: 'IX',
        40: 'XL',
        90: 'XC',
        400: 'CD',
        900: 'CM'
        }
        ans = []
        digit = 1 
        while num:
            val = num % 10
            if val * digit in memo:
                ans.append(memo[val*digit])
            else:
                temp = val * digit
                if (val* digit) >= (digit * 5):
                    temp = (val * digit) - (digit * 5)
                while temp:
                    ans.append(memo[digit]) 
                    temp -= digit
                if (val * digit) >= (digit * 5):
                    ans.append(memo[digit * 5])
            digit *= 10
            num //= 10
        ans.reverse()
        return "".join(ans)
        