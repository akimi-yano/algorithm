# 1647. Minimum Deletions to Make Character Frequencies Unique
# Medium

# 45

# 3

# Add to List

# Share
# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
# Example 2:

# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
# Example 3:

# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

# Constraints:

# 1 <= s.length <= 105
# s contains only lowercase English letters.


# This approach does not work :

# from collections import Counter
# class Solution:
#     def minDeletions(self, s: str) -> int:
#         counts = Counter(s)
#         self.N = len(s)
#         self.min_remove = float('inf')
        
#         def helper(i,  counts):
#             if i > self.N-1:
#                 return
#             check  = set([])
#             total = 0
#             for v in counts.values():
#                 check.add(v)
#                 total += v
#             if len(check) == len(counts):
#                 self.min_remove = min(self.min_remove, self.N - total)
#                 return 
            

#             if counts[s[i]] > 0:
#                 counts[s[i]] -= 1
#                 helper(i+1, counts)
#                 counts[s[i]] += 1
#             helper(i+1, counts)
        
#         helper(0, counts)
#         return self.min_remove
        
        
# This approach works !

import heapq
from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        max_heap = []
        for v in counts.values():
            heapq.heappush(max_heap, -v)
            
        prev_count = float('inf')
        ans = 0
        while max_heap:
            count = heapq.heappop(max_heap)
            count = -count
            if count == prev_count:
                count -= 1
                ans += 1
                if count > 0:
                    heapq.heappush(max_heap, -count)
            else:
                prev_count = count
        return ans
                
        
        
