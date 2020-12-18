# 454. 4Sum II
# Medium

# 1624

# 78

# Add to List

# Share
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

# Example:

# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

# Output:
# 2

# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


# This solution works !

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # AB's patterns {total of A & B: #}
        # CD's patterns counter dict {total of C & D: #}
        AB = self.make_counter(A, B)
        CD = self.make_counter(C, D)     
        
        # a+b+c+d = 0 => c+d = -(a+b)
        count = 0
        ABlist = list(AB.items())
        for key, val in ABlist:
            if -key in CD:
                count += val * CD[-key]
                del AB[key]
                del CD[-key]
        return count
        
    def make_counter(self, arr1, arr2):
        memo = {}
        for val1 in arr1:
            for val2 in arr2:
                total = val1 + val2
                if total not in memo:
                    memo[total] = 1
                else:
                    memo[total] += 1
        return memo