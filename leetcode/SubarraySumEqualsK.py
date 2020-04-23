# Subarray Sum Equals K
# Solution
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#         matched = 0
#         for start in range(len(nums)):
#             sum = 0
#             for end in range(start, len(nums)):
#                 sum += nums[end]
     
#                 if sum == k:
#                     matched+=1
#         return matched
        sum_from_first = {}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in sum_from_first:
                sum_from_first[sum].append((0, i))
            else:
                sum_from_first[sum] = [(0, i)]
        count = 0
        target = k
        for i in range(len(nums)):
            val = 0
            if i > 0:
                val = nums[i-1]
            target += val
            if target in sum_from_first:
                for start_end_tuple in sum_from_first[target]:
                    if start_end_tuple[1] >= i:
                        count += 1
            
        return count
            