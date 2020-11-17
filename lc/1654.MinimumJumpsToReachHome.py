# 1654. Minimum Jumps to Reach Home
# Medium

# 66

# 15

# Add to List

# Share
# A certain bug's home is on the x-axis at position x. Help them get there from position 0.

# The bug jumps according to the following rules:

# It can jump exactly a positions forward (to the right).
# It can jump exactly b positions backward (to the left).
# It cannot jump backward twice in a row.
# It cannot jump to any forbidden positions.
# The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

# Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.


# Example 1:

# Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# Output: 3
# Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
# Example 2:

# Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# Output: -1
# Example 3:

# Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# Output: 2
# Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.


# Constraints:

# 1 <= forbidden.length <= 1000
# 1 <= a, b, forbidden[i] <= 2000
# 0 <= x <= 2000
# All the elements in forbidden are distinct.
# Position x is not forbidden.


# This approach does not work : 

# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
#         def helper(i, used):
#             key = (i, used)
#             if key in memo:
#                 return memo[key]
#             min_step = float('inf')
#             if i == x:
#                 min_step =  0
#             elif i < 0 or i in B:
#                 pass
#             else:
#                 min_step = min(min_step, 1 + helper(i+a, False))
#                 if not used:
#                     min_step = min(min_step, 1 + helper(i-b, True))
#                 memo[key] = min_step
#             return min_step
#         memo = {}
#         B = set(forbidden)
#         ans = helper(0, False)
#         return ans if ans != float('inf') else -1


# # This approach does not work 

# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
#         def helper(i, used):
#             key = (i, used)
#             if key in memo:
#                 return memo[key]
#             min_step = float('inf')
#             if i == x:
#                 min_step =  0
#             elif i < 0 or i in B or i > 2000:
#                 pass
#             else:
#                 B.add(i)
#                 min_step = min(min_step, 1 + helper(i+a, False))
#                 if not used:    
#                     min_step = min(min_step, 1 + helper(i-b, True))
                
#             memo[key] = min_step
#             return min_step
#         memo = {}
#         B = set(forbidden)
#         ans = helper(0, False)
#         return ans if ans != float('inf') else -1
            
            
            
# This solution works !

'''
minimum # of jumps -> think of BFS shortest path !!!

think in this order: 1 BFS, 2 DP, 3 Binary Search

due to the constraints blow, next pos needs to be less than 4000 :
# 1 <= a, b, forbidden[i] <= 2000
# 0 <= x <= 2000

'''

from collections import deque
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        queue = deque([(0, False, 0)])
        banned = set(forbidden)
        seen = set([(0, False)])
        
        while queue:
            cur, is_last_backed, count = queue.popleft()
            if cur == x:
                return count
            
            # forward
            next_pos = cur + a
            if next_pos < 4000 and next_pos not in banned and (next_pos, False) not in seen:
                queue.append((next_pos, False, count+1))
                seen.add((next_pos, False))
            
            # backword
            next_pos  = cur - b
            if not is_last_backed and next_pos >= 0 and next_pos not in banned and (next_pos, True) not in seen:
                queue.append((next_pos, True, count+1))
                seen.add((next_pos, True))
                
        return -1
        
        