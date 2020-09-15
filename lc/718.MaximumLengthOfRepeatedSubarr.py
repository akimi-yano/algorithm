# 718. Maximum Length of Repeated Subarray
# Medium

# 1447

# 49

# Add to List

# Share
# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

# Example 1:

# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
 

# Note:

# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100


# # This solution does not work :
# class Solution:
#     def findLength(self, A: List[int], B: List[int]) -> int:
        
#         max_length = 0
#         idxa = 0 
#         while idxa < len(A):
#             length = 0
#             idxb = 0
#             while idxb < len(B) and B[idxb]!= A[idxa]:
#                 idxb += 1
#             # same or end of array b
#             while idxb < len(B) and idxa < len(A) and B[idxb] == A[idxa]:
#                 length += 1
#                 idxa += 1
#                 idxb += 1
#             max_length = max(max_length, length)
#             idxa += 1
            
#         return max_length


# This approach does not work (TLE)
# class Solution:
#     def findLength(self, A: List[int], B: List[int]) -> int:
        
#         a = set([])
#         b = set([])
#         for i in range(len(A)):
#             for j in range(i+1,len(A)+1):
#                 a.add(tuple(A[i:j]))
                
#         for i in range(len(B)):
#             for j in range(i+1,len(B)+1):
#                  b.add(tuple(B[i:j]))
#         longest = 0
#         for elem in a:
#             if elem in b:
#                 longest = max(longest, len(elem))
#         return longest


# This approach works !!! Binary Search for size !!! 
# longest ... and shortest ... problem tends to have binary search solution 
# idea: if size 10 is valid then size 5 is also valid (so we dont have to look) 
# in the same way, if 12 is invalid we dont have to look at anything larger than that 

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right + 1) // 2
            if self.found(A, B, mid):
                left = mid
            else:
                right = mid - 1
        return left
    
    def found(self, A, B, size):
        aset = set([tuple(A[i:size+i]) for i in range(len(A)-size+1)])
        for i in range(len(B)-size+1):
            if tuple(B[i:size+i]) in aset:
                return True
            
# More readable ver without list comprehension :) 
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right + 1) // 2
            if self.found(A, B, mid):
                left = mid
            else:
                right = mid - 1
        return left
    
    
    # Its basically like a window that I am checking each time 
    def found(self, A, B, size):
        a_set = set([])
        for i in range(len(A)-size+1):
            subarr = tuple(A[i:size+i])
            a_set.add(subarr)
        for i in range(len(B)-size+1):
            subarr = tuple(B[i:size+i])
            if subarr in a_set:
                return True