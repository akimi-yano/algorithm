# 1749. Maximum Absolute Sum of Any Subarray
# Medium

# 92

# 0

# Add to List

# Share
# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
 

# Example 1:

# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
# Example 2:

# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# This solution works:
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = {-1:0}
        total = 0
        for i, num in enumerate(nums):
            total += num
            prefix_sum[i] = total
        return max(prefix_sum.values()) - min(prefix_sum.values())
        
'''
find the largest difference/ change: Max - Min

Input: nums = [1,-3,2,3,-4]
Output: 5

prefix_sum = 
{
-1:0,
 0:1,
 1:-2, <-
 2:0,
 3:3,  <-
 4:-1
}

Input: nums = [2,-5,1,-4,3,-2]
Output: 8

prefix_sum =
{
-1:0,
 0:2, <-
 1:-3,
 2:-2
 3:-6, <-
 4:-3
 5:-5
}
'''

