# 647. Palindromic Substrings
# Medium

# 3977

# 134

# Add to List

# Share
# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:

# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
 

# Example 2:

# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Note:

# The input string length won't exceed 1000.
 


# This approach does not work - TLE:

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def is_palindrome(start, end):
#             while start < end:
#                 if s[start] != s[end]:
#                     return False
#                 start += 1
#                 end -= 1
#             return True
#         count = 0
#         for start in range(len(s)):
#             for end in range(start, len(s)):
#                 if is_palindrome(start, end):
#                     count += 1
#         return count


# This solution works:

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for mid in range(len(s)):
            left = right = mid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        for mid in range(len(s)):
            left = mid
            right = mid + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans



# This solution works:

class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(start, end):
            count = 0
            while start > -1 and end < len(s) and s[start] == s[end]:
                count +=1
                start -= 1
                end += 1
            return count
        
        ans = 0
        for mid in range(len(s)):
            ans += is_palindrome(mid, mid)
            ans += is_palindrome(mid, mid+1)
        return ans