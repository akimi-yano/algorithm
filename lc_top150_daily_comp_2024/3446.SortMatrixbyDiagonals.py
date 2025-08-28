'''
3446. Sort Matrix by Diagonals
Medium
Topics
premium lock icon
Companies
Hint
You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
 

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Explanation:



The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

[7, 2] becomes [2, 7].
[3] remains unchanged.
Example 2:

Input: grid = [[0,1],[1,2]]

Output: [[2,1],[1,0]]

Explanation:



The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

Example 3:

Input: grid = [[1]]

Output: [[1]]

Explanation:

Diagonals with exactly one element are already in order, so no changes are needed.

 

Constraints:

grid.length == grid[i].length == n
1 <= n <= 10
-105 <= grid[i][j] <= 105
'''

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        [0,2]
        [0,1], [1,2]
        [0,0], [1,1]
        [1,0], [2,1]
        [2,0]
        '''
        N = len(grid)
        temp_grid = []
        for start_col in range(N-1,0,-1):
            temp_row = []   
            col = start_col
            row = 0
            while row < N and col < N:
                temp_row.append(grid[row][col])
                row += 1
                col += 1
            temp_row.sort()
            temp_grid.append(temp_row)
        
        for start_row in range(N):
            temp_row = []   
            col = 0
            row = start_row
            while row < N and col < N:
                temp_row.append(grid[row][col])
                row += 1
                col += 1
            temp_row.sort(reverse=True)
            temp_grid.append(temp_row)
        # print(temp_grid, grid)
        arr = [c for r in temp_grid for c in r ]
        # print(arr)
        
        # WRITE
        i = 0
        for start_col in range(N-1,0,-1):
            col = start_col
            row = 0
            while row < N and col < N:
                grid[row][col] = arr[i]
                row += 1
                col += 1
                i += 1
        
        for start_row in range(N):
            col = 0
            row = start_row
            while row < N and col < N:
                grid[row][col] = arr[i]
                row += 1
                col += 1
                i += 1
        
        return grid

# Another approach - shorter code:

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        [0,2] : -2
        [0,1], [1,2] : -1
        [0,0], [1,1] : 0
        [1,0], [2,1] : 1
        [2,0] : 2
        '''
        diagonals = defaultdict(list)
        N = len(grid)
        
        for row in range(N):
            for col in range(N):
                diagonals[row-col].append(grid[row][col])
        
        for k in diagonals:
            diagonals[k].sort(reverse=(k<0)) # reverse it cuz i wanna pop later
        
        for row in range(N):
            for col in range(N):
                grid[row][col] = diagonals[row-col].pop()
        
        return grid