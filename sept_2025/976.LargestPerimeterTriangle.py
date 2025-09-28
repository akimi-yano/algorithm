'''
976. Largest Perimeter Triangle
Solved
Easy
Topics
premium lock icon
Companies
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
'''

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        perimeter：三角形の周囲

        1 Sort the nums 
        2 Try to get a triangle with 3 biggest numbers.
            If nums[n-1] < nums[n-2] + nums[n-3], we can make a triangle.
            If nums[n-1] >= nums[n-2] + nums[n-3], we cannot make any triangle with nums[n-1]
        3 repeat the step 2 
        * Do this with reversely sorted nums with (reverse=True)

        '''
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0