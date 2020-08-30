# 1568. Minimum Number of Days to Disconnect Island

# Given a 2D grid consisting of 1s (land) and 0s (water).  An island is a maximal 4-directionally (horizontal or vertical) connected group of 1s.

# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

# In one day, we are allowed to change any single land cell (1) into a water cell (0).

# Return the minimum number of days to disconnect the grid.



# Example 1:



# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 2
# Explanation: We need at least 2 days to get a disconnected grid.
# Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
# Example 2:

# Input: grid = [[1,1]]
# Output: 2
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
# Example 3:

# Input: grid = [[1,0,1,0]]
# Output: 0
# Example 4:

# Input: grid = [[1,1,0,1,1],
#                [1,1,1,1,1],
#                [1,1,0,1,1],
#                [1,1,0,1,1]]
# Output: 1
# Example 5:

# Input: grid = [[1,1,0,1,1],
#                [1,1,1,1,1],
#                [1,1,0,1,1],
#                [1,1,1,1,1]]
# Output: 2


# Constraints:

# 1 <= grid.length, grid[i].length <= 30
# grid[i][j] is 0 or 1.


# This approach does not work !:
# class Solution:
#     def minDays(self, grid: List[List[int]]) -> int:
#         def count_island(grid):
#             pass
        
#         m = len(grid)
#         n = len(grid[0])
#         if count_island !=1:
#             return 0
#         days = 0
#         for row in range(m):
#             for col in range(n):
#                 grid[row][col] = 0
#                 count_island



# This approach works !

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        '''
        1 traverse the entire grid to count 1's 
        2 pick any of the 1's, do DFS; if count for DFS < total -> return 0
        3 pick each of the 1's, do DFS after flipping to 0; if count for DFS < total -1: return 1
        4 else return 2
        '''
        def helper(row, col, visited):
            if not 0 <= row <= self.m-1 or not 0 <= col <= self.n-1 or grid[row][col] == 0 or (row, col) in visited:
                return 0
            visited.add((row, col))
            
            one = helper(row+1,col, visited) 
            two = helper(row-1,col, visited) 
            three = helper(row,col+1, visited) 
            four = helper(row,col-1, visited)
            
            return 1 + one + two + three + four
        
        self.m = len(grid)
        self.n = len(grid[0])
        total = 0
        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == 1:
                    total += 1
        # if there's exactly 1 island
        if total == 1:
            return 1
        
        found = False
        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == 1:
                    if helper(row,col, set([])) < total:
                        return 0    
                    found = True
                if found:
                    break
            if found:
                break
        
        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == 1:
                    count = helper(row+1,col, set([(row, col)]))
                    if count < 1:
                        count = helper(row-1,col, set([(row, col)]))
                        if count < 1:
                            count = helper(row,col+1, set([(row, col)]))
                            if count < 1:
                                count = helper(row,col-1, set([(row, col)]))
                    if count < total - 1:
                        return 1
        return 2
            