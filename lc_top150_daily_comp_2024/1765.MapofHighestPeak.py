'''
1765. Map of Highest Peak
Medium
Topics
Companies
Hint
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

 

Example 1:



Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.
Example 2:



Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.
 

Constraints:

m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] is 0 or 1.
There is at least one water cell.
 

Note: This question is the same as 542: https://leetcode.com/problems/01-matrix/
'''

import heapq
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        minheap = []
        ROW = len(isWater)
        COL = len(isWater[0])
        ans = [[None for cc in range(COL)] for rr in range(ROW)] 
        
        seen = set([])
        for r in range(ROW):
            for c in range(COL):
                if isWater[r][c]:
                    heapq.heappush(minheap, (0, r, c))

        while minheap:
            val, row, col = heapq.heappop(minheap)
            if (row, col) in seen:
                continue
            seen.add((row, col))
            ans[row][col] = val
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_r, next_c = dr + row, dc + col
                if not(0 <= next_r < ROW) or not(0 <= next_c < COL) or (next_r, next_c) in seen:
                    continue
                heapq.heappush(minheap, (val+1, next_r, next_c))
        return ans

# Another approach using queue

from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROW = len(isWater)
        COL = len(isWater[0])
        ans = [[-1] * COL for _ in range(ROW)] 
        bfs = deque([])

        for r in range(ROW):
            for c in range(COL):
                if isWater[r][c]:
                    bfs.append((r, c))
                    ans[r][c] = 0

        while bfs:
            row, col = bfs.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_r, next_c = dr + row, dc + col
                if not(0 <= next_r < ROW) or not(0 <= next_c < COL) or ans[next_r][next_c] != -1:
                    continue
                ans[next_r][next_c] = ans[row][col] + 1
                bfs.append((next_r, next_c))
        return ans
