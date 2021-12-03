# 152. Maximum Product Subarray
# Medium

# 9205

# 288

# Add to List

# Share
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# It is guaranteed that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# This solution works:


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        there are only 2 patterns and 1 generic one:
        [xxxooo]
        [oooxxx]
        [oooooo] (generic one)
        '''
        best = nums[0]
        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            best = max(best, cur)
            if cur == 0:
                cur = 1
        
        cur = 1
        for k in range(len(nums)-1,-1,-1):
            cur*=nums[k]
            best = max(best,cur)
            if cur == 0:
                cur = 1
                
        return best

