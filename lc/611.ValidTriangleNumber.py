# 611. Valid Triangle Number
# Medium

# 1785

# 126

# Add to List

# Share
# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

# Example 1:

# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:

# Input: nums = [4,2,3,4]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

# This solution works:

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        A triangle can be valid if the sum of 2 sides out of 3 sides is greater than the other side (for all three combinations)
        '''
        nums.sort()
        ans = 0
        for i in range(len(nums)-2):
            left = -1
            for j in range(i+1, len(nums)-1):
                left = max(left, j+1)
                right = len(nums)-1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[i]+nums[j]>nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += left-j-1
        return ans