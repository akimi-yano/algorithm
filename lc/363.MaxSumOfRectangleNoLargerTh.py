# 363. Max Sum of Rectangle No Larger Than K
# Hard

# 1343

# 87

# Add to List

# Share
# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

# It is guaranteed that there will be a rectangle with a sum no larger than k.

 

# Example 1:


# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
# Example 2:

# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -105 <= k <= 105
 

# Follow up: What if the number of rows is much larger than the number of columns?


# This solution works:

class Solution:
    def maxSumSubmatrix(self, M, k):
        
        def countRangeSum(nums, U):
            SList, ans = [0], -float("inf")
            for s in accumulate(nums):
                idx = bisect_left(SList, s - U) 
                if idx < len(SList): ans = max(ans, s - SList[idx])        
                bisect.insort(SList, s)
            return ans
        
        m, n, ans = len(M), len(M[0]), -float("inf")
        for i, j in product(range(1, m), range(n)):
            M[i][j] += M[i-1][j]
        M = [[0]*n] + M
        for r1, r2 in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(M[r1], M[r2])]
            ans = max(ans, countRangeSum(row, k))
        return ans

