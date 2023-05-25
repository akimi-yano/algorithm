'''
387. First Unique Character in a String
Easy
7.8K
255
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for i, char in enumerate(s):
            if char not in counts:
                counts[char] = []
            counts[char].append(i)
        
        smallest_idx = float('inf')
        for char in counts:
            if len(counts[char]) < 2:
                smallest_idx = min(smallest_idx, counts[char][0])
            
        return -1 if smallest_idx == float('inf') else smallest_idx


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        n = len(s)
        for idx in range(n):
            if counts[s[idx]] == 1:
                return idx
        return -1