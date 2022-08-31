# 417. Pacific Atlantic Water Flow
# Medium

# 4815

# 973

# Add to List

# Share
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

# Constraints:

# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105


# This solution works:


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return []

        R = len(matrix)
        C = len(matrix[0])

        reached_pacific = set([])
        reached_atlantic = set([])
        
        queue = deque([(0, c, float('-inf')) for c in range(C)] + [(r, 0, float('-inf')) for r in range(1, R)])
        while queue:
            r, c, prev = queue.popleft()
            # if r, c is invalid, or matrix[r][c] is smaller than the previous value
            if not 0 <= r < R or not 0 <= c < C or matrix[r][c] < prev:
                continue
            if (r, c) in reached_pacific:
                continue
            reached_pacific.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                queue.append((r+dr, c+dc, matrix[r][c]))
        
        queue = deque([(R-1, c, float('-inf')) for c in range(C)] + [(r, C-1, float('-inf')) for r in range(R-1)])
        while queue:
            r, c, prev = queue.popleft()
            # if r, c is invalid, or matrix[r][c] is smaller than the previous value
            if not 0 <= r < R or not 0 <= c < C or matrix[r][c] < prev:
                continue
            if (r, c) in reached_atlantic:
                continue
            reached_atlantic.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                queue.append((r+dr, c+dc, matrix[r][c]))
        
        # print(reached_pacific)
        
        return reached_pacific.intersection(reached_atlantic)