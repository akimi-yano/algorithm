# 5. Longest Palindromic Substring
# Medium

# 9410

# 631

# Add to List

# Share
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),

# This solution works

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(start, end):
            if end > len(s)-1:
                return 0, ""
            if s[start] != s[end]:
                return 0, ""
            while start > -1 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            start +=1
            end -=1
            return (end - start + 1), s[start:end+1]
        
        best_length = 0
        ans = ""
        for mid in range(len(s)):
            a_l,a_s = is_palindrome(mid, mid) 
            b_l, b_s = is_palindrome(mid, mid+1)
            if a_l > 0 and best_length < a_l:
                best_length = a_l
                ans = a_s
            if b_l > 0 and best_length < b_l:
                best_length = b_l
                ans = b_s
        return ans
        
# This solution works:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(start, end):
            if end > len(s)-1:
                return 0, ""
            if s[start] != s[end]:
                return 0, ""
            while start > -1 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            start +=1
            end -=1
            return (end - start + 1), s[start:end+1]
        
        best_length = 0
        ans = ""
        for mid in range(len(s)):
            a_l,a_s = is_palindrome(mid, mid) 
            b_l, b_s = is_palindrome(mid, mid+1)
            if best_length < a_l:
                best_length = a_l
                ans = a_s
            if best_length < b_l:
                best_length = b_l
                ans = b_s
        return ans
            
# This solution works - opmitization

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(start, end):
            if end > len(s)-1:
                return 0, -1, -1
            if s[start] != s[end]:
                return 0, -1, -1
            while start > -1 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            start +=1
            end -=1
            return (end - start + 1), start, end
        
        best_length = 0
        start = end = -1
        for mid in range(len(s)):
            a_l,a_s, a_e = is_palindrome(mid, mid) 
            b_l, b_s, b_e = is_palindrome(mid, mid+1)
            if best_length < a_l:
                best_length = a_l
                start = a_s
                end = a_e
            if best_length < b_l:
                best_length = b_l
                start = b_s
                end = b_e
        return s[start:end+1]
            