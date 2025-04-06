'''
368. Largest Divisible Subset
Medium
Topics
Companies
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # First of all, sort to make sure that nums[i] is always larger than nums[j]
        nums.sort()
        arrs = [[num] for num in nums]
        for i in range(len(nums)):
            # Look at all smaller numbers than nums[i] and if nums[i] is divisible by 
            # this smaller number, update the solution to apply all the numbers using nums[j] and add nums[j] as well
            # because lets say the smaller number (nums[j]) is b and
            # if a < b < c and c%b == 0 and b%a == 0 then automatically c%a ==0
            # so everything that is smaller than b which that can divide d with 0 remainder can also be the answer
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(arrs[i]) < len(arrs[j]) + 1 : # +1 is for the nums[i] which we are currently looking at
                    arrs[i] = arrs[j] + [nums[i]] # nums[i] is the largest number, drop everything we had stored at arrs[i] and update to use arrs[j]
        return max(arrs, key=len)