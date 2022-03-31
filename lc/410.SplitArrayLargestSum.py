# 410. Split Array Largest Sum
# Hard

# 4607

# 130

# Add to List

# Share
# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

 

# Example 1:

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
# Example 3:

# Input: nums = [1,4,4], m = 3
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= m <= min(50, nums.length)


# This solution works:


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        # binary search the answer
        
        def helper(maybe_ans):
            nonlocal m
            start = 0
            for i in range(m):
                cur_sum = 0
                cur_idx = start
                while cur_idx < len(nums) and cur_sum + nums[cur_idx] <= maybe_ans:
                    cur_sum += nums[cur_idx]
                    cur_idx += 1
                start = cur_idx
            return start == len(nums)
        
        left = 0
        right = sum(nums)
        while left < right:
            mid = (left+right)//2
            if helper(mid):
                right = mid
            else:
                left = mid+1
        return left