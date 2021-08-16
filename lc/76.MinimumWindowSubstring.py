# 76. Minimum Window Substring
# Hard

# 7683

# 483

# Add to List

# Share
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?


# This solution works:


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest_length = float('inf')
        shortest_left = 0
        shortest_right = 0
        ideal = Counter(t)
        
        left = 0
        cur = Counter()
        for right in range(len(s)):
            if s[right] in ideal:
                cur[s[right]] += 1

            while True:
                works = True
                for elem in ideal:
                    if cur[elem] < ideal[elem]:
                        works = False
                        break
                if not works:
                    break
                else:
                    if shortest_length > right-left+1:
                        shortest_length = right-left+1
                        shortest_left, shortest_right = left, right
                    cur[s[left]] -= 1
                    left += 1
        if shortest_length == float('inf'):
            return ''
        return s[shortest_left:shortest_right+1]
        