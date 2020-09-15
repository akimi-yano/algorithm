# 198. House Robber
# Easy

# 5432

# 164

# Add to List

# Share
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400


# THIS WORKS !

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def helper(i):
            if i in memo:
                return memo[i]
            
            if i>len(nums)-1:
                return 0
            
            max_prof = 0
            
            # used
            max_prof = max(max_prof, nums[i] + helper(i+2))
            
            # not used
            max_prof = max(max_prof, helper(i+1))
            
            memo[i] = max_prof
            return max_prof
        
        return helper(0)
    
    
    
# Solution coded 5 months ago !

class Solution:
    def __init__(self):
        self.memo = {}
        
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0]>nums[1]:
                return nums[0]
            else:
                return nums[1]
        if tuple(nums[2:]) not in self.memo:
            self.memo[tuple(nums[2:])]=self.rob(nums[2:])
        choice_a = nums[0] + self.memo[tuple(nums[2:])]
        
        if tuple(nums[1:]) not in self.memo:
            self.memo[tuple(nums[1:])]=self.rob(nums[1:])
        choice_b = self.memo[tuple(nums[1:])]
        if choice_a>choice_b:
            return choice_a
        else:
            return choice_b
        
# Tabulation approach
def rob(nums):
    tookprev = 0
    didnttakeprev = 0
    for num in nums:
        tookprev, didnttakeprev = didnttakeprev + num, max(tookprev, didnttakeprev)
    return max(tookprev, didnttakeprev)
