# 778. Swim in Rising Water
# Hard

# 1151

# 92

# Add to List

# Share
# On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

# Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

# Example 1:

# Input: [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# Example 2:

# Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation:
#  0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6

# The final route is marked in bold.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
# Note:

# 2 <= N <= 50.
# grid[i][j] is a permutation of [0, ..., N*N - 1].

# This solution works:

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap = [(grid[0][0], 0, 0)]
        seen = set([])
        while minheap:
            t, row, col = heapq.heappop(minheap)
            if row == len(grid)-1 and col == len(grid[0])-1:
                return t
            if (row, col) in seen:
                continue
            seen.add((row, col))
            for r, c in ((1,0),(-1,0),(0,1),(0,-1)):
                next_r = row+r
                next_c = col+c
                if 0<=next_r<len(grid) and 0<=next_c<len(grid[0]):
                    heapq.heappush(minheap, (max(grid[next_r][next_c], t), next_r, next_c))