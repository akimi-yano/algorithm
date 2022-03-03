# 413. Arithmetic Slices
# Medium

# 3037

# 233

# Add to List

# Share
# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
# Example 2:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000


# This solution works:


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        diff = A[1] - A[0]
        left = 0
        best = 0
        for right in range(1, len(A)):
            if A[right] - A[right-1] != diff:
                diff = A[right] - A[right-1]
                n = right -1 - left - 1
                if n >= 1:
                    best += (n * (n+1) // 2)
                left = right - 1
        n = len(A) - 1 - left - 1
        if n >= 1:
            best += (n * (n+1)) // 2
        return best