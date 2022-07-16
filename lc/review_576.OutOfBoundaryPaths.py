# 576. Out of Boundary Paths
# Medium

# 1589

# 185

# Add to List

# Share
# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:


# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# Example 2:


# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
 

# Constraints:

# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n


# This solution works:


class Solution:
    MOD = 10 ** 9 + 7
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        '''
        I dont need to create grid because I don't use it in the code below !! As we can visit the same spot multiple times
        '''
        @lru_cache(None)
        def helper(row, col, remaining):
            if not (0<=row<m) or not (0<=col<n):
                return 1
            if remaining == 0:
                return 0
            return helper(row+1, col, remaining-1)+helper(row-1, col, remaining-1)+helper(row, col+1, remaining-1)+helper(row, col-1, remaining-1) % Solution.MOD
        return helper(startRow, startColumn, maxMove) % Solution.MOD