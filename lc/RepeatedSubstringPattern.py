# Repeated Substring Pattern
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

# Example 1:

# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:

# Input: "aba"
# Output: False
# Example 3:

# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
'''
Input: "abab"
Output: True

a
b
ab
ba
aba
bab
abab
        
----

Input: "aba"
Output: False

a
b
ab
ba
aba

----

Input: "abcabcabcabc"
Output: True

a
b
c
ab
bc
ca
abc
bca
cab
abca
bcab
cabc

----

abcd
a
b

...

'''
# This does not work - Brute Force: TLEed on 56 / 120 test cases passed.    

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         options = set([])
#         for i in range(len(s)):
#             for j in range(i+1, len(s)):
#                 options.add(s[i:j])
#         # print(options)
#         length = len(s)
#         for option in options:
#             temp = option
#             while length > len(temp):
#                 # print(option)
#                 temp += option
#             # print(temp,s)
#             if temp == s:
#                 return True
        # return False
                

# This does not owrk - Memory Limit Exceeded 

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         options = set([])
#         for i in range(len(s)):
#             for j in range(i+1, len(s)):
#                 options.add(s[i:j])
#         length = len(s)
#         for option in options:
#             temp = option
#             while length > len(temp):
#                 temp += option
#             # added
#             if len(temp) == len(s) and temp == s:
#                 return True
#         return False


# nice 1 liner 

def repeatedSubstringPattern(self, str):
    return str in (2 * str)[1:-1]



# Solution 1
# Just check all posible divisors of lenght of s, replicate them and compare them with original string. If we have found it, we return True, if we reached the end and we did not find any, we return False.

# Complexity: time complexity is O(n*sqrt(n)), because we have no more than O(sqrt(n)) divisors of number n (we can split them into pairs, where one number in pair will be <sqrt(n). Space compexity is O(n).

class Solution:
    def repeatedSubstringPattern(self, s):
        N = len(s)
        for i in range(1, N//2+1):
            if N % i == 0 and s[:i]* (N//i) == s:
                return True
        return False
# Solution 2
# But wait, there is more! There is in fact very short and interesting solution. Let us replicate our sting, remove first and last elements and try to find original string: for example:

# s = abcdabcd, then we have bcdabcdabcdabc, where we can find abcdabcd inside. It is a bit more difficult to prove, that opposite is true: if we found substring it will mean that we have repeated substring pattern. I will add proof a bit later.

# Complexity: time complexity is basically O(n), because we can find substrings in linear time. In python function in will work, using Boyer–Moore algorithm, which is in average work in linear time (if you do not like average, you can use KMP, which have worst linear time, not average). Space complexity is O(n).
class Solution:
    def repeatedSubstringPattern(self, s):
        return s in (s+s)[1:-1]
    
    
# Solution! 
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # replicate our sting, remove first and last elements and try to find original string
        return s in (s+s)[1:-1]