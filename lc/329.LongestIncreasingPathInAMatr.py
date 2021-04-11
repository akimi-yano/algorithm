# 329. Longest Increasing Path in a Matrix
# Hard

# 3110

# 56

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
        def helper(row, col, prev):
            nonlocal seen
            if not 0<=row<ROW or not 0<=col<COL or prev >= matrix[row][col] or (row,col) in seen:
                return 0
            seen.add((row,col))
            ans = 1+max(helper(row+1,col,matrix[row][col]), helper(row-1,col,matrix[row][col]),helper(row,col+1,matrix[row][col]),helper(row,col-1,matrix[row][col]))
            seen.remove((row,col))
            return ans
                        
        longest = 0
        for row in range(ROW):
            for col in range(COL):
                seen = set([])
                longest = max(longest, helper(row, col,float ('-inf')))    
        return longest