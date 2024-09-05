'''
58. Length of Last Word
Solved
Easy
Topics
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

# This approach works:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
# Time: O(N)
# Space:O(N)

# Small optimization:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
            else:
                break
        count = 0
        while i >= 0:
            if s[i] != ' ':
                count += 1
                i -= 1
            else:
                break
        return count
# Time: O(N)
# Space: O(1)