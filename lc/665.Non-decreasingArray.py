# 665. Non-decreasing Array
# Medium

# 2904

# 626

# Add to List

# Share
# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105

# This approach does not work:
#         count = 0
#         for i in range(2, len(nums)):
#             if nums[i-1] > nums[i]:
#                 if nums[i-2] > nums[i-1]:
#                     return False
#                 else:
#                     count += 1
#                     if nums[i] < nums[i-1]:
#                         nums[i-1] = nums[i]
#                     else:
#                         nums[i] = nums[i-1]
#             elif nums[i-2] > nums[i-1]:
#                 count += 1
#                 nums[i-1] = nums[i-2]
                
#         return count <= 1

# This solution works:

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        '''
        look not only at the prev but also prev prev
        '''
        prevprev = prev = float('-inf')
        changed = False
        for num in nums:
            if prev <= num:
                prevprev, prev = prev, num
                continue
            if changed:
                return False
            changed = True
            # 2, 4, 3, 3
            if prevprev <= num: # if prevprev (2) <= num (3), we can bring down prev to num (4->3)
                prev = num
            # 4, 4, 3, 4
            else: # if prevprev (4) > num (3), we are forced to bring num up to prev (3->4)
                pass # same as doing prev = prev
        return True

             