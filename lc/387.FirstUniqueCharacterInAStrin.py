# 387. First Unique Character in a String
# Easy

# 6023

# 219

# Add to List

# Share
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


# This solution works:


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_idxes = {}
        for i, c in enumerate(s):
            if c not in char_idxes:
                char_idxes[c] = []
            char_idxes[c].append(i)
        
        smallest_idx = float('inf')
        for c, arr in char_idxes.items():
            if len(arr) == 1:
                smallest_idx = min(smallest_idx, arr[0])
                
        return -1 if smallest_idx == float('inf') else smallest_idx