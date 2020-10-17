# 74. Search a 2D Matrix
# Medium

# 2367

# 171

# Add to List

# Share
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# Output: false
# Example 3:

# Input: matrix = [], target = 0
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 0 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# This solution works !!!

'''
binary search matrix 
row: divide the mid by COL
col: mod the mid by COL
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        ROW = len(matrix)
        COL = len(matrix[0])
        
        left = 0
        right = ROW*COL -1
        
        while left<=right:
            mid = (left+right)//2
            row = mid // COL
            col = mid % COL
            # print(row, col, mid)
            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                left = mid +1
            
            else:
                right = mid -1
        return False
            