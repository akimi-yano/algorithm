# 329. Longest Increasing Path in a Matrix
# Hard

# 5323

# 91

# Add to List

# Share
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

# Example 1:


# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1


# This solution works:


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix [0])
        
        @lru_cache(None)
        def helper(row, col):
            nonlocal matrix
            best = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                row2, col2 = row + dr, col + dc
                if 0<=row2<ROW and 0<=col2<COL and matrix[row][col] < matrix[row2][col2]:
                    best = max(best, 1 + helper(row2, col2))
            return best
                        
        longest = 0
        for row in range(ROW):
            for col in range(COL):
                longest = max(longest, helper(row, col))
        helper.cache_clear()
        return longest