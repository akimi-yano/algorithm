# 416. Partition Equal Subset Sum
# Medium

# 6017

# 101

# Add to List

# Share
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100


# This solution works:


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        @lru_cache(None)
        def helper(i, left, right):
            if i > len(nums)-1:
                return left == right
            return helper(i+1, left + nums[i], right) or helper(i+1, left, right + nums[i])
        return helper(0, 0, 0)


# This solution works - optimization:


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        @lru_cache(None)
        def helper(i, left):
            nonlocal total
            if i > len(nums)-1:
                return left == total // 2
            return helper(i+1, left + nums[i]) or helper(i+1, left)
        return helper(0, 0)