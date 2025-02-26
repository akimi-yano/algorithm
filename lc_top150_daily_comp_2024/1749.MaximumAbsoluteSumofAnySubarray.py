'''
1749. Maximum Absolute Sum of Any Subarray
Medium
Topics
Companies
Hint
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        '''
        [1,-3,2,3,-4]

        1  -2 0 3 -4

        [2,-5,1,-4,3,-2]
         2 -3 -2 -6 -3 -5
        '''
        running_sum = 0
        neg_largest = 0
        pos_largest = 0
        best = 0
        for num in nums:
            running_sum += num
            if running_sum < 0:
                diff = running_sum - pos_largest
                best = max(best, abs(diff))
                neg_largest = min(neg_largest, running_sum)
            else:
                pos_largest = max(pos_largest, running_sum)
                diff = running_sum - neg_largest
                best = max(best, abs(diff))
        return best

# Simplified:

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        '''
        [1,-3,2,3,-4]

        1  -2 0 3 -4

        [2,-5,1,-4,3,-2]
         2 -3 -2 -6 -3 -5
        '''
        running_sum = 0
        max_sum = 0
        min_sum = 0
        for num in nums:
            running_sum += num
            min_sum = min(min_sum, running_sum)
            max_sum = max(max_sum, running_sum)
        return abs(max_sum-min_sum)

# Time: O(N)
# Space: O(1)