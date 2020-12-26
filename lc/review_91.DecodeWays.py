# 91. Decode Ways
# Medium

# 3666

# 3308

# Add to List

# Share
# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.

 

# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:

# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
# Example 4:

# Input: s = "1"
# Output: 1
 

# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

# This solution works !

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def helper(start):
            if start == len(s):
                return 1
            if start > len(s):
                return 0
            if s[start] == '0':
                return 0
            ways = 0
            if 1 <= int(s[start:start+1]) <=26:
                ways += helper(start+1)
            if 1 <= int(s[start:start+2]) <=26:
                ways += helper(start+2)
            return ways
    
        return helper(0)