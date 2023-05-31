'''
53. Maximum Subarray
Medium
29.8K
1.3K
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        if the cur_total becomes less than 0, it is better off to not have that and start from the next one
        ok we need to have at least one element in the arr, so adding that as a condition for best_total and checking is after adding the new one 
        '''
        cur_total = 0
        best_total = nums[0]
        for num in nums:
            cur_total += num
            best_total = max(best_total, cur_total)
            if cur_total < 0:
                cur_total = 0               
        return best_total