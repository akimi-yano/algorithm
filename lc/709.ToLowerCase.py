# 709. To Lower Case
# Easy

# 739

# 1969

# Add to List

# Share
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

# Example 1:

# Input: s = "Hello"
# Output: "hello"
# Example 2:

# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"
 

# Constraints:

# 1 <= s.length <= 100
# s consists of printable ASCII characters.

# This solution works:

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

# This solution works:

class Solution:
    def toLowerCase(self, s: str) -> str:
        
        # print(ord('A')) 65
        # print(ord('Z')) 90
        
        # print(ord('a')) 97
        # print(ord('z')) 122
        
        slist = list(s)
        for i, c in enumerate(slist):
            num = ord(c)
            if 65 <= num <= 90:
                slist[i] = chr(ord('a') + (num - ord('A')))
        return "".join(slist)