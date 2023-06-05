'''
36. Valid Sudoku
Medium
8.8K
918
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

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        9x9
        '''
        def check_row():
            for row in range(9):
                seen = set([])
                for col in range(9):
                    if board[row][col] in seen:
                        return False
                    if board[row][col] != ".":
                        seen.add(board[row][col])
            return True
        
        def check_col():
            for col in range(9):
                seen = set([])
                for row in range(9):
                    if board[row][col] in seen:
                        return False
                    if board[row][col] != ".":
                        seen.add(board[row][col])
            return True
        
        def check_3x3():
            for start_row in range(0,9,3):
                for start_col in range(0,9,3):
                    seen = set([])
                    for row in range(3):
                        for col in range(3):
                            if board[start_row+row][start_col+col] in seen:
                                return False
                            if board[start_row+row][start_col+col] != ".":
                                seen.add(board[start_row+row][start_col+col])          
            return True
                        
        row = check_row() 
        col = check_col() 
        three = check_3x3()
        return row and col and three

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def validate(row, col, val):
            
            # row check
            for c in range(9):
                if not(c == col) and board[row][c] == val:
                    return False
                
            # col check
            for r in range(9):
                if not(r == row) and board[r][col] == val:
                    return False
            
            # 3x3 check
            start_row = row//3*3
            start_col = col//3*3
            end_row = start_row+3
            end_col = start_col+3
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if not(r == row) and  not(c == col) and board[r][c] == val:
                        return False
            return True
        
        for row in range(9):
            for col in range(9):
                if board[row][col] != "." and not validate(row, col, board[row][col]):
                    return False
        return True