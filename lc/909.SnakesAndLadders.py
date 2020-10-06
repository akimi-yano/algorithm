# 909. Snakes and Ladders
# Medium

# 426

# 935

# Add to List

# Share
# On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:


# You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

# You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
# (This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
# If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
# A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

# Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

# Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

# Example 1:

# Input: [
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation: 
# At the beginning, you start at square 1 [at row 5, column 0].
# You decide to move to square 2, and must take the ladder to square 15.
# You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
# You then decide to move to square 14, and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
# Note:

# 2 <= board.length = board[0].length <= 20
# board[i][j] is between 1 and N*N or is equal to -1.
# The board square with number 1 has no snake or ladder.
# The board square with number N*N has no snake or ladder.

# This approach does not work 

# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#         M = len(board)
#         N = len(board[0])
        
#         sample = [[None for i in range(N)] for k in range(M)]
#         # print(sample)
#         for row in range(M):
#             for col in range(N):
#                 if row%2 == 0:
#                     largest = M * (M - row)
#                     val = largest - col
#                     sample[row][col] = val
#                 else:
#                     val = M * ( M - (row+1) ) + (col+1)
#                     sample[row][col] = val
#         # print(sample)
        
#         jumps = {}
#         for row in range(M):
#             for col in range(N):
#                 if board[row][col] != -1:
#                     if row % 2 == 0:
#                         largest = M * (M - row)
#                         val = largest - col
#                     else:
#                         val = M * ( M - (row+1) ) + (col+1)
#                     jumps[val] = board[row][col]
                    
#         # print(jumps)
        
#         def helper(row, col):
#             if not 0<=row<=M-1 or not 0<=col<=N-1:
#                 return float('inf')
#             if sample[row][col] in jumps:
#                 new_val = jumps[sample[row][col]]
#                 # get the row and col for the new val
#                 row =  M - new_val // M
#                 if row %2 == 0:
#                     col = new_val//M
#                 else:
#                     col = new_val - new_val//M
                
#             if sample[row][col] == M*N:
#                 return 0

#             min_steps = float('inf')
#             if row % 2!=0:
#                 for maybe_col in range(1, 7):
#                     next_col = col + maybe_col 
#                     flipped = False
#                     if next_col > N-1:
#                         next_col %= N
#                         flipped = True
                    
#                     if flipped:
#                         min_steps = min(min_steps, 1 + helper(row-1, N-next_col) )
#                     else:
#                         min_steps = min(min_steps, 1 + helper(row, next_col) )
            
#             else:
#                 for maybe_col in range(1, 7):
#                     next_col = col - maybe_col 
#                     flipped = False
#                     if next_col < 0:
#                         next_col %= N
#                         flipped = True
                    
#                     if flipped:
#                         min_steps = min(min_steps, 1 + helper(row-1, next_col) )
#                     else:
#                         min_steps = min(min_steps, 1 + helper(row, next_col) )
#             return min_steps
#         return helper(M-1,0)
    

# This way does not work:
    
# from collections import deque

# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#         queue = deque([(1, 0)])
#         N = len(board)
#         target = N ** 2
#         seen = set([])
#         while len(queue) > 0:
#             num, level = queue.popleft()
#             if num in seen:
#                 continue
#             seen.add(num)

#             if num == target:
#                 return level

#             for delta in range(1, 7):
#                 next_num = num + delta
#                 if next_num > target:
#                     continue
#                 row, col = self.get_loc(next_num, N)
#                 print(row, col)
#                 if board[row][col] == -1:
#                     queue.append((next_num, level+1))
#                 else:
#                     queue.append((board[row][col], level+1))
                
#         return -1
    
#     def get_loc(self, num, N):
#         # print(num)
#         row = N -1 -(num //N)
#         if row % 2 == 0:
#             max_val = N * (N - row)
#             col = max_val -  num  -1
#         else:
#             col = num - (N * (N - row -1) +1)
#         # print(row,  col)
#         return (row, col)


# This solution works !!!!
'''
BFS 

TO GET ROW:
N-1 - (num-1)//N

TO GET COL:
                
(num-1)%N   <-start and end etc.
if (N-row) % 2 == 0:
    N-1-((num-1)%N)
'''

from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # start with a tuple of val and path#
        queue = deque([(1, 0)])
        N = len(board)
        # its a square matrix
        target = N ** 2
        seen = set([])
        while len(queue) > 0:
            num, level = queue.popleft()
            # use seen set to not go to the same path
            if num in seen:
                continue
            seen.add(num)
            # found the answer 
            if num == target:
                return level

            for delta in range(1, 7):
                next_num = num + delta
                # important ! don't put it into queue if it  goes over the target
                if next_num > target:
                    continue
                # we need the row and col index because we need to check if its -1 or snake or ladder
                row, col = self.get_loc(next_num, N)
                print(row, col)
                if board[row][col] == -1:
                    queue.append((next_num, level+1))
                else:
                    # if  it's snake or ladder, just use the value
                    queue.append((board[row][col], level+1))
                
        return -1
    
    def get_loc(self, num, N):
        # find row
        row = N -1 - ((num-1) //N)
        
        # find col
        col = (num-1) % N
        if (N-row) % 2 == 0:
            col = N - 1 - col
        return (row, col)