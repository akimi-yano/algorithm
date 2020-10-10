# 1071. Greatest Common Divisor of Strings
# Easy

# 567

# 140

# Add to List

# Share
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# Example 4:

# Input: str1 = "ABCDEF", str2 = "ABC"
# Output: ""


# Constraints:

# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


# This approach does not work : 


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         for k in range(len(str2),0,-1):
#             if len(str2) % k or len(str1) % k:
#                 continue
#             i = 0
#             invalid = False
#             while i <= len(str1)-1:
#                 if str1[i:i+len(str2[:k])] == str2[:k]:
#                     i += len(str2[:k])
#                 else:
#                     invalid = True
#                     break
#             if not invalid:
#                 return str2[:k]
#         return ""
                    


# This solution works: 

'''
check from the longest candidates 
make sure that both string's length are divisible by k (length % k == 0)
make a substring of either string and multiply by the length //k and compare with the string for both strings
substr * len(str1)//k == str1

str1:                ------

substr with k = 3 :  --- 
str1's length //3 :  ------
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for k in range(len(str2),0,-1):
            if len(str2) % k or len(str1) % k:
                continue
            substr = str1[:k]

            if substr * (len(str1)//k) == str1 and substr * (len(str2)//k) == str2:
                return substr

        return ""
                    