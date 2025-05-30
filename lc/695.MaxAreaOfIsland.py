# 695. Max Area of Island
# Medium

# 2795

# 94

# Add to List

# Share
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

# This solution works:

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(row, col):
            nonlocal ROW, COL, count
            if not (0<=row<ROW) or not (0<=col<COL) or grid[row][col] == 0:
                return
            count += 1
            grid[row][col] = 0
            helper(row+1, col)
            helper(row-1, col)
            helper(row, col+1)
            helper(row, col-1)
        
        ROW = len(grid)
        COL = len(grid[0])
        
        best = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    count = 0
                    helper(row, col)
                    best = max(best, count)
        return best
    
    
# This solution works:

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(row, col):
            nonlocal ROW, COL
            if not (0<=row<ROW) or not (0<=col<COL) or grid[row][col] == 0:
                return 0
        
            grid[row][col] = 0
            return 1 + helper(row+1, col) + helper(row-1, col) + helper(row, col+1) + helper(row, col-1)
        
        ROW = len(grid)
        COL = len(grid[0])
        
        best = 0
        for row in range(ROW):
            for col in range(COL):
                best = max(best, helper(row, col))
            
        return best