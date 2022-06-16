# 5. Longest Palindromic Substring
# Medium

# 18296

# 1084

# Add to List

# Share
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


# This solution works:


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
            nonlocal best
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                cur_len = right-left+1
                if len(best) < cur_len:
                    best = s[left:right+1]
                left -= 1
                right += 1
        
        best = ""
        for mid in range(len(s)):
            if mid != len(s)-1:
                helper(mid, mid+1)
            helper(mid, mid)
        return best