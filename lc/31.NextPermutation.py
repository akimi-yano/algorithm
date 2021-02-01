# 31. Next Permutation
# Medium

# 4833

# 1685

# Add to List

# Share
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:

# Input: nums = [1]
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


# This approach does not  work
# from itertools import permutations
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         arr = list(permutations(nums, len(nums)))
#         prev = None
#         find_next = False
#         target = arr[0]
        
#         for i in range(len(arr)):
#             if arr[i] == prev:
#                 continue
#             if find_next:
#                 target = arr[i]
#                 break
#             if nums == list(arr[i]):
#                 find_next = True
#                 break
#             prev = arr[i]
        
#         for k in range(len(nums)):
#             nums[k] = target[k]

# This solution works:
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                for num in range(nums[i]+1, 100+1):
                    for k in range(len(nums)-1, -1, -1):
                        if i > k:
                            break
                        if nums[k] == num:
                            nums[i], nums[k] = nums[k], nums[i]
                            left = i+1
                            right = len(nums)-1
                            while left < right:
                                nums[left], nums[right] =  nums[right], nums[left]
                                left += 1
                                right -= 1
                            return
        nums.reverse()
        return

# This solution works - optimization:
    class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                for k in range(len(nums)-1, -1, -1):
                    if nums[k] > nums[i]:
                        nums[i], nums[k] = nums[k], nums[i]
                        left = i+1
                        right = len(nums)-1
                        while left < right:
                            nums[left], nums[right] =  nums[right], nums[left]
                            left += 1
                            right -= 1
                        return
        nums.reverse()
        return
    
'''
iterate through the nums array from right to left and find any increasing sequence
iterate from right to left and if I find any number greater than the element from first loop nums[i]
then swap with it and reverse everything from i+i to the end
and return it

otherwise just reverse and return

ex)
13221
just finding the first element from right which is larger than the element to swap
as the right side of the element is guatanteed to have an element larger than the element to swap
also in the case of dups, just find the first larger element and reverse will work
'''