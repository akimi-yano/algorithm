# 910. Smallest Range II
# Medium

# 532

# 237

# Add to List

# Share
# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

# After this process, we have some array B.

# Return the smallest possible difference between the maximum value of B and the minimum value of B.



# Example 1:

# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
# Example 2:

# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
# Example 3:

# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]


# Note:

# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000



# This approach does not work - TLE !

# class Solution:
#     def smallestRangeII(self, A: List[int], K: int) -> int:
#         @lru_cache(None)
#         def helper(i, maxB, minB):
#             if i > len(A)-1:
#                 return maxB - minB 
#             min_diff = float('inf')            
#             # choose +K
#             min_diff = min(min_diff, helper(i+1, max(maxB, A[i] + K), min(minB, A[i] + K)))
#             # choose -K
#             min_diff = min(min_diff, helper(i+1, max(maxB, A[i] - K), min(minB, A[i] - K)))
#             return min_diff
        
#         ans = helper(0, float('-inf'), float('inf'))
#         helper.cache_clear()
#         return ans
#         # A = [1,3,6], K = 3
#         # Output: 3
        
# #         1 +3 = 4  
# #         1 -3 = -2
        
# #         3+3 = 6
# #         3-3 = 0
        
# #         6+3 = 9
# #         6-9 = -3


# This solution works !

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        # after sorted              [1,2,3,4,5,6,7,8,9,10]
        # the pattern always become [+ + + + + + - - - - ] to make it min difference
        # four important elements:   @         @ @     @   <-  beginning and end and boundry
        #             lowerbound =  MIN+K              MAX-K = upperbound         
        # we are just using MIN+K and MAX-K as lowerbound and upperbound respectively 
        # so that A[i]+K and A[i+1]-K do not go out of bound
        # find the boundry in which the diff between max and min is the smallest
        A.sort()
        MIN = A[0]
        MAX = A[-1]
        ans = MAX - MIN
        # iterate until the second to last one as we look at i+1
        for i in range(len(A)-1):
            ans = min(ans, max(MAX-K, A[i]+K) - min(MIN+K, A[i+1]-K))
        return ans