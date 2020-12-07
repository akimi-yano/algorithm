# 59. Spiral Matrix II
# Medium

# 1379

# 124

# Add to List

# Share
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20

# This solution works !

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        max_row = max_col  = n
        min_row = min_col = 0
        number = 1
        while number <= n*n:
            
            for col in range(min_col, max_col):
                if grid[min_row][col] != 0:
                    break
                grid[min_row][col] = number
                number += 1
            
            min_row += 1
            for row in range(min_row, max_row):
                if grid[row][max_col-1] != 0:
                    break
                grid[row][max_col-1] = number
                number += 1
            
            max_col -= 1
            for col in range(max_col-1, min_col-1, -1):
                if grid[max_row-1][col] != 0:
                    break
                grid[max_row-1][col] = number
                number += 1
            
            max_row -= 1
            for row in range(max_row-1, min_row-1, -1):
                if grid[row][min_col] != 0:
                    break
                grid[row][min_col] = number
                number += 1
            min_col += 1
        
        return grid