'''
283. Move Zeroes
Easy
13.7K
347
Companies
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Input: nums = [0,1,0,3,12]
                       z n 
                       [1,0,0,3,12]
                          z   n
                       [1,3,0,0,12]   
                            z   n
                       [1,3,12,0,0]
                               z
        
        Output: [1,3,12,0,0]
        '''
        z = n = 0
        while z < len(nums) and n < len(nums):
            if nums[z] != 0:
                z += 1
            elif nums[n] == 0:
                n += 1
            elif z < n:
                nums[z], nums[n] = nums[n], nums[z]
            else:
                n += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_idx = 0
        for read_idx in range(len(nums)):
            if nums[read_idx] != 0:
                nums[write_idx] = nums[read_idx]
                write_idx += 1
        
        for i in range(write_idx, len(nums)):
            nums[i] = 0