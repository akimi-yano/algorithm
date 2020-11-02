# 974. Subarray Sums Divisible by K

# https://leetcode.com/problems/subarray-sums-divisible-by-k/

# Medium

# 1194

# 86

# Add to List

# Share
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

# Example 1:

# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# Note:

# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000

# This solution works !
'''
prefix sum and modular arithmetic and counter dict
'''
from collections import Counter

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cur = 0
        counts = Counter([cur])

        ans = 0
        for num in A:
            cur = (cur + num) % K
            ans += counts[cur]
            counts[cur] += 1
        return ans