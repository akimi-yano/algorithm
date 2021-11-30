# 85. Maximal Rectangle
# Hard

# 5480

# 97

# Add to List

# Share
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = []
# Output: 0
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
# Example 4:

# Input: matrix = [["1"]]
# Output: 1
# Example 5:

# Input: matrix = [["0","0"]]
# Output: 0
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 0 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.


# This solution works:


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        ROW = len(matrix)
        COL = len(matrix[0])
        
        widths = []
        for row in matrix:
            arr = []
            count = 0
            for elem in row:
                if elem == "1":
                    count += 1
                else:
                    count = 0
                arr.append(count)
            widths.append(arr)
        print(widths)
        
        ans = 0
        for start_row in range(ROW):
            for col in range(COL):
                width = float('inf')
                for end_row in range(start_row, ROW):
                    width = min(width, widths[end_row][col])
                    if width == 0:
                        break
                    ans = max(ans, (end_row-start_row+1)*width)
        return ans