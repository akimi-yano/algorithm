# 3. Longest Substring Without Repeating Characters
# Medium

# 12509

# 662

# Add to List

# Share
# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


# This solution works !

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''unique character then its ok sliding window'''
        unique = set([])
        look = None
        left = 0
        best_length = 0
        for right in range(len(s)):
            if s[right] not in unique:
                unique.add(s[right])
            else:
                look = s[right]
                while left < right and s[left] != look:
                    unique.remove(s[left])
                    left += 1
                left += 1
            best_length = max(best_length, right - left + 1)
        return best_length
    
# This solution works !

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''unique character then its ok sliding window'''
        unique = set([])
        left = 0
        best_length = 0
        for c in s:
            while c in unique:
                unique.remove(s[left])
                left += 1
            unique.add(c)
            best_length = max(best_length, len(unique))
        return best_length