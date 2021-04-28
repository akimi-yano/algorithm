# 63. Unique Paths II
# Medium

# 2754

# 295

# Add to List

# Share
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and space is marked as 1 and 0 respectively in the grid.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
 

# Constraints:

# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.

# This solution works:

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        @lru_cache(None)
        def helper(row, col):
            if row == ROW-1 and col == COL-1:
                return 1
            if not (0<=row<=ROW-1) or not (0<=col<=COL-1) or obstacleGrid[row][col] == 1:
                return 0 
            obstacleGrid[row][col] = 1
            return helper(row+1, col) + helper(row, col+1)
            
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROW-1][COL-1] == 1:
            return 0
        return helper(0, 0)