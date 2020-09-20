# 1590. Make Sum Divisible by P
# Medium

# 41

# 1

# Add to List

# Share
# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array.

 

# Example 1:

# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
# Example 2:

# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
# Example 3:

# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
# Example 4:

# Input: nums = [1,2,3], p = 7
# Output: -1
# Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
# Example 5:

# Input: nums = [1000000000,1000000000,1000000000], p = 3
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= p <= 109


# This solution does not work:

# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
#         '''
#         ( total - sub arr sum ) % p == 0
        
#         make all kinds of sub arr and try this
#         '''
#         total = sum(nums)
#         if total % p == 0:
#             return 0
#         for num in nums:
#             if (total - num) %  p == 0:
#                 return 1
#         prefix = {}
#         temp = 0
#         for i in range(len(nums)):
#             temp += nums[i]
#             prefix[temp] = i
#         # print(prefix)
#         candi = []
#         for k, v in  prefix.items():
#             if k % p == 0:
#                 candi.append(v)
#         if candi:
#             return len(prefix)-1 - candi[-1]
#         return -1


# This solution works : !!
'''
classic combination of 1 prefix sum 2 three sum 3 modulo !!!
'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        '''
        three sum: a + b = c -> b = c - a
        cur_prefix - prev_prefix = to_remove
        cur_prefix - to_remove = prev_prefix
        '''
        to_remove = sum(nums) % p
        if to_remove < 1:
            return 0
        # print("want to remove ", to_remove)

        best = float('inf')
        prefix = 0
        prefixes = {0: -1}
        # print("prefix sum at index {}: {}".format(-1, 0))
        for i, num in enumerate(nums):
            prefix += num
            prefix %= p
            # print("prefix sum at index {}: {}".format(i, prefix))
            key = (prefix - to_remove) % p
            if key in prefixes:
                start_i = prefixes[key]
                # print("  found subarray: index {} to index {}".format(start_i, i))
                best = min(best, i-start_i)
            prefixes[prefix] = i
        return best if best < len(nums) else -1