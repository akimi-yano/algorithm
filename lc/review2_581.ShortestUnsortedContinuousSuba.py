# 581. Shortest Unsorted Continuous Subarray
# Medium

# 5267

# 207

# Add to List

# Share
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
 

# Follow up: Can you solve it in O(n) time complexity?


# This solution works:


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        Important thing is to keep track of the max value and if its smaller than than the max_val, we need  to update the end index
        '''
        monoq = []
        start = len(nums)
        end = -1
        max_val = float('-inf')
        for i, num in enumerate(nums):
            while monoq and nums[monoq[-1]] > num:   
                idx = monoq.pop()
                start = min(start, idx)
            if num < max_val:
                end = i
            max_val = max(max_val, num)
            monoq.append(i)  
            
        if start == len(nums):
            return 0
        return end - start +1