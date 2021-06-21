# 1905. Count Sub Islands
# Medium

# 169

# 6

# Add to List

# Share
# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

# Return the number of islands in grid2 that are considered sub-islands.

 

# Example 1:


# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
# Example 2:


# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2 
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

# Constraints:

# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.

# This solution works:

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROW = len(grid2)
        COL = len(grid2[0])
        
        def helper(row, col):
            nonlocal subisland
            if not(0<=row< ROW) or not(0<=col<COL) or grid2[row][col] == 0:
                return
            if grid1[row][col] != 1:
                subisland = False
                return
            grid2[row][col] = 0
            helper(row+1,col)
            helper(row-1,col)
            helper(row, col+1)
            helper(row, col-1)
        
        ans = 0
        subisland = False
        for row in range(ROW):
            for col in range(COL):
                if grid2[row][col] == 1:
                    subisland = True
                    helper(row, col)
                    if subisland:
                        ans += 1
        return ans
