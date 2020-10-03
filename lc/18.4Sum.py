# 18. 4Sum
# Medium

# 2375

# 351

# Add to List

# Share
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]



# This solution does not  work - TLEd !!!


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         def helper(arr, i):
            
#             if len(arr)==4 and sum(arr) == target:
#                 ans.add(tuple(sorted(arr)))
#                 return
#             if i  > len(nums)-1:
#                 return
    
#             temp = list(arr)
#             temp.append(nums[i])
#             helper(temp, i+1)
#             helper(arr, i+1)
        
        
#         ans = set([])
#         for i in range(len(nums)):
#             helper([], i)
        
#         return [list(elem) for elem in ans]

# This solution does not work: TLE 

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         def helper(arr, i):
            
#             if len(arr)==4 and sum(arr) == target:
#                 ans.add(tuple(arr))
#                 return
#             if i  > len(nums)-1:
#                 return
       
#             temp = list(arr)
#             temp.append(nums[i])
#             helper(temp, i+1)
#             helper(arr, i+1)
        
#         nums.sort()
#         ans = set([])
#         for i in range(len(nums)):
#             helper([], i)
        
#         return [list(elem) for elem in ans]


# This solution does not  work - TLEd:
    
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         def helper(arr, i):
            
#             if len(arr)==4 and sum(arr) == target:
#                 ans.add(tuple(arr))
#                 return
#             if i  > len(nums)-1:
#                 return
       
            
#             arr.append(nums[i])
#             helper(arr, i+1)
#             arr.pop()
#             helper(arr, i+1)
        
#         nums.sort()
#         ans = set([])
#         for i in range(len(nums)):
#             helper([], i)
        
#         return [list(elem) for elem in ans]
        