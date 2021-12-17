# 221. Maximal Square
# Medium

# 5958

# 130

# Add to List

# Share
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.


# This solution works:


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        DP = [[0 for _ in range(COL+1)] for _ in range(ROW+1)]
        best_side = 0
        for row in range(ROW):
            for col in range(COL):
                if matrix[row][col] == "1":
                    DP[row+1][col+1] = min(DP[row][col], DP[row+1][col], DP[row][col+1])+1
                best_side = max(best_side, DP[row+1][col+1])
        
        return best_side ** 2