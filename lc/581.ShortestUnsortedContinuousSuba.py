# 581. Shortest Unsorted Continuous Subarray
# Medium

# 3431

# 165

# Add to List

# Share
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
 

# Follow up: Can you solve it in O(n) time complexity?

# This solution works:

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        targets = list(sorted(nums))
        start = len(nums)-1
        end = 0
        for i in range(len(nums)):
            if nums[i] != targets[i]:
                start = min(start, i)
                end = max(end,i)
        if start >= end:
            return 0

        return end - start +1
   


# This solution works - optimization:

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = len(nums), len(nums)-1
        prev = float('-inf')
        for i, num in enumerate(nums):
            if num < prev:
                left = min(left, i)
                while left - 1 >= 0 and nums[left-1] > num:
                    left -= 1
                right = i
            prev = max(prev, num)
        return right - left + 1