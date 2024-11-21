'''
2257. Count Unguarded Cells in the Grid
Attempted
Medium
Topics
Companies
Hint
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
 

Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.
'''

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 1
        
        for r, c in walls:
            grid[r][c] = 2
        
        def mark_guarded(r, c):
            for row in range(r+1, m):
                if grid[row][c] in (1, 2):
                    break
                grid[row][c] = 3
            
            for row in reversed(range(0, r)):
                if grid[row][c] in (1, 2):
                    break
                grid[row][c] = 3

            for col in range(c+1, n):
                if grid[r][col] in (1, 2):
                    break
                grid[r][col] = 3

            for col in reversed(range(0, c)):
                if grid[r][col] in (1, 2):
                    break
                grid[r][col] = 3

        for r, c in guards:
            mark_guarded(r, c)
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    ans += 1
        return ans