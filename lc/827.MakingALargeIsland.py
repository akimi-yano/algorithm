# 827. Making A Large Island
# Hard

# 1338

# 37

# Add to List

# Share
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

 

# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:

# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:

# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.


# This solution works:


class Solution:
    '''
    ii
    iz
    '''
    def largestIsland(self, grid: List[List[int]]) -> int:
        # edge case
        N = len(grid)
        ones = sum(sum(row) for row in grid)
        if ones == N ** 2:
            return ones
        if ones == 0:
            return 1
        
        zeros = set([])
        for r in range(N):
            for c in range(N):
                if not grid[r][c]:
                    zeros.add((r,c))
        
        def helper(r, c, seen):
            nonlocal grid, N
            if not 0 <= r < N or not 0 <= c < N or not grid[r][c]:
                return
            grid[r][c] = 0
            seen.add((r, c))
            helper(r-1, c, seen)
            helper(r+1, c, seen)
            helper(r, c-1, seen)
            helper(r, c+1, seen)
        
        idx = 0
        m = {}
        for r in range(N):
            for c in range(N):
                seen = set([])
                helper(r, c, seen)
                if not seen:
                    continue
                for row, col in seen:
                    m[(row, col)] = idx, len(seen)
                idx += 1
        
        best = float('-inf')
        for r, c in zeros:
            neighbors = set()
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_r, next_c = r + dr, c + dc
                if (next_r, next_c) in m:
                    neighbors.add(m[(next_r, next_c)])
            best = max(best, 1 + sum(neighbor[1] for neighbor in neighbors) if neighbors else 1)
        return best
        