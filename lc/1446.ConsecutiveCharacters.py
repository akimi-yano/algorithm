# 1446. Consecutive Characters
# Easy

# 317

# 8

# Add to List

# Share
# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Return the power of the string.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
# Example 3:

# Input: s = "triplepillooooow"
# Output: 5
# Example 4:

# Input: s = "hooraaaaaaaaaaay"
# Output: 11
# Example 5:

# Input: s = "tourist"
# Output: 1


# Constraints:

# 1 <= s.length <= 500
# s contains only lowercase English letters.

# This solution works !
'''
kept track of thr max_length by using left and right pointers
TIME: O(N)
SPACE: O(1)
'''

class Solution:
    def maxPower(self, s: str) -> int:
        max_length = 0
        right = left = 0
        while left < len(s) and right < len(s):
            if s[left] == s[right]:
                right += 1
                max_length = max(max_length, right - left)
            else:
                left = right
        return max_length
            
