# 289. Game of Life

# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# Example:

# Input: 
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output: 
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


# This solution does not work ! need to change in  place!

# class Solution:

    # def gameOfLife(self, board: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     self.board = board
    #     ans = [[None for _ in range(len(board[0]))] for _ in range(len(board))]
    #     for row in range(len(board)):
    #         for col in range(len(board[row])):
    #             live= self.count_neighbors(row,col)
    #             if board[row][col] == 1 and live<2:
    #                 ans[row][col] = 0
    #             elif board[row][col] == 1 and 2<=live<=3:
    #                 ans[row][col] = 1
    #             elif board[row][col] == 1 and 3<live:
    #                 ans[row][col] = 0 
    #             elif board[row][col] == 0 and live == 3:
    #                 ans[row][col] = 1
    #             else:
    #                 ans[row][col] = 0 
    #     board = ans       
    #     print(ans)
        
    # def count_neighbors(self,row,col):
    #     live = 0
    #     m = len(self.board)
    #     n = len(self.board[0])
    #     for r,c in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
    #         if 0<=r+row<=m-1 and 0<=c+col<=n-1:
    #             if self.board[r+row][c+col] == 1:
    #                 live+=1
    #     return live
                        




# This solution works !!!!

'''
To update the matrix in place there are 2 steps:

    1) use -1 and 2 to express the changed ones -> originally 1 is either 1 or 2 !
    die->live : -1
    live->die : 2
    
    2) update the -1 and 2 back to 1 and 0!
    -1 -> 1
    2 -> 0 
'''


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 

        m = len(board)
        n = len(board[0])
        
        for row in range(m):
            for col in range(n):
                live= self.count(row,col,board,m,n)
                if board[row][col] == 1 and (live<2 or 3<live):
                    board[row][col] = 2
                    
                elif board[row][col] == 0 and live == 3:
                    board[row][col] = -1
      
        self.update(board,m,n)
        
    def count(self,row,col,board,m,n):
        live = 0
        for r,c in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            if 0<=r+row<=m-1 and 0<=c+col<=n-1:
                if board[r+row][c+col] == 1 or board[r+row][c+col] == 2:
                    live+=1
        return live
                        
    def update(self,board, m, n):
        for row in range(m):
            for col in range(n):
                if board[row][col] == 2:
                    board[row][col] = 0 
                elif board[row][col] == -1:
                    board[row][col] = 1
 
        