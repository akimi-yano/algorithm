# 238. Product of Array Except Self
# Medium

# 9752

# 637

# Add to List

# Share
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


# This solution works:


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,    2,     3,    4]
        2*3*4  1*3*4  1*2*4 1*2*3
        24     12     8     6
        
        [24,12,8,6]
        
        '''
        @lru_cache(None)
        def helper_left(i):
            if i < 0:
                return 1
            return nums[i] * helper_left(i-1)
        
        @lru_cache(None)
        def helper_right(i):
            if i > len(nums)-1:
                return 1
            return nums[i] * helper_right(i+1)
        
        ans = []
        for i in range(len(nums)):
            ans.append(helper_left(i-1)*helper_right(i+1))
        return ans