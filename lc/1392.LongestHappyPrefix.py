# 1392. Longest Happy Prefix
# Hard

# 251

# 16

# Add to List

# Share
# A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

# Given a string s. Return the longest happy prefix of s .

# Return an empty string if no such prefix exists.

 

# Example 1:

# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
# Example 2:

# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
# Example 3:

# Input: s = "leetcodeleet"
# Output: "leet"
# Example 4:

# Input: s = "a"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 10^5
# s contains only lowercase English letters.



# This solution does not work - TLEd !
# class Solution:
#     def longestPrefix(self, s: str) -> str:
#         prefix = set([])
#         suffix = set([])
        
#         temp = ""
#         for i in range(len(s)-1):
#             temp += s[i]
#             prefix.add(temp)
#         # print(prefix)
#         temp = []
#         for i in range(len(s)-1,0,-1):
#             temp.append(s[i])
#             suffix.add(''.join(reversed(temp)))
#         # print(suffix)
#         longest_length = 0
#         longest_ans = ""
#         for elem in prefix:
#             if elem in suffix and len(elem)>longest_length:
#                 longest_length = len(elem)
#                 longest_ans = elem
        
#         return longest_ans

# doesn't work - TLE

# class Solution:
#     def longestPrefix(self, s: str) -> str:
#         N = len(s)
#         left_i, right_i = 0, N - 1
#         left_val = right_val = 0
        
#         best_left = -1
#         right_multiplier = 1
#         for i in range(N - 1):
#             left_char, right_char = s[i], s[N-i-1]
#             left_val = left_val * 26 + (ord(left_char) - ord('a'))
#             right_val = (ord(right_char) - ord('a')) * right_multiplier + right_val
#             right_multiplier *= 26
#             if left_val == right_val:
#                 best_left = i

#         return s[:best_left+1]


# This solution works !!!: Incremental Hash or Rolling Hash approach

'''
process the character as an integer and keep adding to check if they are equal
just remember to mod cuz it gets a long number
don't calculate the multiplier each time but save it in the class variable 
IMPORTANT TO MOD - result will be the same because we're moding both left and right 
MPORTANT TO MOD - result will be the same because its multiplier - its same regardless of if multiplying before or after mod 
'''

class Solution:
    MOD = 10 ** 9 + 7
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        left_i, right_i = 0, N - 1
        left_val = right_val = 0
        
        best_left = -1
        right_multiplier = 1
        for i in range(N - 1):
            left_char, right_char = s[i], s[N-i-1]
            left_val = left_val * 26 + (ord(left_char) - ord('a'))
            right_val = (ord(right_char) - ord('a')) * right_multiplier + right_val
            right_multiplier *= 26
            
            # IMPORTANT TO MOD - result will be the same because we're moding both left and right 
            left_val %= Solution.MOD
            # IMPORTANT TO MOD - result will be the same because we're moding both left and right 
            right_val %= Solution.MOD
            # IMPORTANT TO MOD - result will be the same because its multiplier - its same regardless of if multiplying before or after mod 
            right_multiplier %= Solution.MOD
            
            if left_val == right_val:
                best_left = i

        return s[:best_left+1]
    
    
# There is also a solution with KMP algorithm !
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm