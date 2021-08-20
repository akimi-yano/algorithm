# 36. Valid Sudoku
# Medium

# 3180

# 601

# Add to List

# Share
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.

# This solution works:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def validate(row, col, val):
            
            for c in range(COL):
                if c != col and board[row][c] == val:
                    return False
            
            for r in range(ROW):
                if r != row and board[r][col] == val:
                    return False

            start_row = row//3*3
            end_row = start_row+3
            start_col = col//3*3
            end_col = start_col+3
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if not(r == row and c == col) and board[r][c] == val:
                        return False
            return True
        
        ROW = len(board)
        COL = len(board[0])
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] != "." and not validate(row, col, board[row][col]):
                    return False
        return True