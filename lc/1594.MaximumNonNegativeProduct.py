# 1594. Maximum Non Negative Product in a Matrix
# Medium

# 24

# 0

# Add to List

# Share
# You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (rows - 1, cols - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.

# Notice that the modulo is performed after getting the maximum product.



# Example 1:

# Input: grid = [[-1,-2,-3],
#                [-2,-3,-3],
#                [-3,-3,-2]]
# Output: -1
# Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
# Example 2:

# Input: grid = [[1,-2,1],
#                [1,-2,1],
#                [3,-4,1]]
# Output: 8
# Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).
# Example 3:

# Input: grid = [[1, 3],
#                [0,-4]]
# Output: 0
# Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).
# Example 4:

# Input: grid = [[ 1, 4,4,0],
#                [-2, 0,0,1],
#                [ 1,-1,1,1]]
# Output: 2
# Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).


# Constraints:

# 1 <= rows, cols <= 15
# -4 <= grid[i][j] <= 4


# This solution works !!!

class Solution:
    mod = 10 ** 9 + 7
    def maxProductPath(self, grid: List[List[int]]) -> int:
        memo = {}
        def helper(row,col,largest,smallest):
            if (row,col,largest,smallest) in memo:
                return memo[(row,col,largest,smallest)]
            if not 0<=row<=len(grid)-1 or not 0<=col<=len(grid[0])-1:
                return float('-inf')
            if row == len(grid)-1  and col == len(grid[0])-1:
                return max(largest * grid[row][col], smallest * grid[row][col])
            best = float('-inf')
            best = max(best,helper(row+1,col,max(largest*grid[row][col],smallest*grid[row][col]), min(largest*grid[row][col],smallest*grid[row][col])))
            best = max(best,helper(row,col+1,max(largest*grid[row][col],smallest*grid[row][col]), min(largest*grid[row][col],smallest*grid[row][col])))
            memo[(row,col,largest,smallest)] = best
            return best
        ans = helper(0,0,1,1) 
        return ans % Solution.mod if ans > -1 else -1