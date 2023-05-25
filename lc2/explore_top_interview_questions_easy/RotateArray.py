'''
189. Rotate Array
Medium
14.2K
1.6K
Companies
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        nums = [1,2,3,4,5,6,7], k = 3
        7 elems
        k=0 [1,2,3,4,5,6,7]
                         i=i-1
        k=1 [7,1,2,3,4,5,6]
        k=2 [6,7,1,2,3,4,5]
        k=3 [5,6,7,1,2,3,4]
        k=4 [4,5,6,7,1,2,3]
        k=5 [3,4,5,6,7,1,2]
        k=6 [2,3,4,5,6,7,1]
        k=7 [1,2,3,4,5,6,7]
        '''
        n = len(nums)
        k = k%n
        temp = nums[-k:] + nums[:n-k]
        for i in range(n):
            nums[i] = temp[i]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
                0 ~ n-k-1
                -------
        nums = [1,2,3,4,5,6,7], k = 3
                        -----
                        n-k ~ n-1
        k=3    [5,6,7,1,2,3,4]
        
        1) reverse 0 ~ n-k-1
        2) reverse n-k ~ n-1
        3) reverse all
        '''
        n = len(nums)
        k = k % n
        # end is inclusive
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n-k-1)
        reverse(n-k, n-1)
        reverse(0, n-1)