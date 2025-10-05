'''
417. Pacific Atlantic Water Flow
Solved
Medium
Topics
premium lock icon
Companies
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        1) Use DFS from all border cells touching the 
        Pacific and Atlantic oceans.

        2) During DFS only move to neighbors with height ≥ current height.

        3) Maintain two visited sets: pacific and atlantic.

        4) After traversal, the answer is the intersection of these two sets.
        '''
        def dfs(row, col, seen):
            seen.add((row, col))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0 ,-1)):
                next_r, next_c = row+dr, col+dc
                if (0<=next_r<ROW) and (0<=next_c<COL) and ((next_r, next_c) not in seen) and (heights[next_r][next_c] >= heights[row][col]):
                    dfs(next_r, next_c, seen)
        
        ROW = len(heights)
        COL = len(heights[0])
        pacific = set([])
        atlantic = set([])
        for col in range(COL):
            dfs(0, col, pacific)
            dfs(ROW-1, col, atlantic)

        for row in range(ROW):
            dfs(row, 0, pacific)
            dfs(row, COL-1, atlantic)
        
        return list(pacific & atlantic)