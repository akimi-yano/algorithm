# 289. Game of Life
# Medium

# 2318

# 318

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



# This solution works 

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Any live cell with fewer than two live neighbors dies as if caused by under-population.
        # Any live cell with two or three live neighbors lives on to the next generation.
        # Any live cell with more than three live neighbors dies, as if by over-population.
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        
        #       2  3
        #   die live die  - (live)
        #         live    - (dead)
        R = len(board)
        C = len(board[0])
        temp_a = []
        for row in range(R):
            temp_r = []
            for col in range(C):
                neib = 0
                for new_row in (row-1, row, row+1):
                    for new_col in (col-1, col, col+1):
                        if new_row == row and new_col == col:
                            continue
                        if 0 <= new_row < R and 0 <= new_col < C: 
                            neib += board[new_row][new_col]
                
                if board[row][col] == 0:
                    if neib == 3:
                        temp_r.append(1) 
                    else:
                        temp_r.append(0) 
                else:
                    if neib < 2 or neib > 3:
                        temp_r.append(0)
                    else:
                        temp_r.append(1) 
                
            temp_a.append(temp_r)
        
        for row in range(R):
            for col in range(C):
                board[row][col] = temp_a[row][col]
        

