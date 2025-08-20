'''
1277. Count Square Submatrices with All Ones
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])

        @cache
        def helper(row, col):
            if matrix[row][col]==1:
                if row!=0 and col!=0:
                    return min(helper(row-1, col), helper(row, col-1), helper(row-1, col-1))+1
                else:
                    return 0+1
            else:
                return 0
        
        return sum(helper(row, col) for row in range(ROW) for col in range(COL))