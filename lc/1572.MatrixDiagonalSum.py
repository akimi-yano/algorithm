# 1572. Matrix Diagonal Sum
# Easy

# 16

# 1

# Add to List

# Share
# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

# Example 1:


# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# Example 2:

# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:

# Input: mat = [[5]]
# Output: 5
 

# Constraints:

# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100


# Solution I had  during the comp ! This solution ACed !!!

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = set([])
        maxrow = len(mat)-1
        maxcol = len(mat[0])-1
        total = 0
        row = 0
        col = 0
        
        while row<maxrow+1 and col<maxcol+1:
            # print(row,col)
            if (row,col) not in visited and 0<=row<=maxrow and 0<=col<=maxcol:
                total += mat[row][col]
                visited.add((row,col))
            
            row += 1
            col += 1
        
        row = 0
        col = maxcol
        
        while row<maxrow+1 and col>-1:
            # print(row,col)
            if (row,col) not in visited and 0<=row<=maxrow and 0<=col<=maxcol:
                total += mat[row][col]
                visited.add((row,col))
            row += 1
            col -= 1
        # print(visited)
        return total
            
            