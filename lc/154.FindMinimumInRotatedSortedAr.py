# 154. Find Minimum in Rotated Sorted Array II
# Hard

# 2147

# 315

# Add to List

# Share
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [1,3,5]
# Output: 1
# Example 2:

# Input: nums = [2,2,2,0,1]
# Output: 0
 

# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
 

# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

 
#  This solution works:


'''
The idea is to use Binary Search, but here we can have equal numbers, so sometimes we need to find our minimum not in one half, but in two halves. Let us consider several possible cases of values start, mid and end.

nums[start] < nums[mid] < nums[end], for example 0, 10, 20. In this case we need to search only in left half, data is not shifted.
nums[mid] < nums[end] < nums[start], for example 20, 0, 10. In this case data is shifted and we need to search in left half.
nums[end] < nums[start] < nums[mid], for example 10, 20, 0. In this case data is shifted and we need to search in right half.
nums[end] = nums[mid], it this case we need to check the value of nums[start], and strictly speaking we not always need to search in two halves, but I check in both for simplicity of code.
Complexity: time complexity is O(log n) if there are no duplicates in nums. If there are duplicates, then complexity can be potentially O(n), for cases like 1,1,1,...,1,2,1,1,....1,1. Additional space complexity is O(1).
'''
class Solution:
    def findMin(self, nums):
        def bin_dfs(start, end):
            if end - start <=  1:
                self.Min = min(nums[start], nums[end], self.Min)
                return

            mid = (start + end)//2
            if nums[end] <= nums[mid]:
                bin_dfs(mid + 1, end)
            if nums[end] >= nums[mid]:
                bin_dfs(start, mid)
        
        self.Min = float("inf")
        bin_dfs(0, len(nums) - 1)
        return self.Min

