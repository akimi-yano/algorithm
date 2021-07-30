# 542. 01 Matrix
# Medium

# 2858

# 143

# Add to List

# Share
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.


# This solution works: - dijikistra :) and start from 0s !


import heapq
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        minheap = []
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    heapq.heappush(minheap, (0, row, col))
        seen = set([])
        while minheap:
            dist, row, col = heapq.heappop(minheap)
            if (row, col) in seen:
                continue
            seen.add((row, col))
            if mat[row][col] == 0:
                dist = 0
            else:
                dist += 1
                mat[row][col] = dist
            for r, c in ((1,0),(-1,0),(0,1),(0,-1)):
                if 0 <= row+r < len(mat) and 0 <= col+c < len(mat[0]):
                    heapq.heappush(minheap,(dist, row+r, col+c))
        return mat
                