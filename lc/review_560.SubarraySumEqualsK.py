# 560. Subarray Sum Equals K
# Medium

# 10991

# 354

# Add to List

# Share
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107


# This solution works:


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        running_sum = 0
        counts = {0:1}
        for num in nums:
            running_sum += num
            remaining = running_sum - k
            if remaining in counts:
                ans += counts[remaining]
            
            if running_sum not in counts:
                counts[running_sum] = 0
            counts[running_sum] += 1
        return ans