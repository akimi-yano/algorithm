# 1621. Number of Sets of K Non-Overlapping Line Segments
# Medium

# 35

# 10

# Add to List

# Share
# Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

# Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

 

# Example 1:


# Input: n = 4, k = 2
# Output: 5
# Explanation: 
# The two line segments are shown in red and blue.
# The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
# Example 2:

# Input: n = 3, k = 1
# Output: 3
# Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
# Example 3:

# Input: n = 30, k = 7
# Output: 796297179
# Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.
# Example 4:

# Input: n = 5, k = 3
# Output: 7
# Example 5:

# Input: n = 3, k = 2
# Output: 1
 

# Constraints:

# 2 <= n <= 1000
# 1 <= k <= n-1



# This approach does not work 


# from itertools import combinations
# class Solution:
#     MOD = 10 ** 9 + 7
#     def numberOfSets(self, n: int, k: int) -> int:
#         options = []
#         for start in range(n):
#             for end in range(start+1,n):
#                 options.append((start, end))
        
#         res = list(combinations(options, k))
        
#         ans = 0
#         prev_s = prev_e = float('-inf')
#         print(res)
#         for pair in res:
#             valid = True
#             for s, e in pair:
#                 if prev_e>s or prev_s>s or prev_e>e or prev_s>e:
#                     valid = False
#                     break
#             if valid:
#                 ans += 1

        
#         return ans % Solution.MOD




# This solution works !!!!!

class Solution:
    MOD = 10 ** 9 + 7
    def numberOfSets(self, n: int, k: int) -> int:
        self.n = n
        self.memo = {}
        return self.helper(0, k, False) % Solution.MOD
    
    def helper(self, idx, remaining, is_drawing):
        key = (idx, remaining, is_drawing)
        if key in self.memo:
            return self.memo[key]
        
        ans = 0
        # you have zero options: you can't draw or not draw after passing n
        if idx >= self.n:
            pass
        # you only have one option: no drawing
        elif remaining == 0:
            ans = 1
        # if you are drawing an interval
        elif is_drawing:
            # you have two options: either keep drawing, or stop drawing
            ans = self.helper(idx+1, remaining, True) + self.helper(idx, remaining-1, False)
        # if you are not drawing an interval
        else:
            # you have two options: don't do anything (don't start drawing), or start drawing
            ans = self.helper(idx+1, remaining, False) + self.helper(idx+1, remaining, True)
        self.memo[key] = ans
        return ans
    
    
# This solution works and very fast:
'''
Intuition
Case 1: Given n points, take k segments, allowed to share endpoints.
Same as:
Case 2: Given n + k - 1 points, take k segments, not allowed to share endpoints.


Prove
In case 2, for each solution,
remove one point after the segments,
then we got one valid solution for case 1.

Reversly also right.


Explanation
Easy combination number C(n + k - 1, 2k).


***
n+k-1 : # of intervals that can overlap
k intervals * 2 (start and end)
'''

import math
class Solution:
    MOD = 10 ** 9 + 7
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n+k-1,k*2) % Solution.MOD