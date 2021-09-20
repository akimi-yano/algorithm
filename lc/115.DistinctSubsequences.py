# 115. Distinct Subsequences
# Hard

# 2651

# 115

# Add to List

# Share
# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# It is guaranteed the answer fits on a 32-bit signed integer.

 

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
 

# Constraints:

# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.


# This solution works:


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def helper(i1, i2):
            if i2 > len(t)-1:
                return 1
            if i1 > len(s)-1:
                return 0
            ways = 0
            ways += helper(i1+1, i2)
            if s[i1] == t[i2]:
                ways += helper(i1+1, i2+1)
            return ways
        return helper(0, 0)
