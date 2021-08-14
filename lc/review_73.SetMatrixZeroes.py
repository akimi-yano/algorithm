# 73. Set Matrix Zeroes
# Medium

# 4265

# 402

# Add to List

# Share
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# This solution works:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper_h(row, col):
            if not 0<=row<ROW or not 0<=col<COL or (row, col) in seen:
                return 
            if matrix[row][col] != 0:
                matrix[row][col] = float('inf')
            seen.add((row, col))
            helper_h(row, col+1)
            helper_h(row, col-1)
        
        def helper_v(row, col):
            if not 0<=row<ROW or not 0<=col<COL or (row, col) in seen:
                return 
            if matrix[row][col] != 0:
                matrix[row][col] = float('inf')
            seen.add((row, col))
            helper_v(row+1, col)
            helper_v(row-1, col)
            
        ROW = len(matrix)
        COL = len(matrix[0])
        
        for row in range(ROW):
            for col in range(COL):
                if matrix[row][col] == 0:
                    seen = set([])
                    helper_h(row, col)
                    seen.remove((row,col))
                    helper_v(row, col)
    
        for row in range(ROW):
            for col in range(COL):
                if matrix[row][col] == float('inf'):
                    matrix[row][col] = 0 
        