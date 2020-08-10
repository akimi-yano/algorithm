# 560. Subarray Sum Equals K

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2

# Constraints:

# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].



# this solution works but over complicating the problem - see at the bottom!

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         sum_from_first = {}
#         sum = 0
#         for i in range(len(nums)):
#             sum += nums[i]
#             if sum in sum_from_first:
#                 sum_from_first[sum].append((0, i))
#             else:
#                 sum_from_first[sum] = [(0, i)]
#         count = 0
#         target = k
#         for i in range(len(nums)):
#             val = 0
#             if i > 0:
#                 val = nums[i-1]
#             target += val
#             if target in sum_from_first:
#                 for start_end_tuple in sum_from_first[target]:
#                     if start_end_tuple[1] >= i:
#                         count += 1
#         return count
    

# solved using prefix sum!

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        prev_sum={current_sum:1}
        total=0
        for num in nums:
            current_sum+=num
            if current_sum-k in prev_sum:
                total+=prev_sum[current_sum-k] 
            if current_sum not in prev_sum:
                prev_sum[current_sum]=0
            prev_sum[current_sum]+=1
        return total