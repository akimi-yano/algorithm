# 395. Longest Substring with At Least K Repeating Characters

# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

# Example 1:

# Input:
# s = "aaabb", k = 3

# Output:
# 3

# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input:
# s = "ababbc", k = 2

# Output:
# 5

# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


# This solution does not work:
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         if k == 0:
#             return len(s)
#         if len(s) == 0:
#             return 0 
    
#         memo = {}
#         for i in range(len(s)):
#             if s[i] not in memo:
#                 memo[s[i]] = ([i],1)
#             else:
#                 idx,count = memo[s[i]] 
#                 idx.append(i)
#                 count+=1
#                 memo[s[i]]=(idx,count)
                
#         # print(memo)
#         keys = list(memo.keys())
#         for key in keys:
#             if memo[key][1]<k:
#                 del memo[key]
#         sm = len(s)
#         lg = 0
#         for val in memo.values():
#             lg = max(lg,max(val[0]))
#             sm = min(sm,min(val[0]))
#         ans = (lg-sm+1)
#         return ans if ans > -1  else 0

# This works - but can be optimized 

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k < 1:
            return len(s)

        best = 0
        for i in range(len(s)):
            cleared = set([])
            chars = {}
            for j in range(i, len(s)):
                c = s[j]
                if c in cleared:
                    pass
                else:
                    if c not in chars:
                        chars[c] = 0
                    chars[c] += 1
                    if chars[c] >= k:
                        cleared.add(c)
                        del chars[c]
                if len(chars) < 1:
                    best = max(best, j - i + 1)
        return best
    
# This solution works - O(N*26)ish as all are lower case letters 
# I can just take the first too rare character instead of a rarest.

def longestSubstring(self, s, k):
    for c in set(s):
        if s.count(c) < k:
            return max(self.longestSubstring(t, k) for t in s.split(c))
    return len(s)

# If every character appears at least k times, the whole string is ok. 
# Otherwise split by a least frequent character 
# (because it will always be too infrequent and thus can't be part of any ok substring) and make the most out of the splits.




# YAY THIS WORKS !!! USED COUNTER DICTIONARY AND ITS INTUITIVE:

from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = Counter(s)
        for letter, count in counts.items():
            if count < k:
                return max([self.longestSubstring(substr, k) for substr in s.split(letter)])
        return len(s)