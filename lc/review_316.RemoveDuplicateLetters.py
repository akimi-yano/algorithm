# 316. Remove Duplicate Letters
# Medium

# 3968

# 280

# Add to List

# Share
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
 

# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/



# This solution works:



class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idxes = {}
        for i, elem in enumerate(s):
            last_idxes[elem] = i
        
        ans = []
        for i, elem in enumerate(s):
            if elem in ans:
                continue
            while ans and ans[-1] > elem and last_idxes[ans[-1]] > i:
                ans.pop()
            ans.append(elem)
        return "".join(ans)