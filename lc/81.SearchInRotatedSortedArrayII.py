# 81. Search in Rotated Sorted Array II
# Medium

# 1723

# 512

# Add to List

# Share
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?


# This solution works !
'''
For the worst case, we need to check everything - so just check everything anyways 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
    
    
# This approach does not work - dont do this - just check everything

# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         # find the real start index
#         left = 0
#         right = len(nums)-1
#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] <= nums[right]:
#                 right = mid
#             else:
#                 left = mid +1 
#         real_start = left
#         l = 0
#         r = len(nums)-1
#         while l <= r:
#             mid = ((l + r + real_start) // 2) % len(nums)
#             if target == nums[mid]:
#                 return True
#             elif target < nums[mid]:
#                 l = mid + 1  
#             else:
#                 r = mid - 1 
#         return False