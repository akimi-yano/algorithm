# 498. Diagonal Traverse
# Medium

# 1046

# 381

# Add to List

# Share
# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

# Example:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# Output:  [1,2,4,7,5,3,6,8,9]

# Explanation:

 

# Note:

# The total number of elements of the given matrix will not exceed 10,000.


# This solution works !


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        row, col = 0, 0
        ascending = True
        ans = []
        
        while not (row == len(matrix)-1 and col == len(matrix[0])-1):
            if ascending:
                if 0 <= row <= len(matrix)-1 and 0 <= col <= len(matrix[0])-1:
                    ans.append(matrix[row][col])
                    row -= 1
                    col += 1
                else:
                    ascending = False
                    row += 1
                    if col > len(matrix[0])-1:
                        col -= 1
                        row += 1
            
            elif not ascending:
                if 0 <= row <= len(matrix)-1 and 0 <= col <= len(matrix[0])-1:
                    ans.append(matrix[row][col])
                    row += 1
                    col -= 1
                else:
                    ascending = True
                    col += 1
                    if row > len(matrix)-1:
                        col += 1
                        row -= 1

        ans.append(matrix[row][col])            
        return ans

