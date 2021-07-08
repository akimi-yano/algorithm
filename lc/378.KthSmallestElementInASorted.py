# 378. Kth Smallest Element in a Sorted Matrix
# Medium

# 4139

# 201

# Add to List

# Share
# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 

# Constraints:

# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2

# This solution works - push all the elements into a new array and sort:

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        R = len(matrix)
        C = len(matrix[0])
        for row in range(R):
            for col in range(C):
                ans.append(matrix[row][col])
        ans.sort()
        return ans[k-1]

# This solution works - maxheap of size k:

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxheap = []
        R = len(matrix)
        C = len(matrix[0])
        for row in range(R):
            for col in range(C):
                heapq.heappush(maxheap, -matrix[row][col])
                if len(maxheap) > k:
                    heapq.heappop(maxheap)
        return -heapq.heappop(maxheap)