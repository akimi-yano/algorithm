'''
2658. Maximum Number of Fish in a Grid
Medium
Topics
Companies
Hint
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
'''

# BFS

from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        best = 0
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] > 0:
                    queue = deque([])
                    queue.append((row, col))
                    val = grid[row][col]
                    grid[row][col] = 0
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                            next_r, next_c = cur_r + dr, cur_c + dc
                            if 0<=next_r<ROW and 0<=next_c<COL and grid[next_r][next_c] > 0:
                                val += grid[next_r][next_c]
                                grid[next_r][next_c] = 0
                                queue.append((next_r, next_c))
                    
                    best = max(best, val)
        return best

# DFS

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def helper(row, col):
            val = grid[row][col]
            grid[row][col] = 0
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                next_r, next_c = row + dr, col + dc
                if 0 <= next_r < ROW and 0 <= next_c < COL and grid[next_r][next_c] > 0:
                    val += helper(next_r, next_c)
            return val

        best = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] > 0:
                    best = max(best, helper(row, col))
        return best
    
