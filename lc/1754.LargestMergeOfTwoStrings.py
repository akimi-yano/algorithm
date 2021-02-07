# 1754. Largest Merge Of Two Strings
# Medium

# 52

# 23

# Add to List

# Share
# You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:

# If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
# For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".
# If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
# For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".
# Return the lexicographically largest merge you can construct.

# A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.

 

# Example 1:

# Input: word1 = "cabaa", word2 = "bcaaa"
# Output: "cbcabaaaaa"
# Explanation: One way to get the lexicographically largest merge is:
# - Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
# - Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
# - Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
# - Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
# - Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
# - Append the remaining 5 a's from word1 and word2 at the end of merge.
# Example 2:

# Input: word1 = "abcabc", word2 = "abdcaba"
# Output: "abdcabcabcaba"
 

# Constraints:

# 1 <= word1.length, word2.length <= 3000
# word1 and word2 consist only of lowercase English letters.


# This solution works:

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        '''
        separate recursion comparison part (+lru_cache) and constructing string array part :)
        '''
        @lru_cache(None)
        def helper(a_i, b_i):
            if a_i > len(word1)-1:
                return False
            if b_i > len(word2)-1:
                return True
            if word1[a_i] > word2[b_i]:
                return True
            if word1[a_i] < word2[b_i]:
                return False
            return helper(a_i+1, b_i+1)
        
        ans = []
        idx1 = idx2 = 0
        while idx1 < len(word1) or idx2 < len(word2):
            if helper(idx1, idx2):
                ans.append(word1[idx1])
                idx1+=1
            else:
                ans.append(word2[idx2])
                idx2+=1
        return "".join(ans)
    
    
# This approach does not work:

# class Solution:
#     def largestMerge(self, word1: str, word2: str) -> str:
#         # ans = []
#         # idx1 = idx2 = 0
#         # while idx1 < len(word1) and idx2 < len(word2):
#         #     if word1[idx1] > word2[idx2]:
#         #         ans.append(word1[idx1])
#         #         idx1 += 1
#         #     else:
#         #         ans.append(word2[idx2])
#         #         idx2 += 1
        
#         @lru_cache(None)
#         def helper(idx1, idx2):
#             ans = []
#             if idx1 > len(word1)-1 and idx2 > len(word2)-1:
#                 return [ans]
#             elif idx1 > len(word1)-1:
#                 ans.extend([word2[idx2]] + arr for arr in helper(idx1, idx2+1))
#             elif idx2 > len(word2)-1:
#                 ans.extend([word1[idx1]] + arr for arr in helper(idx1+1, idx2))
#             else:
#                 if word1[idx1] < word2[idx2]:
#                     ans.extend([word2[idx2]] + arr for arr in helper(idx1, idx2+1))
#                 elif word1[idx1] > word2[idx2]:
#                     ans.extend([word1[idx1]] + arr for arr in helper(idx1+1, idx2))
#                 else:
#                     option1 = []
#                     option1.extend([word1[idx1]] + arr for arr in helper(idx1+1, idx2))
#                     option2 = []
#                     option2.extend([word2[idx2]] + arr for arr in helper(idx1, idx2+1))
#                     ans.extend(max(option1, option2))
#             return ans
#         return "".join(helper(0, 0)[0])
        

# This approach does not work:

# class Solution:
#     def largestMerge(self, word1: str, word2: str) -> str:
#         ans = []
#         idx1 = idx2 = 0
#         while idx1 < len(word1) and idx2 < len(word2):
#             if word1[idx1] > word2[idx2]:
#                 ans.append(word1[idx1])
#                 idx1 += 1
#             elif word1[idx1] < word2[idx2]:
#                 ans.append(word2[idx2])
#                 idx2 += 1
#             else:
#                 temp1 = idx1
#                 temp2 = idx2
#                 while temp1 < len(word1) and temp2 < len(word2) and word1[temp1] == word2[temp2]:
#                     temp1+=1
#                     temp2+=1
#                 if temp1 < len(word1) and temp2 < len(word2) and word1[temp1] > word2[temp2]:
#                     for i in range(idx1, temp1+1):
#                         ans.append(word1[i])
#                     idx1 = temp1
#                 elif temp1 < len(word1) and temp2 < len(word2) and word1[temp1] < word2[temp2]:
#                     for i in range(idx2, temp2+1):
#                         ans.append(word1[i])
#                     idx2 = temp2
    
                    
#         return "".join(ans)
        