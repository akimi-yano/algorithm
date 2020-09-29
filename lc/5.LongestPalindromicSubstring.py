# 5. Longest Palindromic Substring
# Medium

# 8099

# 576

# Add to List

# Share
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"



# This solution works - review :
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        best = ''
        start_idx=0
        end_idx=0

        # case 1: odd number
        for middle in range(len(s)):
            start_idx = middle
            end_idx=middle
            
            # keep on moving start & end index if it is a palindrome
            while start_idx > 0 and end_idx < len(s) - 1 \
            and s[start_idx - 1] == s[end_idx + 1]:
                start_idx -= 1
                end_idx += 1
            
            if len(best) < end_idx - start_idx + 1:
                best = s[start_idx:end_idx+1]
        
        for middle in range(len(s)):
            start_idx = middle
            end_idx = middle - 1
            # keep on moving start & end index if it is a palindrome
            while start_idx > 0 and end_idx < len(s) - 1 \
            and s[start_idx - 1] == s[end_idx + 1]:
                start_idx -= 1
                end_idx += 1
            
            if len(best) < end_idx - start_idx + 1:
                best = s[start_idx:end_idx+1]
                
        return best
        