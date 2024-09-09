'''
200. Number of Islands
Solved
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # if I see the '1', change it to '0'
        def helper(row, col):
            if not (0<=row<ROW) or not (0<=col<COL):
                return
            if grid[row][col] == '1':
                grid[row][col] = '0'
                helper(row+1, col)
                helper(row-1, col)
                helper(row, col+1)
                helper(row, col-1)

        ROW = len(grid)
        COL = len(grid[0])
        ans = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == '1':
                    helper(row, col)
                    ans += 1
        return ans
        
# Time: O(m*n)
# Space: O(1)