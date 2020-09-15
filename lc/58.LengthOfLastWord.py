# 58. Length of Last Word
# Easy

# 773

# 2696

# Add to List

# Share
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5


# This solution works !:

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        if len(s_list) == 0:
            return 0
        
        return len(s_list[-1])
    
    
    
# Another approach without split:
'''
We can just split our string, remove all extra spaces and return length of the last word, however we need to spend O(n) time for this, where n is length of our string. There is a simple optimization: let us traverse string from the end and:

find the last element of last word: traverse from the end and find first non-space symbol.
continue traverse and find first space symbol (or beginning of string)
return end - beg.
Complexity: is O(m), where m is length of part from first symbol of last word to the end. Space complexity is O(1).
'''
class Solution:
    def lengthOfLastWord(self, s):
        end = len(s) - 1
        while end > 0 and s[end] == " ": end -= 1
        beg = end
        while beg >= 0 and s[beg] != " ": beg -= 1
        return end - beg