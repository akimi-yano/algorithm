# 795. Number of Subarrays with Bounded Maximum
# Medium

# 1086

# 74

# Add to List

# Share
# We are given an array nums of positive integers, and two positive integers left and right (left <= right).

# Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

# Example:
# Input: 
# nums = [2, 1, 4, 3]
# left = 2
# right = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
# Note:

# left, right, and nums[i] will be an integer in the range [0, 109].
# The length of nums will be in the range of [1, 50000].

# This solution works:

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        '''
        [2,1,4,3]
        2
        3
        
        [2,1]
        [3]
        
        
        [1, 2, 3, 4, 5, ..., 100]
        # of subarrays: 100 + 99 + 98 + ... 1
        # formula: n(n+1)/2
        
        [2, 1]
        # in bit form:
        [1, 0]
        # idea: count total number of subarrays, then subtract the invalid ones
        
        
        [2, 1, 2, 2, 2, 1, 4, 3]
        left: 2
        right: 3
        
        [2, 1, 2, 2, 2, 1], [3]
        
        [2, 1, 2, 2, 2, 1]
        
        [1, 0, 1, 1, 1, 0]
        n = 6
        total number of subarrays: 6 * ( 6 + 1 ) // 2 = 6*7/2 = 42 / 2 = 21
        This includes subarrays like [0] and [0], which don't have a max that is within the 2->3 range
        So you want to subtract them from the total
        
        so then you would subtract:
        subarrays in [0] -> 1
        subarrays in [0] -> 1
        total - 1 - 1 = 21 - 2 = 19
        
        
        '''
        def helper(arr):
            total = len(arr) * (len(arr) + 1) // 2
            count = 0
            for bit in arr:
                if not bit: # 0, it was smaller than left
                    count += 1
                else: # 1, it was between left and right
                    total -= count * (count + 1) // 2
                    count = 0
            total -= count * (count + 1) // 2
            return total

        bitmask = []
        ans = 0
        for num in nums:
            if num <= right:
                bitmask.append(left <= num <= right)
            else:
                ans += helper(bitmask)
                bitmask = []

        ans += helper(bitmask)
        return ans
        