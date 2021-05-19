# 1862. Sum of Floored Pairs
# Hard

# 132

# 16

# Add to List

# Share
# Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.

# The floor() function returns the integer part of the division.

 

# Example 1:

# Input: nums = [2,5,9]
# Output: 10
# Explanation:
# floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
# floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
# floor(5 / 2) = 2
# floor(9 / 2) = 4
# floor(9 / 5) = 1
# We calculate the floor of the division for every pair of indices in the array then sum them up.
# Example 2:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 49
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

# This solution works:

class Solution:
    MOD = 10 ** 9 + 7
    
    '''
    nums = [3, 4, 5, 6, 10]

    i = 0, num = 3
    floor_val = 1->2
    bisect_left(nums, 2 * 3, lo=0)->3
    ans += (3-0) * (2 - 1)
    
    floor_val = 2->3
    bisect_left
    
    '''
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i, num in enumerate(nums):
            floor_val = 1
            
            prev_i = bisect_left(nums, num)
            while prev_i < len(nums):
                floor_val += 1
                next_i = bisect_left(nums, floor_val * num, lo=prev_i)
                # print(next_i, prev_i, (floor_val - 1))
                ans += (next_i - prev_i) * (floor_val - 1)
                ans %= Solution.MOD
                prev_i = next_i
            
        return ans
