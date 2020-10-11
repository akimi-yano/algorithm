# 316. Remove Duplicate Letters
# Medium

# 1691

# 126

# Add to List

# Share
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.


# This approach does not work :

# from itertools import combinations 
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         uniques = set(s)
#         N = len(uniques)
#         arr = list(combinations(s, N))
#         # arr = ["".join(elem) for elem in arr]
#         candi = []
#         for elem in arr:
#             if len(set(elem)) == len(elem):
#                 candi.append(elem)  
                
#         candi.sort()
#         return "".join(candi[0])



# This solution works : 

from collections import deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indexes={}
        for i in range(len(s)):
            if s[i] not in indexes:
                indexes[s[i]] = deque([])
            indexes[s[i]].append(i)
        # print(indexes)
        
        ans = ''
        while len(indexes) > 0:
            chosen = None
            for candidate in sorted(indexes.keys()):
                for other in indexes.keys():
                    # if the candidate failed, set it to None and break
                    if indexes[other][-1] < indexes[candidate][0]:
                        candidate = None
                        break
                if candidate is not None:
                    chosen = candidate
                    break
            ans += chosen
            # remove indexes that are before the chosen one's index
            for other_indexes in indexes.values():
                while other_indexes[0] < indexes[chosen][0]:
                    other_indexes.popleft()
            # delete the chosen key-value pair
            del indexes[chosen]
        return ans
    

# This solution works and its very smart ...

from collections import deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indexes={}
        # overwrite the index with the last index
        for i, c in enumerate(s):
            indexes[c] = i
        
        ans = []
        for i, c in enumerate(s):
            if c in ans:
                continue
            # if there is guarantee that there will be the same character with larger index later on
            # then can pop
            while ans and c < ans[-1] and i < indexes[ans[-1]]:
                ans.pop()
            # append no matter what
            ans.append(c)
        return ''.join(ans)