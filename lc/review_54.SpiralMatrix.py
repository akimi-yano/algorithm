# 54. Spiral Matrix
# Medium

# 5021

# 721

# Add to List

# Share
# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


# This solution works:


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        ROW = len(matrix)
        COL = len(matrix[0])
        mincol = 0
        minrow = 0
        maxcol = COL-1
        maxrow = ROW-1
        while len(ans) < ROW * COL:
            for col in range(mincol, maxcol+1):
                ans.append(matrix[minrow][col])
            minrow += 1   
            if len(ans) >= ROW * COL:
                break
                
            for row in range(minrow, maxrow+1):
                ans.append(matrix[row][maxcol])
            maxcol -= 1
            if len(ans) >= ROW * COL:
                break
            
            for col in range(maxcol, mincol-1, -1):
                ans.append(matrix[maxrow][col])
            maxrow -= 1
            if len(ans) >= ROW * COL:
                break
                
            for row in range(maxrow, minrow-1, -1):
                ans.append(matrix[row][mincol])
            mincol += 1
            if len(ans) >= ROW * COL:
                break

        return ans