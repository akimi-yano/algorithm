# 1616. Split Two Strings to Make Palindrome
# Medium

# 38

# 76

# Add to List

# Share
# You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

# When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

# Return true if it is possible to form a palindrome string, otherwise return false.

# Notice that x + y denotes the concatenation of strings x and y.

 

# Example 1:

# Input: a = "x", b = "y"
# Output: true
# Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
# aprefix = "", asuffix = "x"
# bprefix = "", bsuffix = "y"
# Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
# Example 2:

# Input: a = "abdef", b = "fecab"
# Output: true
# Example 3:

# Input: a = "ulacfd", b = "jizalu"
# Output: true
# Explaination: Split them at index 3:
# aprefix = "ula", asuffix = "cfd"
# bprefix = "jiz", bsuffix = "alu"
# Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
# Example 4:

# Input: a = "xbdef", b = "xecab"
# Output: false
 

# Constraints:

# 1 <= a.length, b.length <= 105
# a.length == b.length
# a and b consist of lowercase English letters


# This approach does not work :

# class Solution:
#     def checkPalindromeFormation(self, a: str, b: str) -> bool:
#         '''
#         same length
#         split them at the same IDX
#         '''
#         for i in range(len(a)+1):
#             a_pre = a[:i]
#             a_suf = a[i:]
#             b_pre = b[:i]
#             b_suf = b[i:]
#             # print(i,a_pre,a_suf)
#             # print(i,b_pre,b_suf)
#             # str1 = a_pre + b_suf
#             # str2 = b_pre + a_suf
#             # print(str1, str2)
#             if self.is_palindrome(a_pre,b_suf,i) or self.is_palindrome(b_pre,a_suf,i):
#                 return True
#         return False
    
#     def is_palindrome(self, pre, suf, idx):
#         # prefix = pre[:idx]
#         # suffix = suf[idx:]
#         # print(prefix,suffix)
#         # string = prefix + suffix
#         # length = len(string)
#         # print(pre, suf, idx)
#         string = pre + suf
#         left = 0
#         right = len(string)-1
#         # print(string, idx)
#         while left < right :
#             if string[left] != string[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True


# This solution works !!!
'''
check for both cases: left for a and right for b & left for b and right for a
check if they are palin and extract the parts that are not 
check if they themselves are palindrome
if any of them are, return True
'''

# Time O(N), Space O(N)

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        left = 0
        right = len(a) - 1
        
        while left < right and a[left] == b[right]:
            left += 1
            right -= 1
            
        s1 = a[left: right + 1]
        s2 = b[left: right + 1]

        left = 0
        right = len(a) - 1
        
        while left < right and b[left] == a[right]:
            left += 1
            right -= 1
        
        s3 = a[left: right + 1]
        s4 = b[left: right + 1]

        return any(s == s[::-1] for s in (s1,s2,s3,s4))