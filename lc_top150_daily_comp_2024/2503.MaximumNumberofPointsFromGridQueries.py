'''
2503. Maximum Number of Points From Grid Queries
Hard
Topics
Companies
Hint
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106
'''

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        '''
        As we can only traverse adjacent cells, process smaller values first to maintain a valid traversal path ! -> use minheap
        '''
        ROW = len(grid)
        COL = len(grid[0])
        ans = [0] * len(queries)
        sorted_queries = sorted([(query_num, query_index) for query_index, query_num in enumerate(queries)])
        minheap = []
        visited = set([])
        points = 0

        # Add the first one already
        heapq.heappush(minheap, (grid[0][0], 0, 0))  # (grid_val, row, col) 
        visited.add((0,0))

        for query_num, query_index in sorted_queries:
            while minheap and minheap[0][0] < query_num:
                grid_val, row, col = heapq.heappop(minheap)
                points += 1

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row, next_col = row + dr, col + dc
                    if 0<=next_row<ROW and 0<=next_col<COL and (next_row, next_col) not in visited:
                        visited.add((next_row, next_col))
                        heapq.heappush(minheap, (grid[next_row][next_col], next_row, next_col))
            ans[query_index] = points
                
        return ans    
