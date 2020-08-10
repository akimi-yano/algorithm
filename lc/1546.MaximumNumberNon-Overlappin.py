# 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
# Medium

# 139

# 4

# Add to List

# Share
# Given an array nums and an integer target.

# Return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 2
# Output: 2
# Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
# Example 2:

# Input: nums = [-1,3,5,1,4,2,-9], target = 6
# Output: 2
# Explanation: There are 3 subarrays with sum equal to 6.
# ([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
# Example 3:

# Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
# Output: 3
# Example 4:

# Input: nums = [0,0,0], target = 0
# Output: 3
 

# Constraints:

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 0 <= target <= 10^6



# this solution does not work !

# class Solution:
#     def maxNonOverlapping(self, nums: List[int], target: int) -> int:
#         start = 0
#         end = 0
#         total = 0
#         while start<len(nums):
#             print(nums[start])
#             if nums[start]==target:
#                 total+=1
            
#             elif nums[start]<target:
#                 temp = nums[start]
#                 end = start+1
#                 while temp<target and end<len(nums):
#                     temp += nums[end]
#                     end +=1
#                 if end == len(nums):
#                     end = start+1
#                 if temp == target:
#                     total+=1
#                 start=end-1
#             start+=1
#         return total


# this works ! prefix sum !

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        current_sum = 0
        prev_sums = set([current_sum])
        count = 0

        print('target: {}'.format(target))
        for i, num in enumerate(nums):
            current_sum += num
            # print("Loop {}: prev_sums: {}; current_sum: {}; current_sum - target:{}".format(i, prev_sums, current_sum, current_sum-target))
            if current_sum-target in prev_sums:
                count+=1
                prev_sums=set([])
            prev_sums.add(current_sum)
        return count