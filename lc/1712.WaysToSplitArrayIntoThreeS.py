# 1712. Ways to Split Array Into Three Subarrays
# Medium

# 57

# 16

# Add to List

# Share
# A split of an integer array is good if:

# The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
# The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
# Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [1,1,1]
# Output: 1
# Explanation: The only good way to split nums is [1] [1] [1].
# Example 2:

# Input: nums = [1,2,2,2,5,0]
# Output: 3
# Explanation: There are three good ways of splitting nums:
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
# Example 3:

# Input: nums = [3,2,1]
# Output: 0
# Explanation: There is no good way to split nums.
 

# Constraints:

# 3 <= nums.length <= 105
# 0 <= nums[i] <= 104

# This solution works !

'''
left mid right
O(N) solution - for each left_end_index,  find the range for possible  mid (lower_mid_end_index and upper_mid_end_index) 
and count/ calcurate how many valid options we have by ans += (upperbound - lowerbound +1)
'''

class Solution:
    MOD = (10 ** 9) + 7
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sums = {}
        total = sum(nums)
        N = len(nums)
        running_total = 0
        for i, num in enumerate(nums):
            running_total += num
            prefix_sums[i] = running_total
        
        ans = 0
        lower_mid_end_idx, upper_mid_end_idx = 0, 0
        for left_end_idx in range(N-2):
            left_sum = prefix_sums[left_end_idx]

            lower_mid_end_idx = max(left_end_idx+1, lower_mid_end_idx)
            while lower_mid_end_idx < N - 1:
                mid_sum = prefix_sums[lower_mid_end_idx] - left_sum
                if mid_sum >= left_sum:
                    break
                lower_mid_end_idx += 1
            if lower_mid_end_idx >= N - 1:
                break
            
            upper_mid_end_idx = max(upper_mid_end_idx, lower_mid_end_idx)
            while upper_mid_end_idx < N:
                right_sum = total - prefix_sums[upper_mid_end_idx]
                mid_sum = prefix_sums[upper_mid_end_idx] - left_sum
                if mid_sum > right_sum:
                    upper_mid_end_idx -= 1
                    break
                upper_mid_end_idx += 1
            upper_mid_end_idx = min(upper_mid_end_idx, N - 2)

            ans += upper_mid_end_idx - lower_mid_end_idx + 1
            ans %= Solution.MOD
        return ans
    
    
# This approach does not work:

# class Solution:
#     MOD = (10** 9) + 7
#     def waysToSplit(self, nums: List[int]) -> int:
#         left_sum = nums[0]
#         middle_num = nums[1]
#         right_sum = sum(nums[2:])
#         ans = 0
        
#         middle_s = 1
#         middle_e = 2 # exclusive
        
#         while middle_e < len(nums) + 1:
#             if left_sum <= middle_sum <= right_sum:
#                 ans += 1
#             else:
#                 middle_e -= 1
#                 break
#             right_sum -= nums[middle_e]
#             middle_sum += nums[middle_e]
#             middle_e += 1
#         while middle_s < middle_e:
#             middle_s += 1
#             if left_sum <= middle_sum <= right_sum:
#                 ans += 1
#             else:
#                 break