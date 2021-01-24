# 1738. Find Kth Largest XOR Coordinate Value
# Medium

# 62

# 10

# Add to List

# Share
# You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

# The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

# Find the kth largest value (1-indexed) of all the coordinates of matrix.

 

# Example 1:

# Input: matrix = [[5,2],[1,6]], k = 1
# Output: 7
# Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
# Example 2:

# Input: matrix = [[5,2],[1,6]], k = 2
# Output: 5
# Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
# Example 3:

# Input: matrix = [[5,2],[1,6]], k = 3
# Output: 4
# Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
# Example 4:

# Input: matrix = [[5,2],[1,6]], k = 4
# Output: 0
# Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 0 <= matrix[i][j] <= 106
# 1 <= k <= m * n

# This solution works:
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix)
        N = len(matrix[0])
        arr = []
        for row in range(M):
            for col in range(N):
                prevelem = prevrow = prevcol = 0
                if row != 0:
                    prevrow = matrix[row-1][col] 
                if col != 0:
                    prevcol = matrix[row][col-1] 
                if row and col:
                    prevelem = matrix[row-1][col-1] 
                val = matrix[row][col]
                matrix[row][col] = prevrow ^ prevcol ^ val ^ prevelem
                arr.append(matrix[row][col])
        arr.sort(reverse=True)
        return arr[k-1]
    
# This approach works
# class Solution:
#     def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
#         M = len(matrix)
#         N = len(matrix[0])
#         # for row in range(M):
#         #     for col in range(N):
#         #         if row == 0:
#         #             prevrow = 0
#         #             prevelem = 0
#         #         else:
#         #             prevrow = matrix[row-1][col] 
#         #         if col == 0:
#         #             prevcol = 0
#         #             prevelem = 0
#         #         else:
#         #             prevcol = matrix[row][col-1] 
#         #         if not row and not col:
#         #             prevelem = matrix[row-1][col-1] 
#         #         val = matrix[row][col]
#         #         matrix[row][col] = prevrow ^ prevcol ^ val | prevelem
                
                
        
#         # grid = [[matrix[row][col] for col in range(N)] for row in range(M)]
#         # def helper(row, col, prev):
#         #     if not (0<=row<=M-1) or not (0<=col<=N-1):
#         #         return
#         #     grid[row][col] ^= prev ^ matrix[row][col]
#         #     helper(row+1, col, prev^ matrix[row][col])
#         #     helper(row, col+1, prev^ matrix[row][col])
#         # helper(0, 0, 0)
        
#         print(matrix)
#         # arr.sort(reverse=True)
#         # return arr[k-1]