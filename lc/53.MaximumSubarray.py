# 53. Maximum Subarray
# Easy

# 16135

# 757

# Add to List

# Share
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


# This solution:


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        1) keep track of the prefix sum
        2) keep track of the min prefix sum
        3) keep track of the best which is the difference between cur prefix sum and min prefix sum
        '''
        cur_prefix_sum = 0
        min_prefix_sum = 0
        best = float('-inf')
        for num in nums:
            cur_prefix_sum += num
            best = max(best, (cur_prefix_sum-min_prefix_sum))
            min_prefix_sum = min(min_prefix_sum, cur_prefix_sum)
        return best
            
