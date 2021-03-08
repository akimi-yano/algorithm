# 1787. Make the XOR of All Segments Equal to Zero
# Hard

# 55

# 5

# Add to List

# Share
# You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

# Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.

 

# Example 1:

# Input: nums = [1,2,0,3,0], k = 1
# Output: 3
# Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
# Example 2:

# Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
# Output: 3
# Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
# Example 3:

# Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
# Output: 3
# Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].
 

# Constraints:

# 1 <= k <= nums.length <= 2000
# ​​​​​​0 <= nums[i] < 210


# This solution works:

from collections import Counter
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        freqs = [Counter(nums[i::k]) for i in range(k)]
        # storing the number of numbers that didn't have to be changed for the given xor value
        dp = [float('-inf') for _ in range(1<<10)]
        # only dp[0] is allowed to end with a xor value 0
        dp[0] = 0
        
        for freq in freqs:
            best_prev = max(dp)
            new_dp = [best_prev for _ in  range(1 << 10)]
            for num, count in freq.items():
                for prev_num in range(1 << 10):
                    new_dp[num ^ prev_num] = max(new_dp[num ^ prev_num], count + dp[prev_num])
            dp = new_dp
        return  len(nums) - dp[0]