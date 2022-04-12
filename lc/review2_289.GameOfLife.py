# 289. Game of Life
# Medium

# 3719

# 395

# Add to List

# Share
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

# Example 1:


# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
 

# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?


# This solution works:


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        1->0 (0 or 1 live nei)
        1->1 (2 or 3 live nei)
        1->0 (4 or more live nei)
        0->1 (3 live)
        
        1 -> 1
        3 -> 1 which will become 0
        0 ->
        2 -> 0 which will become 1
        '''
        ROW = len(board)
        COL = len(board[0])
        
        for row in range(ROW):
            for col in range(COL):
                val = board[row][col]
                neighbors = 0
                
                for delta_r,delta_c in ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)):
                    next_r, next_c = row+delta_r, col+delta_c
                    
                    if (0<=next_r<ROW) and (0<=next_c<COL):
                        neighbors += 1 if board[next_r][next_c] %2 else 0

                if val:
                    if neighbors <= 1 or neighbors >= 4:
                        board[row][col] = 3
                else:
                    if neighbors == 3:
                        board[row][col] = 2
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 3:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1