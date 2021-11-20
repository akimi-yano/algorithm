# 540. Single Element in a Sorted Array
# Medium

# 3653

# 95

# Add to List

# Share
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105


# This solution works:


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
         [1,2,2,3,3,4,4,8,8]
          0 1 2 3 4 5 6 7 8
                  m
                3 
          l   r
            m
              
        '''
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if mid != 0 and nums[mid] == nums[mid-1]:
                if (mid -1) %2 != 0:
                    # there
                    right = mid-2
                else:
                    # the other side
                    left = mid+1
            elif mid != len(nums)-1 and nums[mid] == nums[mid+1]:
                if (len(nums)-1 - mid+1) %2 != 0:
                    # there
                    left = mid+2
                else:
                    # the other side
                    right = mid-1
            else:
                return nums[mid]
        return nums[left]