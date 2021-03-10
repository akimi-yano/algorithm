# 540. Single Element in a Sorted Array
# Medium

# 2275

# 87

# Add to List

# Share
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5


# This approach does not work:

# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         l = 0
#         r = len(nums)-1
#         while l <= r:
#             m = (l+r)//2
#             if nums[m-1] < nums[m] < nums[m+1]:
#                 return nums[m]
#             elif nums[m-1] == nums[m]:
#                 if ((m-1) - l) % 2:
#                     # left is the answer
#                     r = m-2
#                 else:
#                     # right is the answer
#                     l = m+1
#             elif nums[m] == nums[m+1]:
#                 if ((m-1) - l) % 2:
#                     # left is the answer
#                     r = m-1
#                 else:
#                     # right is the answer
#                     l = m+2


# This solution works:

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l+r)//2
            
            '''
            112
            1 1 2 3 3
            '''
            if m % 2:
                if nums[m] != nums[m+1]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] == nums[m+1]:
                    l = m + 2
                else:
                    r = m
        return nums[l]