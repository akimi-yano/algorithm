# 1463. Cherry Pickup II
# Hard

# 515

# 8

# Add to List

# Share
# Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.

# You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

# Return the maximum number of cherries collection using both robots  by following the rules below:

# From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
# When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
# When both robots stay on the same cell, only one of them takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in the grid.
 

# Example 1:



# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.
# Example 2:



# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.
# Example 3:

# Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
# Output: 22
# Example 4:

# Input: grid = [[1,1],[1,1]]
# Output: 4
 

# Constraints:

# rows == grid.length
# cols == grid[i].length
# 2 <= rows, cols <= 70
# 0 <= grid[i][j] <= 100 


# This solution works !

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.ROW = len(grid)
        self.COL = len(grid[0])
        
        @lru_cache(None)
        def helper(r1, c1, r2, c2):
            if not 0<=r1<=self.ROW-1 or not 0<=c1<=self.COL-1 or not 0<=r2<=self.ROW-1 or not 0<=c2<=self.COL-1:
                return float('-inf')
            
            val1 = grid[r1][c1]
            val2 = grid[r2][c2]
            if r1 == r2 and c1 == c2:
                val2 = 0
                
            if r1 == self.ROW-1 and r2 == self.ROW-1:
                return val1 + val2
            max_cherry = 0
            max_cherry += val1 + val2 + max(
                helper(r1+1, c1-1, r2+1, c2-1),
                helper(r1+1, c1-1, r2+1, c2),
                helper(r1+1, c1-1, r2+1, c2+1),
                helper(r1+1, c1,   r2+1, c2-1), 
                helper(r1+1, c1,   r2+1, c2), 
                helper(r1+1, c1,   r2+1, c2+1), 
                helper(r1+1, c1+1, r2+1, c2-1), 
                helper(r1+1, c1+1, r2+1, c2), 
                helper(r1+1, c1+1, r2+1, c2+1)
                             )
            return max_cherry
        return helper(0, 0, 0, self.COL-1)
    
    
# This solution works - optimization and code clean up after a code review :)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        @lru_cache(None)
        def helper(r, c1, c2):
            if r == self.ROW:
                return 0
            if not 0<=r<=self.ROW-1 or not 0<=c1<=self.COL-1 or not 0<=c2<=self.COL-1:
                return float('-inf')
            
            val = grid[r][c1]
            if c1 != c2:
                val += grid[r][c2]
            
            max_cherry = val + max(helper(r+1, c1+i, c2+j) for i in range(-1, 2) for j in range(-1, 2))
            return max_cherry
        
        self.ROW = len(grid)
        self.COL = len(grid[0])
        ans = helper(0, 0, self.COL-1)
        helper.cache_clear()
        return ans