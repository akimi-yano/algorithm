# 1658. Minimum Operations to Reduce X to Zero
# Medium

# 560

# 12

# Add to List

# Share
# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.



# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109

# this solution works:

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = {-1: 0}
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            prefix[i] = cur
        # get the longest length in which the sum becomes (length - x) 
        # and returns the length - longest_length
        longest_length = 0
        left = -1
        right = 0
        target = sum(nums) - x
        while right < len(nums):
            while left < right and ((prefix[right] - prefix[left]) > target):
                left += 1
            if left < right and prefix[right] - prefix[left] == target:
                longest_length = max(longest_length, (right - left ))
            right += 1
        if target != 0 and longest_length == 0:
            return -1
        return len(nums) - longest_length
    
    
# this solution works:

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        +++++++++++++++++
        ++++l
        -------r
        '''
        cur = sum(nums)
        if cur < x:
            return -1
        
        best = float('inf')
        l = r = 0
        while r < len(nums):
            if cur > x:
                cur -= nums[r]
                r += 1
            elif cur < x:
                cur += nums[l]
                l += 1
            else:
                best = min(best, (len(nums) - r) + l)
                cur -= nums[r]
                r += 1
        while cur < x:
            cur += nums[l]
            l += 1
        if cur == x:
            best = min(best, (len(nums) - r) + l)
        return best if best < float('inf') else -1