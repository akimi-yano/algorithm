'''
560. Subarray Sum Equals K
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Edge case: when k = 0 -> whether you find it or not, if there is no 0 in the array, it should not increment he ans
        prefix_sum = Counter() # val - count 
        running_sum = 0
        ans = 0
        for num in nums:
            running_sum += num
            if running_sum == k:
                ans += 1
            find = running_sum - k
            ans += prefix_sum[find]
            prefix_sum[running_sum] += 1
        return ans