# 162. Find Peak Element
# Medium

# 2082

# 2262

# Add to List

# Share
# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.
# Follow up: Your solution should be in logarithmic complexity.


# This approach does not work:

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         left = 0
#         right = len(nums)-1
#         while left <= right:
#             mid = (left+right)//2
#             if nums[left] < nums[mid] > nums[right]:
#                 return mid
#             elif nums[left] < nums[right]:
#                 right = mid -1
#             else:
#                 left = mid + 1
#         return left



# This solution works ! Time O(N) & Space: O(1):

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
                
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] >nums[i+1]:
                return i
        
        if nums[0] > nums[1]:
            return 0
        
        elif nums[len(nums)-2] < nums[len(nums)-1]:
            return len(nums)-1
        
        
        
'''
m<m+1 : there must be a peak in right
m>m+1 : there might not be a peak in right -> look left : there must be a peak in left

'''
