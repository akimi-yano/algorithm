#  Valid Palindrome

#  Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false
 

# Constraints:

# s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<2:
            return True
        new_str = s.lower()
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        alpha_set = set(list(alpha))
        left = 0
        right=len(new_str)-1
        while left<=right:
            if new_str[left] not in alpha_set:
                left+=1
            elif new_str[right] not in alpha_set:
                right-=1  
            elif new_str[left] != new_str[right]:
                return False
            else:
                left+=1
                right-=1
        return True
         
# used regex !           
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub('[^A-Za-z0-9]+','',s)
        s=s.lower()
        for i in range(len(s)):
            if s[i]!=s[~i]:
                return False
        return True
                