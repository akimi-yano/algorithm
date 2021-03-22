# 1802. Maximum Value at a Given Index in a Bounded Array
# Medium

# 105

# 23

# Add to List

# Share
# You are given three positive integers n, index and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
# Return nums[index] of the constructed array.

# Note that abs(x) equals x if x >= 0, and -x otherwise.

 

# Example 1:

# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: The arrays [1,1,2,1] and [1,2,2,1] satisfy all the conditions. There are no other valid arrays with a larger value at the given index.
# Example 2:

# Input: n = 6, index = 1,  maxSum = 10
# Output: 3
 

# Constraints:

# 1 <= n <= maxSum <= 109
# 0 <= index < n

# This solution works:

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        '''
        see 10 ** 9 ? -> BINARY SEARCH !!!! O(logN)
         1 x 1 1 1 1 maxSum - (N-1) = 10 - 5 = 5 
        [_ _ _ _ _ _] 
         0 1 2 3 4 5
           @
          max
         so max is between 1 <= max <= 5 - binary search this max value
         
          idx
         2 3 2 1 1 1
        [_ _ _ _ _ _]
         0 1 2 3 4 5
         _ _ (n-idx) - val = all the remaining 1s
         idx+1
         val - (idx+1) = the ones we need to subtract
        '''
        def helper(val):
            left_total = sumof1ton(val)
            right_total = sumof1ton(val) - val
            left_offset = right_offset = 0 
            if (index+1) < val:
                to_be_removed = val - (index+1)
                left_offset = -sumof1ton(to_be_removed)
            else:
                ones_to_be_added = (index+1) - val
                left_offset = ones_to_be_added
            if (n-index) < val:
                to_be_removed = val - (n-index)
                right_offset = -sumof1ton(to_be_removed)
            else:
                ones_to_be_added = (n-index) - val
                right_offset = ones_to_be_added
            
            return (left_total + right_total + left_offset + right_offset) <= maxSum
            
        def sumof1ton(N):
            return (N * (N+1)) // 2
            
        
        left = 1
        right = maxSum - (n-1)
        while left < right:
            mid = (left+right+1) // 2
            if helper(mid):
                left = mid
            else:
                right = mid -1
        return left