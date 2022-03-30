# 74. Search a 2D Matrix
# Medium

# 6696

# 255

# Add to List

# Share
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


# This solution works:


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(arr):
            left = 0
            right = len(arr)-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return False        
            
        left = 0
        right = len(matrix)-1
        while left <= right:
            mid = (left+right)//2
            row = matrix[mid]
            if row[0] <= target<= row[len(row)-1]:
                return helper(row)
            elif target < row[len(row)-1]:
                right = mid-1
            else:
                left = mid+1
        return False