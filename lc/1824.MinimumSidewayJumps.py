# 1824. Minimum Sideway Jumps
# Medium

# 235

# 13

# Add to List

# Share
# There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.

# You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.

# For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
# The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

# For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
# Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

# Note: There will be no obstacles on points 0 and n.

 

# Example 1:


# Input: obstacles = [0,1,2,3,0]
# Output: 2 
# Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
# Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).
# Example 2:


# Input: obstacles = [0,1,1,3,3,0]
# Output: 0
# Explanation: There are no obstacles on lane 2. No side jumps are required.
# Example 3:


# Input: obstacles = [0,2,1,0,3,0]
# Output: 2
# Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.
 

# Constraints:

# obstacles.length == n + 1
# 1 <= n <= 5 * 105
# 0 <= obstacles[i] <= 3
# obstacles[0] == obstacles[n] == 0


# This approach does not work - max depth of recursion:


# class Solution:
#     def minSideJumps(self, obstacles: List[int]) -> int:
#         @lru_cache(None)
#         def helper(cur, i):
            
#             if i >= len(obstacles)-1:
#                 return 0
#             if obstacles[i] == cur:
#                 return float('inf')
            
#             min_op = float('inf')
#             for choice in (1,2,3):
#                 if choice == obstacles[i]:
#                     continue
#                 if cur == choice and obstacles[i+1] != cur:
#                     min_op = min(min_op, helper(cur, i+1))
#                 elif obstacles[i+1] != choice:
#                     min_op = min(min_op, 1 + helper(choice, i+1))
#             return min_op
            
#         ans = helper(2, 0)
#         helper.cache_clear()
#         return ans
#         '''
#         [0,1,2,3,0]
#         cur = 2
#           o
#         ---------
#         x  o
#         ---------
#              o
             
#         choice 2 helper(2, 1) 0 -> choice 123
#         choice 1 helper(1,1) floatint
#         choice 3 helper(3,1) 1
#         '''

# This approach does not work:

# class Solution:
#     def minSideJumps(self, obstacles: List[int]) -> int:
        
#         @lru_cache(None)
#         def helper(cur, i):
#             while i < len(obstacles) and obstacles[i] != cur:
#                 i += 1
#             #important
#             i -= 1
#             if i == len(obstacles)-1:
#                 return 0
            
#             min_op = float('inf')
#             for choice in (1,2,3):
#                 if obstacles[i] != choice and obstacles[i+1] != choice:
#                     min_op = min(min_op, 1 + helper(choice, i+1))
#             return min_op
            
#         return helper(2, 0)

#         '''
#         [0,1,2,3,0]
#         cur = 2
#           o
#         ---------
#         x  o
#         ---------
#              o
             
#         choice 2 helper(2, 1) 0 -> choice 123
#         choice 1 helper(1,1) floatint
#         choice 3 helper(3,1) 1
#         '''

# This approach does not work:

# class Solution:
#     def minSideJumps(self, obstacles: List[int]) -> int:
#         queue = deque([(2, 0)])
#         seen = set([(2, 0)])
#         ans = 0
#         while queue:
#             for _ in range(len(queue)):
#                 lane, point = queue.popleft()
#                 while point < len(obstacles) and obstacles[point] != lane:
#                     point += 1
#                 #important
#                 point -= 1
#                 if point == len(obstacles)-1:
#                     return ans

#                 for next_lane in (1,2,3):
#                     if obstacles[point] != next_lane and obstacles[point+1] != next_lane and (point, next_lane) not in seen:
#                         queue.append((next_lane, point))
#                         seen.add((next_lane, point))
#             ans += 1

# This solution works:

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]
        for obstacle_lane in obstacles:
            # if we meet stone we set this one to be positive infinity
            if obstacle_lane:
                dp[obstacle_lane - 1] = float('inf')
            for next_lane in range(3):
                # avoid the same one
                if obstacle_lane != next_lane + 1:
                    # get the minimum
                    dp[next_lane] = min(dp[next_lane], dp[(next_lane + 1) % 3] + 1, dp[(next_lane + 2) % 3] + 1)
        return min(dp)
    
        '''
        Explanation
        dp[0] = minimum jump to reach lane 1
        dp[1] = minimum jump to reach lane 2
        dp[2] = minimum jump to reach lane 3
        If meet a stone, set its dp[i] to infinity.
        result equals to min(dp)

        Complexity
        Time O(n)
        Space O(1)
        
        '''