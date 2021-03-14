# 1793. Maximum Score of a Good Subarray
# Hard

# 40

# 3

# Add to List

# Share
# You are given an array of integers nums (0-indexed) and an integer k.

# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

# Return the maximum possible score of a good subarray.

 

# Example 1:

# Input: nums = [1,4,3,7,4,5], k = 3
# Output: 15
# Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
# Example 2:

# Input: nums = [5,5,4,5,4,1,1,1], k = 0
# Output: 20
# Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 2 * 104
# 0 <= k < nums.length

# This solution works:

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        smallest = nums[k]
        left = right = k
        best = 0
        while left > -1 and right < len(nums):
            while left > -1 and nums[left] >= smallest:
                left -= 1
            left += 1
            best = max(best, (right - left + 1) * smallest)
            while right < len(nums) and nums[right] >= smallest:
                right += 1
            right -= 1
            best = max(best, (right - left + 1) * smallest)
            if (left-1) >= 0 and (right+1) <= len(nums)-1 and nums[left-1] > nums[right+1]:
                left -= 1
                smallest = min(smallest, nums[left])
            elif (left-1) >= 0 and (right+1) <= len(nums)-1 and nums[left-1] <= nums[right+1]:
                right += 1
                smallest = min(smallest, nums[right])
            elif (left-1) >= 0:
                left -= 1
                smallest = min(smallest, nums[left])
            elif (right+1) <= len(nums)-1:
                right += 1
                smallest = min(smallest, nums[right])
            else:
                break
        return best
