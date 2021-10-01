# 698. Partition to K Equal Sum Subsets
# Medium

# 3836

# 226

# Add to List

# Share
# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2:

# Input: nums = [1,2,3,4], k = 3
# Output: false
 

# Constraints:

# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 104
# The frequency of each element is in the range [1, 4].


# This solution works:


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse = True)
        buckets = [0 for _ in range(k)]
        
        
        @lru_cache(None)
        def helper(i, buckets):
            for num in buckets:
                if num > target:
                    return False
            if i > len(nums)-1:
                return True
            buckets = list(buckets)
            for j in range(len(buckets)):
                buckets[j] += nums[i]
                if helper(i+1, tuple(sorted(buckets,reverse=True))):
                    return True
                buckets[j] -= nums[i]
            return False
        return helper(0, tuple(buckets))
        
        