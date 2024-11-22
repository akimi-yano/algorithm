'''
1072. Flip Columns For Maximum Number of Equal Rows
Medium
Topics
Companies
Hint
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.
'''

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:        
        '''
        1 0 0
        0 1 1
        1 0 1
        0 1 0

        0 1 1
        0 1 1
        0 1 0
        0 1 0

        '0 1 1' -> 2
        '0 1 0' -> 2
        '''
        ROW = len(matrix)
        COL = len(matrix[0])
        for row in range(ROW):
            if matrix[row][0] != 0:
                for col in range(COL):
                    matrix[row][col] ^= 1

        patterns = {}
        for row in range(ROW):
            pattern = tuple(matrix[row])
            if pattern not in patterns:
                patterns[pattern] = 0
            patterns[pattern] += 1
        return max(patterns.values())