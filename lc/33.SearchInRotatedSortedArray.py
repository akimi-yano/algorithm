# 33. Search in Rotated Sorted Array
# Medium

# 5945

# 516

# Add to List

# Share
# You are given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4


# This solution works !!!

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1 find start index by looking for a boundery 
        2 set offet as start to do binary search
        * dont forget to mod
        * dont just use the mid to update left and right 
        - calculate it again using left and right
        '''
        # 1 find start / offset
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left+right)//2 
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
    
        offset = left
        
        # 2 binary search
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = ((left+right)//2 + offset) % len(nums)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = (left + right) // 2 + 1
            else:
                right = (left + right) // 2 - 1
        return -1

        