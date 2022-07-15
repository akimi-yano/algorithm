# 695. Max Area of Island
# Medium

# 6615

# 155

# Add to List

# Share
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.


# This solution works:


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dont cache - you only go once :)
        def helper(row, col):
            if not(0<=row<ROW) or not(0<=col<COL) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + helper(row, col+1) + helper(row, col-1) + helper(row+1, col) + helper(row-1, col)
            
        if not grid or not grid[0]:
            return 0
        ROW = len(grid)
        COL = len(grid[0])
        best = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    best = max(best, helper(r, c))       
        return best