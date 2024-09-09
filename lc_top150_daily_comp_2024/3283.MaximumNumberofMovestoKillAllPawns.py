'''
3283. Maximum Number of Moves to Kill All Pawns
Hard
Companies
Hint
There is a 50 x 50 chessboard with one knight and some pawns on it. You are given two integers kx and ky where (kx, ky) denotes the position of the knight, and a 2D array positions where positions[i] = [xi, yi] denotes the position of the pawns on the chessboard.

Alice and Bob play a turn-based game, where Alice goes first. In each player's turn:

The player selects a pawn that still exists on the board and captures it with the knight in the fewest possible moves. Note that the player can select any pawn, it might not be one that can be captured in the least number of moves.
In the process of capturing the selected pawn, the knight may pass other pawns without capturing them. Only the selected pawn can be captured in this turn.
Alice is trying to maximize the sum of the number of moves made by both players until there are no more pawns on the board, whereas Bob tries to minimize them.

Return the maximum total number of moves made during the game that Alice can achieve, assuming both players play optimally.

Note that in one move, a chess knight has eight possible positions it can move to, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.



 

Example 1:

Input: kx = 1, ky = 1, positions = [[0,0]]

Output: 4

Explanation:



The knight takes 4 moves to reach the pawn at (0, 0).

Example 2:

Input: kx = 0, ky = 2, positions = [[1,1],[2,2],[3,3]]

Output: 8

Explanation:



Alice picks the pawn at (2, 2) and captures it in two moves: (0, 2) -> (1, 4) -> (2, 2).
Bob picks the pawn at (3, 3) and captures it in two moves: (2, 2) -> (4, 1) -> (3, 3).
Alice picks the pawn at (1, 1) and captures it in four moves: (3, 3) -> (4, 1) -> (2, 2) -> (0, 3) -> (1, 1).
Example 3:

Input: kx = 0, ky = 0, positions = [[1,2],[2,4]]

Output: 3

Explanation:

Alice picks the pawn at (2, 4) and captures it in two moves: (0, 0) -> (1, 2) -> (2, 4). Note that the pawn at (1, 2) is not captured.
Bob picks the pawn at (1, 2) and captures it in one move: (2, 4) -> (1, 2).
 

Constraints:

0 <= kx, ky <= 49
1 <= positions.length <= 15
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 49
All positions[i] are unique.
The input is generated such that positions[i] != [kx, ky] for all 0 <= i < positions.length.
'''

from collections import deque
class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        moves = ((2, 1),(1, 2),(-1, 2),(-2, 1),(-2, -1),(-1, -2),(1, -2),(2, -1))

        '''
        alice: maximize the num moves
        bob: minimize the num moves

        call the function get_num_moves() which returns the fewest moves possible
        alice chooses the largest moves and bob chooses the smallest moves
        
        use bit mask to keep track of which positions are remaining, and where the current x and y are
        '''
        @cache
        def get_num_moves(x, y, i):
            goal_x, goal_y = positions[i]
            visited = set([(x, y)])
            queue = deque([(x, y, 0)])
            while queue:
                cur_x, cur_y, num_step = queue.popleft()
                if cur_x == goal_x and cur_y == goal_y:
                    return num_step
                for dx, dy in moves:
                    next_x = cur_x + dx
                    next_y = cur_y + dy
                    if (next_x, next_y) in visited:
                        continue
                    visited.add((next_x, next_y))
                    if 0 <= next_x < 50 and 0 <= next_y < 50:
                        queue.append((next_x, next_y, num_step+1))
            return float('inf')

        @cache
        def helper(positions_used, x, y, is_alice):
            if not (0<=x<50) or not(0<=y<50):
                return 0
            if positions_used == COMPLETE_BITMASK:
                return 0
            # if alice the best means the max, if bob the best means the min
            best = float('-inf') if is_alice else float('inf')
            for i in range(len(positions)):
                # if this position is not used, I can use it
                if not (1<<i & positions_used): 
                    num_moves = get_num_moves(x, y, i) 
                    new_positions_used = 1<<i | positions_used    
                    if is_alice:
                        best = max(best, num_moves + helper(new_positions_used, positions[i][0], positions[i][1], 0))
                    else:
                        best = min(best, num_moves + helper(new_positions_used, positions[i][0], positions[i][1], 1))
            return best
            
        val = 0
        for j in range(len(positions)):
            val = 1 << j | val
        COMPLETE_BITMASK = val
        return helper(0, kx, ky, 1)