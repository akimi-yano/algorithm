'''
36. Valid Sudoku
Solved
Medium
Topics
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

# This approach works:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])

        # checking rows 
        for row in range(ROW):
            seen = set([])
            for col in range(COL):
                val = board[row][col]
                if  val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # checking cols
        for col in range(COL):
            seen = set([])
            for row in range(ROW):
                val = board[row][col]
                if  val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)

        # checking the 3 x 3
        for start_row in range(0, ROW, 3):
            for start_col in range(0, COL, 3):
                seen = set([])
                for row in range(start_row, start_row+3):
                    for col in range(start_col, start_col+3):
                        val = board[row][col]
                        if  val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True

# Time: O(N^2)
# Space: O(N^2)

# This approach also works and is more elegant :
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])

        seen = []
        for row in range(ROW):
            for col in range(COL):
                val = board[row][col]
                if val != '.':
                    seen.append((row, val))
                    seen.append((val, col))
                    seen.append((row//3, col//3, val))
        return len(seen) == len(set(seen))
    
# Time: O(N^2)
# Space: O(N^2)

