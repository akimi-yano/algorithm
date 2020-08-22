# 1559. Detect Cycles in 2D Grid

# Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

# A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

# Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

# Return true if any cycle of the same value exists in grid, otherwise, return false.



# Example 1:



# Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the image below:

# Example 2:



# Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:

# Example 3:



# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m <= 500
# 1 <= n <= 500
# grid consists only of lowercase English letters.




# this does not work !!!!!!!! 

# class Solution:
#     def containsCycle(self, grid: List[List[str]]) -> bool:
        
#         def helper(row,col,m,n,seen,s_row,s_col):
#             if not 0<=row<=m-1 or not 0<=col<=n-1:
#                 return False
#             if row == s_row and col == s_col:
#                 return True
#             if (row,col) in seen:
#                 return False
            
#             seen.add((row,col))
#             d1=helper(row+1,col)
#             d2=helper(row-1,col)
#             d3=helper(row,col+1)
#             d4=helper(row,col-1)
            
#             return d1  or d2 or d3 or d4
        
#         for row in range(len(grid)):
#             for col in range(len(grid[row])):
#                 if helper(row,col,len(grid),len(grid[row]),set([]),row,col):
#                     return True
#         return False



# YAY - this solution works and  its intuitive - used the depth of recursion to count the length which  has to be longer than 4 !

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.R = len(grid)
        self.C = len(grid[0])
        self.grid = grid
        self.visited = {}
        for row in range(self.R):
            for col in range(self.C):
                target = grid[row][col]
                if self.helper(row, col, target, 0):
                    return True
        return False
    
    def helper(self, row, col, target, depth):
        if not 0 <= row < self.R or not 0 <= col < self.C or self.grid[row][col] != target:
            return False
        if (row, col) in self.visited:
            # if depth difference >= 3, we have a cycle
            return depth - self.visited[(row, col)] >= 4
        
        # else, we are visiting for the first time
        self.visited[(row, col)] = depth
        return self.helper(row+1, col, target, depth+1) or self.helper(row-1, col, target, depth+1) or self.helper(row, col+1, target, depth+1) or self.helper(row, col-1, target, depth+1)