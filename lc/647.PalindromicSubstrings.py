# 647. Palindromic Substrings
# Medium

# 3066

# 124

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





# THIS APPROACH DOES NOT WORK: because going to the right side could open up new opportunity for preoviously disregarded left ones

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         '''
#         Input: "abc"
#         Output: 3
#         Explanation: Three palindromic strings: "a", "b", "c".


#         Example 2:

#         Input: "aaa"
#         Output: 6
#         Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
        
#         '''
#         def is_palindrome(start, end):
#             while start <= end:
#                 if s[start] == s[end]:
#                     start += 1
#                     end -= 1
#                 else:
#                     return False
#             return True
        
#         ans = st = 0
        
#         for en in range(len(s)):
            
#             while st <= en and not is_palindrome(st, en):
#                 print(is_palindrome(st,en))
#                 st += 1 
#             ans  += en - st +1
        
#         return ans

# This approach does not work - TLEd !

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         '''
#         Input: "abc"
#         Output: 3
#         Explanation: Three palindromic strings: "a", "b", "c".


#         Example 2:

#         Input: "aaa"
#         Output: 6
#         Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
        
#         '''
#         def is_palindrome(start, end):
#             while start <= end:
#                 if s[start] == s[end]:
#                     start += 1
#                     end -= 1
#                 else:
#                     return False
#             return True
        
#         ans = 0
        
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if is_palindrome(i, j):
#                     ans +=1
#         return ans
            
            
# This solution works !

'''
think that there are 2 types of palindrome : odd and even
I choose a starting points and go outwards to increment the count of palindrome 
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        # it doesn't matter if length of s is odd or even, because substrings can be odd or even anyways

        def helper(start, end):
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
            return count

        ans = 0
        for i in range(len(s)):
            # odd palindromes starting at i
            ans += helper(i, i)
            # even palindromes starting at i & i+1
            ans += helper(i, i+1)
        return ans