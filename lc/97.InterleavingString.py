# 97. Interleaving String
# Medium

# 2452

# 126

# Add to List

# Share
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

 

# Example 1:


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true
 

# Constraints:

# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
 

# Follow up: Could you solve it using only O(s2.length) additional memory space?

# This solution works:

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def helper(idx1, idx2, idx3):
            if idx3 > len(s3)-1 and idx1 > len(s1)-1 and idx2 > len(s2)-1:
                return True
            if idx1 < len(s1) and idx3 < len(s3) and s1[idx1] == s3[idx3]:
                if helper(idx1+1, idx2, idx3+1):
                    return True
            if idx2 < len(s2) and idx3 < len(s3) and s2[idx2] == s3[idx3]:
                if helper(idx1, idx2+1, idx3+1):
                    return True
            return False
        return helper(0, 0, 0)
        