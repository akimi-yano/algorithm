'''
689. Maximum Sum of 3 Non-Overlapping Subarrays
Hard
Topics
Companies
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)
'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        prefix_sum = [0]
        running_sum = 0 
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        
        @cache
        def helper(i, remaining):
            if remaining == 0:
                return 0, []
            if i > len(nums)-k:
                return float('-inf'), []
            used, used_arr = helper(i+k, remaining-1)
            used += prefix_sum[i+k] - prefix_sum[i]
            not_used, not_used_arr = helper(i+1, remaining)
            if used >= not_used:
                return used, [i] + used_arr
            else:
                return not_used, not_used_arr
            
        return helper(0, 3)[1]