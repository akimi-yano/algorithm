# 287. Find the Duplicate Number
# Medium

# 12260

# 1370

# Add to List

# Share
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?


# This solution works:


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # print('...')
        N = len(nums) - 1
        left = 1
        right = N
        while left < right:
            mid = (left + right) // 2
            # print('Searching (left={}-{}, right={}-{})'.format(left, mid, mid+1, right))
            left_counter = 0
            right_counter = 0
            for num in nums:
                if left <= num <= mid:
                    left_counter += 1
                elif mid < num <= right:
                    right_counter += 1

            # if there are more numbers than there should be on the left side, the duplicate must be
            # on the left side
            if left_counter > (mid-left+1):
                # print('found {} numbers on left side({}-{})'.format(left_counter, left,mid))
                # 
                right = mid
            # otherwise, it must be on the right side
            else:
                # print('found {} numbers on right side({}-{})'.format(right_counter, mid+1,right))
                left = mid + 1
        return left