# Rotting Oranges
# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:



# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.




# This does not work:

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         def helper(row,col):
#             if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1 or grid[row][col]==0:
#                 return float('inf')
#             add_val = 0
#             if grid[row][col]==1:
#                 add_val = 1
#                 grid[row][col]=2
#             min_path = float('inf')
#             min_path = min(min_path, add_val+helper(row+1,col), add_val+helper(row-1,col), add_val+helper(row,col+1), add_val+helper(row,col-1))
#             return min_path
        
#         min_path  = float('inf')
#         for row in range(len(grid)):
#             for col in range(len(grid[row])):
#                 if grid[row][col]==2:
#                     min_path=min(min_path,helper(row,col))
        
#         for row in range(len(grid)):
#             for col in range(len(grid[row])):
#                 if grid[row][col]==1:
#                     return -1
#         return min_path


# this solution works!
# When using queue, we need to check always before updating important variables 
# because the once its pushed to queue, old info might not have been updated in the queue
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        queue = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]==2:
                    for next_r,next_c in ((row+1,col),(row-1,col),(row,col+1),(row,col-1)):
                        if 0<=next_r<=len(grid)-1 and 0<=next_c<=len(grid[0])-1 and grid[next_r][next_c]==1:
                            queue.append((next_r,next_c,0+1))
        # print(queue)
        while queue:
            #IMPORTANT 
            row,col,maybetime = queue.popleft()
            #IMPORTANT
            if grid[row][col]!=1:
                continue
            grid[row][col]=2
            #IMPORTANT
            time = maybetime
            for next_r,next_c in ((row+1,col),(row-1,col),(row,col+1),(row,col-1)):
                if 0<=next_r<=len(grid)-1 and 0<=next_c<=len(grid[0])-1 and grid[next_r][next_c]==1:
                    queue.append((next_r,next_c,time+1))
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]==1:
                    return -1
        return time
