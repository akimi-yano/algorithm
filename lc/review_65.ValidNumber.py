# 65. Valid Number
# Hard

# 93

# 251

# Add to List

# Share
# A valid number can be split up into these components (in order):

# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# At least one digit, followed by a dot '.'.
# At least one digit, followed by a dot '.', followed by at least one digit.
# A dot '.', followed by at least one digit.
# An integer can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# At least one digit.
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

# Given a string s, return true if s is a valid number.

 

# Example 1:

# Input: s = "0"
# Output: true
# Example 2:

# Input: s = "e"
# Output: false
# Example 3:

# Input: s = "."
# Output: false
# Example 4:

# Input: s = ".1"
# Output: true
 

# Constraints:

# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.


# This solution works:

class Solution:
    def isNumber(self, s: str) -> bool:
        s_list = s.lower().split("e")

        if len(s_list) > 2:
            return False
        
        if len(s_list) == 2:
            power = s_list.pop()
            if len(power) < 1:
                return False
            if power[0] in ['+', '-']:
                power = power[1:]
            if not power.isnumeric():
                return False
        
        number = s_list.pop()
        
        s_list2 = number.split('.')
        
        if len(s_list2) > 2:
            return False
        
        decimal = ''
        if len(s_list2) == 2:
            decimal = s_list2.pop()
            if decimal and not decimal.isnumeric():
                return False
        
        integer = s_list2.pop()
        
        if len(integer) > 0 and integer[0] in ['+', '-']:
            integer = integer[1:]
        if integer and not integer.isnumeric():
            return False
        
        return len(integer) > 0 or len(decimal) > 0