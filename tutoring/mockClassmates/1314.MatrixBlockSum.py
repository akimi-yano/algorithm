# 1314. Matrix Block Sum


# Given a m * n matrix mat and an integer K, 
# return a matrix answer where each answer[i][j] is the sum of all 
# elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, 
# and (r, c) is a valid position in the matrix.
 

# Example 1:

# Input: mat = 
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]], K = 1

# Output: 
# [[12,21,16],
#  [27,45,33],
#  [24,39,28]]

# i - K <= r <= i + K
# j - K <= c <= j + K

# i = 0 
# j = 0 
# mat[i][j]=1
# K = 1
# 0-1<=r<=0+1
# -1<=r<=1
# -1<=c<=1
# r - > -1,0,1 -> 0, 1 are only valid
# c - > -1,0,1 -> 0, 1 are only valid
# mat[r][c] 
# (0,0),(0,1),(1,0),(1,1)
# 1      2     4    5       = 12 


# i = 2
# j = 2
# 1<=r<=3
# 1<=c<=3
# r => 1,2,3 -> only 1,2 are valid
# c => 1,2,3 -> only 1,2 are valid
# (1,1)(1,2)(2,1)(2,2)
# 5     6   8   9 
# 11 17 -> 28 

# Example 2:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100

# from itertools import accumulate as acc

# class Solution:
#     def matrixBlockSum(self, A, K):
#         m, n = len(A), len(A[0])
#         ps = [*zip(*map(acc, zip(*map(acc, A))))]
#         def s(i, j):
#             return i >= 0 <= j and ps[min(i, m-1)][min(j, n-1)]
#         return [[s(i+K, j+K) - s(i-K-1, j+K) - s(i+K, j-K-1) + s(i-K-1, j-K-1)
#                  for j in range(n)] for i in range(m)]
