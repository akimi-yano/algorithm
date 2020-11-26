# 395. Longest Substring with At Least K Repeating Characters
# Medium

# 1918

# 240

# Add to List

# Share
# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 105

#This approach does not work:

# from collections import Counter
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         longest = 0
        
#         for left in range(len(s)):
#             for right in range(left+1, len(s)):
#                 smallest_freq = min(Counter(s[left:right]).values())
#                 if smallest_freq >= k:
#                     longest = max(longest, right-left)
#         return longest
        
# This approach does not work:

# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
        
#         def helper(left, right):
#             if left >= right or left >= len(s) or right >= len(s):
#                 return float('-inf')
#             if 
#             longest = 0
#             smallest_freq = min(Counter(s[left:right]).values())
#             if smallest_freq >= k:
#                 longest = max(longest, right-left + helper(left, right+1))
#                 longest = max(longest,  helper(right, right+1))
#             return longest
        
#         return helper(0, 0)

# This solution works !

from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < 1:
            return 0
        counts = Counter(s)
        key, value = min(counts.items(), key = lambda tup: tup[1])
        
        if value < k:
            return max([self.longestSubstring(substr, k) for substr in s.split(key)])
        return len(s)
