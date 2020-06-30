# 64. Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right which minimizes the sum of 
# all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
 
# m-1   n-1
# row col - starting 

# global_min

# base case :
# row == 0 and col == 0 - > found a valid path -> use the count and 
# update global min if smaller than global min
# out of bound -> row < 0 or col < 0

# recursive case :
# down row - 1, col
# right row, col -1

class Solution:
  def min_path_sum(self, grid):
    if len(grid) == 0 or len(grid[0]) ==0:
      return 0
    m = len(grid)
    n = len(grid[0])
    memo = {}
    def helper(row, col):
      if (row,col) in memo:
        return memo[(row,col)]
      # out of bound
      if row<0 or col<0:
        return float('inf')

      # found a valid path
      if row == 0 and col == 0:
        return grid[row][col]
        
      memo[(row,col)] = grid[row][col] + min(helper(row-1,col),helper(row,col-1))
      return memo[(row,col)]

    return helper(m-1,n-1)
    
s = Solution()
print(s.min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))


class Solution:
  def min_path_tab(self, grid):
    tab = [[0 for col in range(len(grid[row]))] for row in range(len(grid))]
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if i == 0 and j == 0:
          tab[i][j] = grid[i][j]
        else:
          if i and j:
            tab[i][j] = min(tab[i-1][j], tab[i][j-1]) + grid[i][j]
          else:
            if i:
              tab[i][j] = tab[i-1][j] + grid[i][j]
            if j:
              tab[i][j] = tab[i][j-1] + grid[i][j]
    # print(tab)
    return tab[-1][-1]

c = Solution()
print(c.min_path_tab([[1,3,1],[1,5,1],[4,2,1]]))

