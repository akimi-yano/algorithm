'''
773. Sliding Puzzle
Solved
Hard
Topics
Companies
Hint
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

Example 1:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Example 2:


Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Example 3:


Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
 

Constraints:

board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
'''

from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        ROW = len(board)
        COL = len(board[0])

        tup_board = tuple(tuple(c for c in r) for r in board)

        queue = deque([])
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 0:
                    queue.append((row, col, 0, tup_board))

        seen = set([tup_board])
        goal = ((1, 2, 3),(4, 5, 0))

        while queue:
            row, col, steps, tup_board = queue.popleft()
       
            if tup_board == goal:
                return steps

            for delta_r, delta_c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_r, next_c = delta_r + row, delta_c + col

                if (0<=next_r<ROW) and (0<=next_c<COL):
                    newboard = list(list(col for col in row) for row in tup_board)
                    newboard[row][col], newboard[next_r][next_c] = newboard[next_r][next_c], newboard[row][col]
                    tup_newboard = tuple(tuple(c for c in r) for r in newboard)
                    if tup_newboard not in seen:
                        queue.append((next_r, next_c, steps+1, tup_newboard))
                        seen.add(tup_newboard)
        return -1