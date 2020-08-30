# 1567. Maximum Length of Subarray With Positive Product

# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

# Return the maximum length of a subarray with positive product.

 

# Example 1:

# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.
# Example 2:

# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
# Example 3:

# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
# Example 4:

# Input: nums = [-1,2]
# Output: 1
# Example 5:

# Input: nums = [1,2,3,5,-6,4,0,10]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9





# This does not work 
# class Solution:
#     def getMaxLen(self, nums: List[int]) -> int:
        # non 0 and it has to be positive 
        # 2 negatives or positives without 0
#         left = [1 for _ in range(len(nums))]
#         val = 1
#         for i in range(len(nums)):
#             left[i] = val*nums[i]
#             val *= nums[i]
            
#         print(left)
#         right = [1 for _ in range(len(nums))]
#         val = 1
#         for i in range(len(nums)-1,-1,-1):
#             right[i] = val*nums[i]
#             val *= nums[i]
#         print(right)



# This solution works !

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # check from left to right and from right to left with variables count, negatives, max_length
        # count - increment unless its 0 ; if 0 -> reset
        # negatives - if negative count is odd, dont update the max_length
        # keep getting the max_length
        
        count = 0
        negs = 0
        left_max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
                negs = 0
            elif nums[i] < 0:
                count += 1
                negs += 1
            else:
                count+=1
            if negs%2 == 0:
                left_max_length = max(left_max_length,count)
        
        count = 0
        negs = 0
        right_max_length = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                count = 0
                negs = 0
            elif nums[i] < 0:
                count += 1
                negs += 1
            else:
                count+=1
            if negs%2 == 0:
                right_max_length = max(right_max_length,count)
                    
        return max(left_max_length, right_max_length)

