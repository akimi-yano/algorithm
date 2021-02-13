# 1091. Shortest Path in Binary Matrix
# Medium

# 821

# 63

# Add to List

# Share
# In an N by N square grid, each cell is either empty (0) or blocked (1).

# A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

# Example 1:

# Input: [[0,1],[1,0]]


# Output: 2

# Example 2:

# Input: [[0,0,0],[1,1,0],[1,1,0]]


# Output: 4

 

# Note:

# 1 <= grid.length == grid[0].length <= 100
# grid[r][c] is 0 or 1


# This solution works - need to do all 8 directions :):

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1:
            return -1
        ROW = len(grid)
        COL = len(grid[0])
        seen = set([])
        queue = deque([(0,0,1)])
        while queue:
            row, col, step = queue.popleft()
            if row == ROW-1 and col == COL-1:
                return step
            if (row, col) in seen:
                continue
            seen.add((row, col))
            for rd, cd in ((1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)):
                newrow = row+rd
                newcol = col+cd
                if (0 <= newrow < ROW) and (0 <= newcol < COL) and (grid[newrow][newcol] == 0):
                    queue.append((newrow, newcol, step+1))
        return -1


# This solution works - optimization:

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] == 1:
            return -1
        N = len(grid)
        queue = deque([(0,0,1)])
        while queue:
            row, col, step = queue.popleft()
            if row == N-1 and col == N-1:
                return step
            if grid[row][col] == 1:
                continue
            grid[row][col] = 1
            for rd, cd in ((1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)):
                newrow = row+rd
                newcol = col+cd
                if (0 <= newrow < N) and (0 <= newcol < N) and (grid[newrow][newcol] == 0):
                    queue.append((newrow, newcol, step+1))
        return -1