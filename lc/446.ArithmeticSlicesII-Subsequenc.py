# 446. Arithmetic Slices II - Subsequence
# Hard

# 1025

# 83

# Add to List

# Share
# Given an integer array nums, return the number of all the arithmetic subsequences of nums.

# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# The test cases are generated so that the answer fits in 32-bit integer.

 

# Example 1:

# Input: nums = [2,4,6,8,10]
# Output: 7
# Explanation: All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
# Example 2:

# Input: nums = [7,7,7,7,7]
# Output: 16
# Explanation: Any subsequence of this array is arithmetic.
 

# Constraints:

# 1  <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1


# This solution works:


'''
Let dp[i][d] denotes the number of arithmetic subsequences that ends with A[i] and its common difference is d. Then we can look at all j < i and check if we can continue subsequence ending with point j. Then difference is equal to d = A[i] - A[j] and we can update dp[i][d] += (dp[j][d] + 1). Notice, that in this way we evaluate number of all possible arithmetic subsequences with length >= 2, so we just need to subtract n(n-1)/2 from final number (be careful to evaluate sum for dp[i], after we iterate over all j).

Complexity
Time and space complexity is O(n^2) for double loop and to keep all dictionaries.
'''
class Solution:
    def numberOfArithmeticSlices(self, A):
        total, n = 0, len(A)
        dp = [Counter() for item in A]
        for i in range(n):
            for j in range(i):
                dp[i][A[i] - A[j]] += (dp[j][A[i] - A[j]] + 1)      
            total += sum(dp[i].values())
          
        return total - (n-1)*n//2  
