# 213. House Robber II
# Medium

# 2218

# 55

# Add to List

# Share
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [0]
# Output: 0


# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000


# This solution works !!! recursion + memorization 

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def helper(i,start):
            if (i,start) in memo:
                return memo[(i,start)]
            
            if i == len(nums)-1:
                if not start:
                    memo[(i,start)] = nums[i]
                    return nums[i]
                else:
                    memo[(i,start)] = 0
                    return 0
                
            elif i > len(nums)-1:
                memo[(i,start)] = 0
                return 0
            
            max_profit = 0
            
            if i == 0:
                max_profit = max(max_profit, nums[i] + helper(i+2, True))
                max_profit = max(max_profit, helper(i+1, start))
            else:    
                max_profit = max(max_profit, nums[i] + helper(i+2, start))
                max_profit = max(max_profit, helper(i+1, start))
            
            memo[(i,start)] = max_profit
            return max_profit
        
        return helper(0, False)
    
    
# This solution works too ! cleaner code :)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def helper(i,start):
            if (i,start) in memo:
                return memo[(i,start)]
            
            if i == len(nums)-1:
                if not start:
                    memo[(i,start)] = nums[i]
                    return nums[i]
                else:
                    memo[(i,start)] = 0
                    return 0
                
            elif i > len(nums)-1:
                memo[(i,start)] = 0
                return 0
            
            max_profit = 0
            
            max_profit = max(max_profit, nums[i] + helper(i+2, start))
            max_profit = max(max_profit, helper(i+1, start))
            
            memo[(i,start)] = max_profit
            return max_profit
        
        return max(nums[0] + helper(2, True), helper(1, False)) 