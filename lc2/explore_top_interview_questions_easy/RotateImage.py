'''
48. Rotate Image
Medium
14.7K
658
Companies
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        [[1,2,3],
         [4,5,6],
         [7,8,9]]
        
        then change the row and col
        
        [[1,4,7],
         [2,5,8],
         [3,6,9]]
         
        then swap the cols
        
        [[7,4,1],
         [8,5,2],
         [9,6,3]]
        '''
        ROW = len(matrix)
        COL = len(matrix[0])
        temp_matrix = []
        for row in range(ROW):
            temp_row = []
            for col in range(COL):
                temp_row.append(matrix[col][row])
            temp_matrix.append(temp_row)
                       
        for row in range(ROW):
            for col in range(COL//2):
                temp_matrix[row][col], temp_matrix[row][COL-1-col] = temp_matrix[row][COL-1-col], temp_matrix[row][col]
                
        for row in range(ROW):
            for col in range(COL):
                matrix[row][col] = temp_matrix[row][col]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        [[1,2,3],
         [4,5,6],
         [7,8,9]]
        
        then change the row and col
        
        [[1,4,7],
         [2,5,8],
         [3,6,9]]
         
        then swap the cols
        
        [[7,4,1],
         [8,5,2],
         [9,6,3]]
        '''
        ROW = len(matrix)
        COL = len(matrix[0])
        for row in range(ROW):
            for col in range(row, COL):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(ROW):
            for col in range(COL//2):
                matrix[row][col], matrix[row][COL-1-col] = matrix[row][COL-1-col], matrix[row][col]