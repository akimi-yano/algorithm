# 1631. Path With Minimum Effort
# Medium

# 88

# 4

# Add to List

# Share
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


# Example 1:



# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
# Example 2:



# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:


# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

# Constraints:

# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106





# This approach does not work :

# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
#         def helper(row, col, max_diff):
#             if row == len(heights)-1 and col == len(heights[0])-1:
#                 return heights[row][col]
#             if not 0<=row<=len(heights)-1 or not 0<=col<=len(heights[0])-1 or heights[row][col] == 0:
#                 return float('-inf')
#             val = heights[row][col]
#             heights[row][col] = 0
#             min_diff = float('inf')
            
#             min_diff = min(min_diff, max(max_diff,  abs(val - helper(row+1, col, max_diff))))
#             min_diff = min(min_diff, max(max_diff,  abs(val - helper(row-1, col, max_diff))))
#             min_diff = min(min_diff, max(max_diff,  abs(val - helper(row, col+1, max_diff))))
#             min_diff = min(min_diff, max(max_diff,  abs(val - helper(row, col-1, max_diff))))
            
#             return min_diff
        
#         return helper(0,0, float('-inf'))




# This approach does not work :

# from collections import deque
# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         queue = deque([(0,0,0)])
#         min_diff = float('inf')
#         while queue:
#             row, col, cur_max = queue.popleft()
#             val = heights[row][col]
#             heights[row][col] = 0
#             if row == len(heights)-1 and col == len(heights[0])-1:
#                 min_diff = min(min_diff, cur_max)
#             for new_row, new_col in ((row+1, col),(row-1, col),(row, col+1),(row, col-1)):
#                 if 0<=new_row<=len(heights)-1 and 0<=new_col<=len(heights[0])-1 and heights[new_row][new_col] != 0:
#                     queue.append((new_row, new_col, max(cur_max, abs(val - heights[new_row][new_col]))))
        
#         return min_diff
    
    

# This approach does not work :

# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
#         def helper(row, col):
#             if row == len(heights)-1 and col == len(heights[0])-1:
#                 return heights[row][col], 0
#             if not 0<=row<=len(heights)-1 or not 0<=col<=len(heights[0])-1 or heights[row][col] == 0:
#                 return float('-inf'), float('-inf')
#             val = heights[row][col]
#             heights[row][col] = 0
#             min_diff = float('inf')
            
#             opt1 = helper(row+1, col)
#             prev_val,cur_max = opt1
#             min_diff = min(min_diff, max(cur_max, abs(prev_val-val))) 
#             opt2 = helper(row-1, col)
#             prev_val,cur_max = opt2
#             min_diff = min(min_diff, max(cur_max, abs(prev_val-val))) 
#             opt3 = helper(row, col+1)
#             prev_val,cur_max = opt3
#             min_diff = min(min_diff, max(cur_max, abs(prev_val-val))) 
#             opt4 = helper(row, col-1)
#             prev_val,cur_max = opt4
#             min_diff = min(min_diff, max(cur_max, abs(prev_val-val))) 
            
#             return val,min_diff
        
#         return helper(0,0)[1]



# This solution works !

'''
djikistra !

why ?:

# of unique path in grid is exponential regardress of how many directions we have to go
4 directions are hard to memorize
2 directions can be memorized
cost differs than just # of steps to take, so DFS will TLE so we should do dijkistra using min heap 
'''
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minheap = [(0,(0,0))]
        
        while minheap:
            diff, (row, col) = heapq.heappop(minheap)
            if heights[row][col] == 0:
                continue
            val = heights[row][col]
            heights[row][col] = 0
            if row == len(heights)-1 and col == len(heights[0])-1:
                return diff

            for new_row, new_col in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if 0 <= new_row <= len(heights)-1 and 0<= new_col <= len(heights[0])-1:
                    heapq.heappush(minheap, (max(diff, abs(val - heights[new_row][new_col])), (new_row, new_col)))