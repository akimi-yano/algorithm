'''
416. Partition Equal Subset Sum
Medium
Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)     

        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [False] * (target + 1) # the last elem is the target 
        dp[0] = True # base case as we can make 0 by not using anything

        for num in nums:
            # look back and see if we can use what we previously proved True
            for i in range(len(dp) - 1, num -1, -1): # from right to left
                if dp[i]:
                    continue
                if dp[i - num]:
                    dp[i] = True
                if dp[-1]:
                    return True
        return False