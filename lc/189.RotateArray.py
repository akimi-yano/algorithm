# 189. Rotate Array
# Medium

# 7654

# 1175

# Add to List

# Share
# Given an array, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


# This solution works:


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maps = {}
        N = len(nums)
        for i, num in enumerate(nums):
            maps[(i+k)%N] = num
        
        for i in maps:
            nums[i] = maps[i]



# This solution works:


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Classical 3-step array rotation:
        #   1 reverse the first n - k elements
        #   2 reverse the rest of them
        #   3 reverse the entire array
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -= 1
        N = len(nums)
        k = k % N
        reverse(0, N-k-1)
        reverse(N-k, N-1)
        reverse(0, N-1)