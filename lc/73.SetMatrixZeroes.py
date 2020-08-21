# 73. Set Matrix Zeroes

# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


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
# -10^9 <= matrix[i][j] <= 10^9
# Accepted


# This solves problem but it can be  improved in terms of  space complexity

# Space: O(MN)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeros.append((row,col))
        
        for r,c in zeros:
            for cl in range(n):
                matrix[r][cl] = 0
            for rw in range(m):
                matrix[rw][c] =0
                

# Space: O(M+N)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = set([])
        zero_cols = set([])
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        for r in range(m):
            for cl in zero_cols:
                matrix[r][cl] = 0
        for c in range(n):
            for rw in zero_rows:
                matrix[rw][c] =0

                
# Another soluiton that works !!!!! - O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        m = len(matrix)
        n = len(matrix[0])
        
        for row in range(m):
            found_zero = False
            for col in range(n):
                if matrix[row][col] == 0:
                    found_zero = True
                    break
            if found_zero:
                for col in range(n):
                    if matrix[row][col] != 0:
                        matrix[row][col] = float('inf')

        for col in range(n):
            found_zero = False
            for row in range(m):
                if matrix[row][col] == 0:
                    found_zero = True
                    break
            if found_zero:
                for row in range(m):
                    if matrix[row][col] != 0:
                        matrix[row][col] = float('inf')

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == float('inf'):
                    matrix[row][col] = 0
        


# Yay this solution works and intuitive ! 
# basic idea: any spot in first row or first col is 0 then the row / col are all 0 + for any 
# spot that has 0, its row[0] and [0]col is also 0 ->  update all at the end  

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        m = len(matrix)
        n = len(matrix[0])
        
        zero_first_col = False
        for row in range(m):
            if matrix[row][0] == 0:
                zero_first_col = True
                break

        zero_first_row = False
        for col in range(n):
            if matrix[0][col] == 0:
                zero_first_row = True
                break
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if zero_first_col:
            for row in range(m):
                matrix[row][0] = 0
        if zero_first_row:
            for col in range(n):
                matrix[0][col] = 0