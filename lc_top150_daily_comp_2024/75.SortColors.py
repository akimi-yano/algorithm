'''
75. Sort Colors
Solved
Medium
Topics
Companies
Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        for i in range(counts[0]):
            nums[i] = 0
        
        for j in range(counts[0], counts[0]+counts[1]):
            nums[j] = 1
        
        for k in range(counts[0]+counts[1], counts[0]+counts[1]+counts[2]):
            nums[k] = 2
    
# Optimization:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count zeros and ones
        ones, zeros, N = 0, 0, len(nums)
        for num in nums:
            if num == 1:
                ones += 1
            elif num == 0:
                zeros += 1
        
        for i in range(zeros):
            nums[i] = 0
        
        for j in range(zeros, zeros+ones):
            nums[j] = 1
        
        for k in range(zeros+ones, N):
            nums[k] = 2