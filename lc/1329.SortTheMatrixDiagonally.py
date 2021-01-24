# 1329. Sort the Matrix Diagonally
# Medium

# 766

# 146

# Add to List

# Share
# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

# Example 1:


# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100

# This solution works

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for s_row in range(len(mat)):
            for s_col in range(len(mat[s_row])):
                if s_col == 0 or s_row == 0:
                    arr = []
                    col = s_col
                    row = s_row
                    while 0 <= col < len(mat[0]) and 0 <= row < len(mat):
                        arr.append(mat[row][col])
                        col += 1
                        row += 1
     
                    col = s_col   
                    row = s_row
                    i = 0
                    arr.sort()
                    while 0 <= col < len(mat[0]) and 0 <= row < len(mat):
                        mat[row][col] = arr[i]
                        col += 1
                        row += 1
                        i += 1
        return mat