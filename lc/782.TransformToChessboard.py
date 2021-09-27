# 782. Transform to Chessboard
# Hard

# 243

# 261

# Add to List

# Share
# You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.

# Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.

# A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

 

# Example 1:


# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# Explanation: One potential sequence of moves is shown.
# The first move swaps the first and second column.
# The second move swaps the second and third row.
# Example 2:


# Input: board = [[0,1],[1,0]]
# Output: 0
# Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
# Example 3:


# Input: board = [[1,0],[1,0]]
# Output: -1
# Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.
 

# Constraints:

# n == board.length
# n == board[i].length
# 2 <= n <= 30
# board[i][j] is either 0 or 1.


# This solution works:


'''
We can find some invariants of our board:

There will be 2 unique types of row and if n is odd, there should be n/2 of each type; if n is even, there should be (n+1)//2 and (n-1)//2.
The same is for columns.
It can be shown, that these two conditions are sufficient and enough. Then for the first row, if n is odd, we have one option: 10101...01 we need to transform to, if n is even, there are two options: 1010...10 and 0101...01 we need to check. The same is for columns.

Line x1 = sum(i == j for i, j in zip(Cnt_r[0][0], patt1)) will check how many not equal elements we have between our pattern and one of our two types of columns, similar logic is for patt2. Then we have two options: try to make it patt1 or patt2. Sometimes it is not possble to converge to one of them: in fact we can converge only if number of not equal elements is even, because on each step we can reduct number of not-equal elements by 2. Imagine example 1000001111 which we try to make equal to 1010101010. Then we enough to make only 2 steps to transform one to another!

Complexity
Final time complexity is O(n^2), space is also O(n^2), because I keep transposed grid and count rows and columns.

'''
class Solution:
    def movesToChessboard(self, board):
        n = len(board)
        patt1 = ([0, 1]*(n//2+1))[:n]
        patt2 = ([1, 0]*(n//2+1))[:n]
        
        board_t = map(list, zip(*board))
        Cnt_r = list(Counter(tuple(row) for row in board).items())
        Cnt_c = list(Counter(tuple(row) for row in board_t).items())
        if len(Cnt_r) != 2 or len(Cnt_c) != 2: return -1
        if abs(Cnt_r[0][1] - Cnt_r[1][1]) > 1: return -1
        if abs(Cnt_c[0][1] - Cnt_c[1][1]) > 1: return -1
        
        x1 = sum(i != j for i,j in zip(Cnt_r[0][0], patt1))
        y1 = sum(i != j for i,j in zip(Cnt_c[0][0], patt1))
        
        x2 = sum(i != j for i,j in zip(Cnt_r[0][0], patt2))
        y2 = sum(i != j for i,j in zip(Cnt_c[0][0], patt2))
        
        cands_x = [x for x in [x1, x2] if x % 2 == 0]
        cands_y = [y for y in [y1, y2] if y % 2 == 0]
        
        return min(cands_x)//2 + min(cands_y)//2
'''
Remark
We can also notice, that all feasible boards will have the following property:

If n is even, first column and row should have n//2 ones, if n is odd, both of them should have (n+1)//2 or (n-1)//2 ones.
For each rectangle with sides parallel to grid, it has even number of zeroes: it means that all elements uniquely defined by first column and first row.
'''