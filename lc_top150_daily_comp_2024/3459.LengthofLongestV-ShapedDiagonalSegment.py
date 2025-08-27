'''
3459. Length of Longest V-Shaped Diagonal Segment
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

The segment starts with 1.
The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
The segment:
Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
Continues the sequence in the same diagonal direction.
Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.


Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

 

Example 1:

Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 5

Explanation:



The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:

Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 4

Explanation:



The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:

Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]

Output: 5

Explanation:



The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:

Input: grid = [[1]]

Output: 1

Explanation:

The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

 

Constraints:

n == grid.length
m == grid[i].length
1 <= n, m <= 500
grid[i][j] is either 0, 1 or 2.
'''

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        best = 0
        directions = [[1,1],[1,-1],[-1,-1],[-1,1]]
        next_target = [2,2,0] 
        
        @cache
        def helper(row, col, cur_target, d, can_use):
            if not (0<=row<ROW) or not (0<=col<COL):
                return 0
            if grid[row][col] != cur_target:
                return 0
            res = helper(row + directions[d][0], col + directions[d][1], next_target[cur_target], d, can_use) + 1
            if can_use > 0:
                d2 = (d + 1) % 4
                res_2 = helper(row + directions[d2][0], col + directions[d2][1], next_target[cur_target], d2, 0) + 1
                res = max(res, res_2)
            return res

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    cur = max(helper(row, col, 1, d, 1) for d in range(4))
                    best = max(best, cur)
        return best