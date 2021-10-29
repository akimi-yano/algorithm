# 994. Rotting Oranges
# Medium

# 4801

# 239

# Add to List

# Share
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


# This solution works:


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # store and start with the fresh ones adjacent to the rotten ones
        queue = deque([])
        ROW = len(grid)
        COL = len(grid[0])
        left = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    left += 1
                    for r, c in ((1,0),(-1,0),(0,1),(0,-1)):
                        next_r = row+r
                        next_c = col+c
                        if not(0<=next_r<ROW) or not(0<=next_c<COL):
                            continue
                        if grid[next_r][next_c] == 2:
                            queue.append((row, col))
                            break
        time = 0
        while queue and left:
            new_queue = deque([])
            while queue:
                row, col = queue.popleft()
            
                if grid[row][col] == 1:
                    left -= 1
                    grid[row][col] = 2
                
                for r, c in ((1,0),(-1,0),(0,1),(0,-1)):
                    next_r = row+r
                    next_c = col+c
                    if not(0<=next_r<ROW) or not(0<=next_c<COL):
                        continue
                    if grid[next_r][next_c] == 1:
                        new_queue.append((next_r, next_c))
            time += 1
            
            queue = new_queue

        if left:
            return -1
        
        return time
            