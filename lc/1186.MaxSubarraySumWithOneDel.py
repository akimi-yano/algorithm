# 1186. Maximum Subarray Sum with One Deletion

# Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. 
# In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element 
# left and the sum of the remaining elements is maximum possible.

# Note that the subarray needs to be non-empty after deleting one element.

# Example 1:

# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
# Example 2:

# Input: arr = [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.
# Example 3:

# Input: arr = [-1,-1,-1,-1]
# Output: -1
# Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, 
# then get an empty subarray to make the sum equals to 0.

# Constraints:

# 1 <= arr.length <= 10^5
# -10^4 <= arr[i] <= 10^4




# This does not work :

# class Solution:
#     def maximumSum(self, arr: List[int]) -> int:
        
#         prefix_sum = {}
#         for start in range(len(arr)):
#             total = 0
#             smallest = float('inf')
#             for end in range(start,len(arr)):
#                 total+=arr[end]
#                 smallest=min(smallest,arr[end])
#                 prefix_sum[(start,end)]=(total,smallest)
#         print(prefix_sum)
        
#         # prev = 0
#         max_sum = float('-inf')
#         for i in range(len(arr)):
#             # print(prefix_sum)
#             for idx,v in prefix_sum.items():
#                 start,end = idx
#                 subtotal,smallest = v
#                 # if subtotal == 0:
#                 #     continue              
#                 # print(max_sum,subtotal,subtotal-smallest)
#                 if start!=end:
#                     max_sum = max(max_sum,subtotal,subtotal-smallest)
#                 else:
#                     max_sum = max(max_sum,subtotal)
#                 # subtotal+=arr[i]*(-1)    
#                 # prefix_sum[idx]=(subtotal,smallest)
            
          
#         return max_sum
        
# '''
#         prefix sum
        
#         -> remove or not remove -> if length is larget thatn 1 and want to remove, remove smallest 
        
#         [1,-2,0,3]
        
#         1 -1 -1 2
        
#         1,-2,0,3 = 2
#         1,0,3 = 4 <=
#         -2,0,3 =1 
#         1,-2,3 = 2
#         1,-2,0 = -1 <= 
        
        
#         brute force
        
#         [1,-2,0,3]
        
#         1
#         1,-2
#         1,-2,0
#         1,-2,0,3
        
#         prefix sum:  1 -1 -1 2
        
#         -2
#         -2,0
#         -2,0,3
        
#          -2 -2 1 (-1 each)
#         0
#         0,3
        
#         0,3 (+2 each)
        
#         3
#         3 (-0)
        
#     for each option, you can remove the smallest one or not remove one 
        
#        {(i,ps):min}
       
# '''
        
        
# This solution works:

# Inspired by the solution for Maximum Subarray Sum
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        max_ending_here = n * [arr[0]]
        for i in range(1, n):
            max_ending_here[i] = max(max_ending_here[i-1] + arr[i], arr[i])
        return max(max_ending_here)
    
# It is not difficult to get this solution:
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        max_ending_here0 = n * [arr[0]]  # no deletion
        max_ending_here1 = n * [arr[0]]  # at most 1 deletion
        for i in range(1, n):
            max_ending_here0[i] = max(max_ending_here0[i-1] + arr[i], arr[i])
            max_ending_here1[i] = max(max_ending_here1[i-1] + arr[i], arr[i])
            if i >= 2:
                max_ending_here1[i] = max(max_ending_here1[i], max_ending_here0[i-2] + arr[i])
        return max(max_ending_here1)
    
    
    
    
    
# most intuitive 

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        sum_with_removed = float('-inf')
        sum_none_removed = float('-inf')
        best = float('-inf')
        for cur in arr:
            print("\nlooking at {}".format(cur))
            print("best subarray with removal: {}".format(sum_with_removed))
            print("best subarray with no removal: {}".format(sum_none_removed))
            
            sum_with_removed = max(sum_with_removed + cur, sum_none_removed)
            sum_none_removed = max(sum_none_removed + cur, cur)
            best = max(best, sum_none_removed, sum_with_removed)
        return best
    
# after clearning up !

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        sum_with_removed = float('-inf')
        sum_none_removed = float('-inf')
        best = float('-inf')
        for cur in arr:            
            sum_with_removed = max(sum_with_removed + cur, sum_none_removed)
            sum_none_removed = max(sum_none_removed + cur, cur)
            best = max(best, sum_none_removed, sum_with_removed)
        return best