'''
407. Trapping Rain Water II
Solved
Hard
Topics
premium lock icon
Companies
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
'''

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROW, COL = len(heightMap), len(heightMap[0])
        seen = set([])

        # 1) Push all boundary cells into a min-heap.
        minheap = []
        for r in range(ROW):
            height = heightMap[r][0]
            heapq.heappush(minheap, (height, r, 0))
            seen.add((r, 0))
            height = heightMap[r][COL-1]
            heapq.heappush(minheap, (height, r, COL-1))
            seen.add((r, COL-1))
        for c in range(1, COL-1):
            height = heightMap[0][c]
            heapq.heappush(minheap, (height, 0, c))
            seen.add((0, c))
            height = heightMap[ROW-1][c]
            heapq.heappush(minheap, (height, ROW-1, c))
            seen.add((ROW-1, c))
        
        ans = 0
        # 2) Repeatedly pop the lowest boundary cell from the minheap.
        while minheap:
            height, row, col = heapq.heappop(minheap)
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_row, next_col = row + dr, col + dc
                if not (0 <= next_row < ROW) or not (0 <= next_col < COL) or (next_row, next_col) in seen:
                    continue
                neighbor_height = heightMap[next_row][next_col]
                ans += max(0, height - neighbor_height) # If the neighbor is lower, water is trapped = currentHeight - neighborHeight
                heapq.heappush(minheap, (max(height, neighbor_height), next_row, next_col))
                seen.add((next_row, next_col))
        return ans