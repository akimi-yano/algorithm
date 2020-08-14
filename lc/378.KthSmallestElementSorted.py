# 378. Kth Smallest Element in a Sorted Matrix

# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.

# This works! but there must be a better way!
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxheap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):  
                heapq.heappush(maxheap,matrix[row][col]*(-1))
                if len(maxheap)>k:
                    heapq.heappop(maxheap)
        return maxheap[0]*(-1)