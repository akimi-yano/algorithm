# 45. Jump Game II
# Medium

# 4257

# 183

# Add to List

# Share
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 105


# This solution works !:
'''
don't include + 0 to avoid max recursion depth error!
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i):
            if i == len(nums)-1:
                return 0
            minops = float('inf')
            for jump in range(1, nums[i]+1):
                if (i+jump) <= len(nums)-1:
                    minops = min(minops, 1 + helper(i+jump))
            return minops
        return helper(0)
