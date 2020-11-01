# 1638. Count Substrings That Differ by One Character
# Medium

# 22

# 24

# Add to List

# Share
# Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

# For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

# Return the number of substrings that satisfy the condition above.

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: s = "aba", t = "baba"
# Output: 6
# Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# The underlined portions are the substrings that are chosen from s and t.
# ​​Example 2:
# Input: s = "ab", t = "bb"
# Output: 3
# Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# ​​​​The underlined portions are the substrings that are chosen from s and t.
# Example 3:
# Input: s = "a", t = "a"
# Output: 0
# Example 4:

# Input: s = "abe", t = "bbc"
# Output: 10
 

# Constraints:

# 1 <= s.length, t.length <= 100
# s and t consist of lowercase English letters only.


# This approach does not work !
'''
we cannot use counter as the order matters !!!!!!!
just keep track of start indexes and so that we dont do dup calculation 
'''

# from collections import Counter
# class Solution:
#     def countSubstrings(self, s: str, t: str) -> int:
#         ans = 0
        
#         for s_start in range(len(s)):
#             for s_end in range(s_start, len(s)):
#                 elem1 = s[s_start: s_end+1]
#                 count1 = Counter(elem1)
                
#                 for t_start in range(len(t)):
#                     for t_end in range(t_start, len(t)):
#                         elem2 = t[t_start: t_end+1]
#                         count2 = Counter(elem2)
                
#                         if count1 == count2:
#                             continue
#                         if len(elem1) != len(elem2):
#                             continue
                        
#                         # print(count1, count2)
#                         for k1, v1 in list(count1.items()):
#                             for k2, v2 in list(count2.items()):
#                                 if k1 in count2:
#                                     count2[k1] -= v1
                               
#                                 if k2 in count1:
#                                     count1[k2] -= v2
                        
#                         print(count1, count2)
#                         for k1, v1 in count1.items():
#                             for k1, v1 in count2.items():
#                                 if v1 <0:
#                                     break
#                                 if v2 <0:
#                                     break
#                         else:
#                             ans += 1
                        
                                        
#                         # Counter({'a': 2, 'b': 1}) Counter({'b': 2, 'a': 1})
            
# #                         dict1 = count1-count2 
# #                         freq1 = list(dict1.values())
                        
# #                         dict2 = count2-count1
# #                         freq2 = list(dict2.values())
                        
# #                         if len(dict1) == 1 and freq1[0] == 1:
# #                             # print(elem1, elem2, dict1)
# #                             ans +=1 
                            
# #                         elif len(dict2) == 1 and freq2[0] == 1:
# #                             # print(elem1, elem2, dict2)
# #                             ans +=1 
                            
#         return ans
                        
            
            
# This solution works !

from collections import Counter
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        targets = Counter()
        for s_start in range(len(s)):
            for t_start in range(len(t)):
                # print(f'starting at {s_start} and {t_start}')
                scur = s_start
                tcur = t_start
                diff = 0
                while scur < len(s) and tcur < len(t) and diff < 2:
                    if s[scur] != t[tcur]:
                        # print(f'{s[scur]} != {t[tcur]}, adding diff')
                        diff += 1
                    # print(diff)
                    if diff == 1:
                        ans += 1
                    scur += 1
                    tcur += 1
        return ans
                        
            