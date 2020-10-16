# 189. Rotate Array
# Medium

# 3555

# 870

# Add to List

# Share
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


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

# 1 <= nums.length <= 2 * 104
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105



# This solution works !!!!!

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        moves_left = N
        
        start_idx = 0
        while moves_left:
            next_idx = (start_idx + k) % N
            temp = nums[start_idx]
            while next_idx != start_idx:
                temp, nums[next_idx] = nums[next_idx], temp
                next_idx = (next_idx + k) % N
                moves_left -= 1
            # need to do one more update
            nums[next_idx] = temp
            
            # in the next loop, start at the next index
            start_idx += 1
            moves_left -= 1
            
            
            
# Another solution 

    
# Classical 3-step array rotation:
#   1 reverse the first n - k elements
#   2 reverse the rest of them
#   3 reverse the entire array

    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1