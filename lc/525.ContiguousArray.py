# 525. Contiguous Array
# Medium

# 4037

# 172

# Add to List

# Share
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


# This solution works:


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        keep track of the count: +1 if it is 1 and -1 if it is 0
        use dictionary to save the index of the count if it is the first time
        if it is not the first time update the best
        '''
        best = 0
        count = 0
        count_idx = {count:-1}
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in count_idx:
                best = max(best, i - count_idx[count])
            else:
                count_idx[count] = i
        return best