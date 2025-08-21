'''
1504. Count Submatrices With All Ones
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n binary matrix mat, return the number of submatrices that have all ones.

 

Example 1:


Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:


Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
 

Constraints:

1 <= m, n <= 150
mat[i][j] is either 0 or 1.
'''

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ROW = len(mat)
        COL = len(mat[0])

        # make histogram 
        for i in range(ROW):
            for j in range(COL):
                if mat[i][j] and i > 0: 
                    mat[i][j] += mat[i-1][j] #histogram 
        
        ans = 0
        for i in range(ROW):
            stack = [] #mono-stack of indices of non-decreasing height
            cnt = 0
            for j in range(COL):
                while stack and mat[i][stack[-1]] > mat[i][j]: 
                    jj = stack.pop()                          #start
                    kk = stack[-1] if stack else -1           #end
                    cnt -= (mat[i][jj] - mat[i][j])*(jj - kk) #adjust to reflect lower height

                cnt += mat[i][j] #count submatrices bottom-right at (i, j)
                ans += cnt
                stack.append(j)

        return ans