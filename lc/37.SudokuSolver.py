# 37. Sudoku Solver
# Hard

# 3562

# 117

# Add to List

# Share
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

 

# Example 1:


# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.


# This solution works:


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.b = board
        self.emptyCells = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    self.emptyCells.append((i, j))
                    
        self.backTrack()
    
    def backTrack(self) -> None:
        if not self.emptyCells: return True
        
        x, y = self.emptyCells.pop(0)
        
        for val in range(1, 10):
            if self.isValid(x, y, str(val)):
                self.b[x][y] = str(val)
                if self.backTrack():
                    return True
                else:
                    self.b[x][y] = '.'
            
        self.emptyCells.insert(0, (x, y))
        return False
                    
    def isValid(self, row: int, col: int, c: str) -> bool:
        for i in range(9):
            if self.b[i][col] != '.' and self.b[i][col] == c: return False
            if self.b[row][i] != '.' and self.b[row][i] == c: return False
            if self.b[3 * (row // 3) + i // 3][ 3 * (col // 3) + i % 3] != '.' and self.b[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c: return False
        
        return True