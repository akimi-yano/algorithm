'''
36. Valid Sudoku
Solved
Medium
Topics
premium lock icon
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
        (0,0),(0,1),(0,2)|(0,3),(0,4),(0,5)
        (1,0),(1,1),(1,2)
        (2,0),(2,1),(2,2)
        -
        (3,0),(3,1)
        (4,0)

        0<=r<=2
        '''
        N = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for row in range(N):
            for col in range(N):
                if board[row][col] != '.':
                    if board[row][col] in rows[row] or board[row][col] in cols[col]:
                        return False
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col]) 

        for start_row in range(0,N,3):
            for start_col in range(0,N,3):
                seen = set([])
                for row in range(start_row, start_row+3):
                    for col in range(start_col, start_col+3):
                        if board[row][col] != '.':
                            if  board[row][col] in seen:
                                return False
                            seen.add(board[row][col])
        
        return True
    
# Another approach/ optimization:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        (r // 3, c // 3)
        (0,0),(0,1),(0,2)|(0,3),(0,4),(0,5)
        (1,0),(1,1),(1,2)
        (2,0),(2,1),(2,2)
        -
        (3,0),(3,1)
        (4,0)

        0<=r<=2
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[(row//3, col//3)]:
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col]) 
                boxes[(row//3, col//3)].add(board[row][col]) 
        
        return True