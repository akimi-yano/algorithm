'''
2577. Minimum Time to Visit a Cell In a Grid
Hard
Topics
Companies
Hint
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.

 

Example 1:



Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
Output: 7
Explanation: One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.
Example 2:



Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: -1
Explanation: There is no path from the top left to the bottom-right cell.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
0 <= grid[i][j] <= 105
grid[0][0] == 0
'''

import heapq
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # If we can not move to the neighboring cells from starting position we can not move anywhere in the matrix hence answer is -1.
        # But if we can move to the neighboring cells from starting position, we can move anywhere in the matrix. 
        # We can wait by playing "ping pong" between previous cell and current cell till a neighboring cell opens up.
        if grid[0][1] > 1 and grid[1][0] > 1: return -1

        minheap = []
        heapq.heappush(minheap, (grid[0][0], 0, 0))
        seen = set([])
        ROW = len(grid)
        COL = len(grid[0])

        while minheap:
            time, row, col = heapq.heappop(minheap)
            if row == ROW-1 and col == COL-1:
                return time
            if (row, col) in seen:
                continue
            seen.add((row, col))

            for row_d, col_d in ((0,1), (0,-1), (1,0), (-1,0)):
                next_r, next_c = row + row_d, col + col_d
                if (0<=next_r<ROW) and (0<=next_c<COL):
                    # 偶数でたどり着くますと奇数でたどり着くマスが決まっている。
                    # If time for a neighbor (target) cell is > 1 + time for current cell. 
                    # We can not directly move to target cell. We will have to "ping pong" between previous cell and current cell. 
                    # When playing ping pong between previous and current cell there can be two cases.
                    # 1) Let's say time for target cell is 4 and current time is 2, difference = 2 (even).
                    # Hence we reach target cell with time: target cell time + 1 when difference between target cell time and curr cell time is even.
                    # 2) Let's say time for target cell is 5 and current time is 2, difference = 3 (odd).
                    # Hence we reach target cell with time: target cell time when difference between target cell time and curr cell time is odd.
                    # * This is because the difference between the cur and next should be always odd to be able to go. so add±1 if even
                    # This "ping pong" is captured in the wait variable in the code
                    wait = 1 if (grid[next_r][next_c] - time) % 2 == 0 else 0
                    heapq.heappush(minheap, (max(time+1, grid[next_r][next_c]+wait), next_r, next_c))