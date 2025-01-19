'''
407. Trapping Rain Water II
Hard
Topics
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
        R, C = len(heightMap), len(heightMap[0])
        heap = []
        for r in range(R):
            height = heightMap[r][0]
            heapq.heappush(heap, (height, r, 0))
            height = heightMap[r][C-1]
            heapq.heappush(heap, (height, r, C-1))
        for c in range(1, C-1):
            height = heightMap[0][c]
            heapq.heappush(heap, (height, 0, c))
            height = heightMap[R-1][c]
            heapq.heappush(heap, (height, R-1, c))
        
        ans = 0
        seen = set([])
        while heap:
            height, row, col = heapq.heappop(heap)
            queue = deque([(row, col)])
            while queue:
                cur_row, cur_col = queue.popleft()
                if (cur_row, cur_col) in seen:
                    continue
                seen.add((cur_row, cur_col))
                ans += height-heightMap[cur_row][cur_col]
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_row, next_col = cur_row + dr, cur_col + dc
                    if not 0 <= next_row < R or not 0 <= next_col < C:
                        continue
                    next_height = heightMap[next_row][next_col]
                    if next_height <= height:
                        queue.append((next_row, next_col))
                    else:
                        heapq.heappush(heap, (next_height, next_row, next_col))
        return ans