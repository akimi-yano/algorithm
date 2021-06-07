# 128. Longest Consecutive Sequence
# Medium

# 5632

# 271

# Add to List

# Share
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# This solution works:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        all_nums = set(nums)
        @lru_cache(None)
        def helper(n):
            if n not in all_nums:
                return 0
            return 1 + helper(n+1)
            
        return max(helper(num) for num in all_nums)