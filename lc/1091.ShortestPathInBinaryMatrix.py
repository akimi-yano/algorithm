# 1091. Shortest Path in Binary Matrix
# Medium

# 422

# 41

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


# my solution that works ! and most intuitive to me

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1:
            return -1
        queue = deque([(0,0,1)])
        while queue:
            row,col,d = queue.popleft() # IMPORTANT!
            if grid[row][col] == 1:
                continue
            if row==len(grid)-1 and col==len(grid[0])-1:
                return d
            grid[row][col]=1
            for r,c in ((0,-1),(0,1),(1,0),(-1,0),(-1,-1),(1,-1),(-1,1),(1,1)):
                if 0<=row+r<=len(grid)-1 and 0<=col+c<=len(grid[0])-1 and grid[row+r][col+c]==0:
                    queue.append((row+r,col+c,d+1))
        return -1




# another solution that works optimization - but less intuitive 
# change 0 -> 1 right before appending it to queue 
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1:
            return -1
        queue = deque([(0,0,1)])
        while queue:
            row,col,d = queue.popleft()
            # if grid[row][col] == 1:
            #     continue
            if row==len(grid)-1 and col==len(grid[0])-1:
                print(grid)
                return d
            # grid[row][col]=1
            for r,c in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                if 0<=row+r<=len(grid)-1 and 0<=col+c<=len(grid[0])-1 and grid[row+r][col+c]==0:
                    grid[row+r][col+c]=1
                    queue.append((row+r,col+c,d+1))
        return -1
    
    
    
    # this solution also works 
    # tricks: the order of loop, changing it to 1 before appending, loping instead of popping (but the length of queue changes ...)
    def shortestPathBinaryMatrix(self,grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
        for i, j, d in q:
            if i == n-1 and j == n-1: return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d+1))
        return -1