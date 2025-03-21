'''
13. Roman to Integer
Solved
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

# This approach works"

class Solution:
    def romanToInt(self, s: str) -> int:
        chars = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev = None
        total = 0
        for c in s:
            if (prev == 'I' and c in ('V', 'X')) or (prev == 'X' and c in ('L', 'C')) or (prev == 'C' and c in ('D', 'M')):
                total -= chars[prev]
                total += chars[c]-chars[prev]
            else:
                total += chars[c]
            prev = c
        return total

# Time: O(N)
# Space: O(1)

# This approach works and more elegant:

class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        The Roman numbers: 
        - when a smaller value appears before a larger value, it represents subtraction, 
        - while when a smaller value appears after or equal to a larger value, it represents addition.
        '''
        total = 0
        chars = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i < len(s)-1 and chars[s[i]] < chars[s[i+1]]:
                total -= chars[s[i]]
            else:
                total += chars[s[i]]
        return total