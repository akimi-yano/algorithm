# 34. Find First and Last Position of Element in Sorted Array
# Medium

# 5510

# 209

# Add to List

# Share
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

# This solution works:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1
        found = False
        for i, num in enumerate(nums):
            if num == target:
                if found == False:
                    start = end = i 
                    found = True
                else:
                    end = i
        return [start, end]

# This solution works - binary search:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(val):
            left = 0
            # right should start from len(nums)
            right = len(nums)
            while left < right:
                mid = (left+right)//2
                if nums[mid] >= val:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        ans = [helper(target), helper(target+1)-1]
        if ans[0] > len(nums)-1 or ans[0] < 0 or nums[ans[0]] != target:
            return [-1,-1]
        return ans
        
        
        