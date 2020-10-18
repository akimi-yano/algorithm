# 1624. Largest Substring Between Two Equal Characters
# Easy

# 19

# 0

# Add to List

# Share
# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.



# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
# Example 4:

# Input: s = "cabbac"
# Output: 4
# Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".


# Constraints:

# 1 <= s.length <= 300
# s contains only lowercase English letters.



# This solution works !

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        memo = {}
        for i, c in enumerate(s):
            if c not in memo:
                memo[c] = []
            memo[c].append(i)
        max_dist = -1
        for v in memo.values():
            if len(v)>1:
                max_dist = max(max_dist, v[-1]-v[0]-1)
        return max_dist