# 1838. Frequency of the Most Frequent Element
# Medium

# 112

# 4

# Add to List

# Share
# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# Example 2:

# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
# Example 3:

# Input: nums = [3,9,6], k = 2
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= 105


# This approach does not work:

# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         '''
#         [1,4,8,13], k = 5
#        4 3   = 3
#        8 7 4 = 11
#       13 12 9 5 = 26
      
#       {0: 0, 1: 3, 2: 7, 3: 12}
#       {0: 0, 1: 1, 2: 5, 3: 13}
          
#         '''
#         nums.sort()
#         prefix = {0:0}
#         running_sum = 0
#         for i, num in enumerate(nums[:-1]):
#             goal = nums[i+1]
#             diff = goal - num 
#             running_sum += diff * (i+1)
#             prefix[i+1] = running_sum
    
#         arr = list(sorted(prefix.items(), reverse = True))

#         for idx, cur_total in arr:
#             if cur_total <= k:
#                 return idx+1
#         return 1


# This solution works! - sort and sliding window approach:

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        Sort the input array A
        Sliding window prolem
        the key is to find out the valid condition:
        k + sum >= size * max
        which is
        k + sum >= (j - i + 1) * A[right]


        For every new element A[right] to the sliding window,
        Add it to the sum by sum += A[right].
        Check if it'a valid window by
        sum + k < nums[right] * (right - left + 1)

        If not, removing nums[left] from the window by
        sum -= nums[left] and left += 1.

        Then update the res by res = max(res, right - left + 1).

        '''
        left = 0
        nums.sort()
        for right in range(len(nums)):
            k += nums[right]
            if k < nums[right] * (right - left + 1):
                k -= nums[left]
                left += 1
        return right - left + 1