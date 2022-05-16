# 1091. Shortest Path in Binary Matrix
# Medium

# 2754

# 132

# Add to List

# Share
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1


# This solution works:


from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque([(0,0,1)])
        seen = set([])
        while queue:
            row, col, step = queue.popleft()
            if row == len(grid)-1 and col == len(grid[0])-1:
                return step
            if (row, col) in seen:
                continue
            seen.add((row, col))
            for r, c in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)):
                next_r, next_c = row+r, col+c
                if 0<=next_r<len(grid) and 0<=next_c<len(grid[0]) and grid[next_r][next_c] == 0:
                    queue.append((next_r, next_c, step+1))
        return -1           