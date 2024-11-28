'''
2290. Minimum Obstacle Removal to Reach Corner
Attempted
Hard
Topics
Companies
Hint
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

 

Example 1:


Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.
Example 2:


Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
2 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
'''

import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        min_obstacles = [[float('inf')] * COL for _ in range(ROW)]
        min_obstacles[0][0] = grid[0][0]
        minheap = [(min_obstacles[0][0], 0, 0)]

        while minheap:
            obstacle, row, col = heapq.heappop(minheap)
            if row == ROW-1 and col == COL-1:
                return obstacle

            for r_delta, c_delta in ((1,0), (-1,0), (0,1), (0,-1)):
                next_r, next_c = row+r_delta, col+c_delta
                if (0<=next_r<ROW) and (0<=next_c<COL):
                    next_obstacle = obstacle + grid[next_r][next_c]
                    if next_obstacle < min_obstacles[next_r][next_c]:
                        min_obstacles[next_r][next_c] = next_obstacle
                        heapq.heappush(minheap, (next_obstacle, next_r, next_c ))
                        