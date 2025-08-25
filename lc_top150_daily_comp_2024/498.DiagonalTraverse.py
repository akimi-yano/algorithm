'''
498. Diagonal Traverse
Solved
Medium
Topics
premium lock icon
Companies
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROW = len(mat)
        COL = len(mat[0])
        ans = [[] for _ in range(ROW+COL-1)]
        for row in range(ROW):
            for col in range(COL):
                ans[row+col].append(mat[row][col])
        temp = [list(reversed(ans[i])) if i % 2 == 0  else ans[i] for i in range(len(ans))]
        return [val for sub_arr in temp for val in sub_arr]