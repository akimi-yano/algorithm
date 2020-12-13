# 312. Burst Balloons
# Hard

# 3059

# 83

# Add to List

# Share
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note:

# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:

# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
            
        
# This approach does not work 

# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         @lru_cache(None)
#         def helper(remaining):
#             if not remaining:
#                 return 0
#             max_points = 0
#             for j in remaining:
#                 left = j-1
#                 right = j+1

#                 if left <= -1:
#                     left_val = 1
#                 else:
#                     left_val = nums[left]
#                 if right >= len(remaining):
#                     right_val = 1
#                 else:
#                     right_val = nums[right]
#                 max_points = max(max_points, left_val * nums[j] * right_val + helper(tuple(remaining[:j] + remaining[j+1:])))
#             return max_points
#         return helper(tuple([i for i in range(len(nums))]))


# This solution works !

'''
keep track of left and right and choose  a middle in which the elements between left-mid + the elements between mid-right become max

use @lru_cache and .cache_clear()
'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        self.nums = [1] + nums + [1]
        ans = self.helper(0, len(self.nums)-1)
        self.helper.cache_clear()
        return ans
    
    # left and right are not inclusive
    # choose left & mid & right and delete the elems between left-mid and mid-right usign recursion
    @lru_cache(None)
    def helper(self, left, right):
        max_points = 0
        for middle in range(left+1, right):
            max_points = max(max_points, self.nums[left] * self.nums[middle] * self.nums[right] + self.helper(left, middle) + self.helper(middle, right))
        return max_points
