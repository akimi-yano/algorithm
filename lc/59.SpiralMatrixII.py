# 59. Spiral Matrix II
# Medium

# 2707

# 166

# Add to List

# Share
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20


# This solution works:


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        maxrow = maxcol = n-1
        minrow = mincol = 0
        count = 1
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        while count <= n**2:
            for col in range(mincol, maxcol+1):
                ans[minrow][col] = count
                count += 1
            minrow += 1

            for row in range(minrow, maxrow+1):
                ans[row][maxcol] = count
                count += 1
            maxcol -= 1

            for col in range(maxcol, mincol-1, -1):
                ans[maxrow][col] = count
                count += 1
            maxrow -= 1

            for row in range(maxrow, minrow-1, -1):
                ans[row][mincol] = count
                count += 1
            mincol += 1
        return ans