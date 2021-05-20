# 462. Minimum Moves to Equal Array Elements II
# Medium

# 863

# 59

# Add to List

# Share
# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment or decrement an element of the array by 1.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# Example 2:

# Input: nums = [1,10,2,9]
# Output: 16
 

# Constraints:

# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


# This solution works:

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        '''
        since we are checking from left to right, smaller things get further and larger things get closer 
        add the further ones and subtract the closer ones from the total burden
        '''
        nums.sort()
        min_num = nums[0]
        best = cur_sum = sum(num - min_num for num in nums)
        
        smaller = 0
        larger = len(nums)
        prev_num = min_num
        for cur_num in nums:
            cur_sum += smaller * (cur_num - prev_num)
            cur_sum -= larger * (cur_num - prev_num)
            best = min(best, cur_sum)
            smaller += 1
            larger -= 1
            prev_num = cur_num
        return best