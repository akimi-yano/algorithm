# 130. Surrounded Regions
# Medium

# 3725

# 927

# Add to List

# Share
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

# Example 1:


# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.


# This solution works:


'''
In this problem we need to understand, what exactly surrouned by 'X' means. It actually means that if we start from 'O' at the border, and we traverse only 'O', only those 'O' are not surrouned by 'X'. So the plan is the following:

Start dfs or bfs from all 'O', which are on the border.
When we traverse them, let us color them as 'T', temporary color.
Now, when we traverse all we wanted, all colors which are not 'T' need to renamed to 'X' and all colors which are 'T' need to be renamed to 'O', and that is all!
Compexity: time complextiy is O(mn), where m and n are sizes of our board. Additional space complexity can also go upto O(mn) to keep stack of recursion.
'''
class Solution:
    def dfs(self, i, j):
        if i<0 or j<0 or i>=self.M or j>=self.N or self.board[i][j] != "O":
            return
        self.board[i][j] = 'T'
        neib_list = [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]
        for x, y in neib_list:
            self.dfs(x, y)
    
    def solve(self, board):
        if not board: return 0
        self.board, self.M, self.N = board, len(board), len(board[0])
        
        for i in range(0, self.M):
            self.dfs(i,0)
            self.dfs(i,self.N-1)
            
        for j in range(0, self.N):
            self.dfs(0,j)
            self.dfs(self.M-1,j)
        
        for i,j in product(range(self.M), range(self.N)):
            board[i][j] = "X" if board[i][j] != "T" else "O"


# This solution works:


class Solution:   
    def solve(self, board):
        def helper(row, col, look, symbol):
            if not(0<=row<ROW) or not(0<=col<COL) or board[row][col]!=look:
                return
            board[row][col] = symbol
            helper(row, col+1, look, symbol)
            helper(row, col-1, look, symbol)
            helper(row+1, col, look, symbol)
            helper(row-1, col, look, symbol)
        
        ROW = len(board)
        COL = len(board[0])
        for row in range(ROW):
            if board[row][0] == 'O':
                helper(row, 0, 'O', 'F')
            if board[row][COL-1] == 'O':
                helper(row, COL-1, 'O', 'F')
        for col in range(COL):
            if board[0][col] == 'O':
                helper(0, col, 'O', 'F')
            if board[ROW-1][col] == 'O':
                helper(ROW-1, col, 'O', 'F')
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 'O':
                    helper(row, col, 'O', 'X')
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 'F':
                    helper(row, col, 'F', 'O')
        