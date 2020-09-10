# 221. Maximal Square
# Medium

# 3392

# 88

# Add to List

# Share
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4


# THIS APPROACH WORKS AND IS GREAT: 

# Understanding basics
# image

# Here I want to mention that we are drawing squares from top left corner to bottom right corner. Therefore, when I mention, "surrounding elements", I am saying cells above the corner cell and the cells on the left of the corner cell.
# Building DP grid to memoize

# We are going to create a dp grid with initial values of 0.
# We are going to update dp as described in the following figure.
# image

# Bigger Example

# Let's try to see a bigger example.
# We go over one cell at a time row by row in the matrix and then update our dp grid accordingly.
# Update max_side with the maximum dp cell value as you update.
# image

# In the code, I create a dp grid which has one additional column and one additional row. The reason is to facilitate the index dp[r-1][c] dp[r][c-1] and dp[r-1][c-1] for cells in first row and first column in matrix.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side
                
# Complexity Analysis

# Time complexity : O(mn). Single pass - row x col (m=row; n=col)
# Space complexity : O(mn). Additional space for dp grid (don't need to worry about additional 1 row and col).

# Follow up
# Space can be optimized as we don't need to keep the whole dp grid as we progress down the rows in matrix.




# With recursion + memorization
from functools import lru_cache 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.best, self.matrix = 0, matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.rdfs((i,j))
        return self.best * self.best
    
    @lru_cache(None)    
    def rdfs(self, pos):
        best = 0
        if self.matrix[pos[0]][pos[1]] == '1':
            if self.next_pos_are_good(pos):
                best = min(self.rdfs((pos[0], pos[1] - 1)), self.rdfs((pos[0] - 1, pos[1])), 
                           self.rdfs((pos[0] - 1, pos[1] - 1))) + 1
            else: best = 1
        self.best = max(best, self.best)
        return best
    
    def next_pos_are_good(self, pos):
        return not (pos[1] - 1 < 0 or pos[0] - 1 < 0)