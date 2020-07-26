# 154. Find Minimum in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:

# Input: [1,3,5]
# Output: 1
# Example 2:

# Input: [2,2,2,0,1]
# Output: 0
# Note:

# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?

# this solution does not work - the solution that works is at the bottom
# class Solution:
#     def findMin(self, arr: List[int]) -> int:
        # find a position where arr[i]<arr[i+1]<[i-1] or the end or beginning of the arr
        
        # left,right = 0,len(arr)-1
        # while left<right:
        #     mid = (left+right)//2
        #     print(arr[mid])
        #     if (mid == 0 and arr[mid]<arr[mid+1]) or (mid == len(arr)-1 and arr[mid]<arr[mid-1]) or (arr[mid]<arr[mid+1]<arr[mid-1]):
        #         return arr[mid]
        #     elif arr[mid]>arr[mid-1]:
        #         left = mid+1
        #     elif arr[mid+1]>arr[mid]:
        #         right = mid-1             
        # return arr[left]
        
        
# These solutions work - explanation
        
# Find Minimum in Rotated Sorted Array I----no duplicate ----O(logN)

# class Solution(object):
# def findMin(self, nums):
#     lo, hi = 0, len(nums) - 1
#     while lo < hi:
#         mid = lo + (hi -lo) // 2
#         if nums[mid] > nums[hi]:
#             lo = mid + 1
#         else:
#             hi = mid
#     return nums[lo] 
# Find Minimum in Rotated Sorted Array II----contain duplicates----O(logN)~O(N)

# class Solution(object):
#     def findMin(self, nums):
#         lo, hi = 0, len(nums) - 1
#         while lo < hi:
#             mid = lo + (hi -lo) // 2
#             if nums[mid] > nums[hi]:
#                 lo = mid + 1
#             else:
#                 hi = mid if nums[hi] != nums[mid] else hi - 1
#         return nums[lo]





# this solution works !!!! yay

from collections import deque

class Solution(object):
    def findMin(self, nums):
        queue = deque([(0, len(nums)-1)])
        smallest = float('inf')
        while len(queue) > 0:
            left, right = queue.popleft()
            if right < left:
                continue
            mid = (left+right) // 2
            smallest = min(smallest, nums[left], nums[mid], nums[right])
            # if mid was smaller than or equal to left, the "drop" could
            # be in here somewhere.
            if nums[left] >= nums[mid]:
                queue.append((left+1, mid-1))
            if nums[mid] >= nums[right]:
                queue.append((mid+1, right-1))
        return smallest