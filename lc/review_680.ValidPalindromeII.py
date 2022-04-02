# 680. Valid Palindrome II
# Easy

# 4266

# 254

# Add to List

# Share
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.


# This solution works:


class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        @lru_cache(None)
        def helper(left, right, removed):
            if left >= right:
                return True
            
            ans = False 
            if s[left] == s[right]:
                ans |= helper(left+1, right-1, removed)
            else:
                if not removed:
                    ans |= helper(left+1, right, True)
                    ans |= helper(left, right-1, True)
                else:
                    return False
            return ans
        
        return helper(0, len(s)-1, False)