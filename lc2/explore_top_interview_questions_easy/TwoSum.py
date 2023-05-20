'''
1. Two Sum
Easy
46.4K
1.5K
Companies
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        [2,7,11,15] 9
        memo {
        2, [0]
        7, [1]
        11, [2]
        15, [3]
        }
        
        
        [3,2,4], target = 6
        memo {
        3, [0]
        2, [1]
        4, [2]
        }
        
        nums = [3,3], target = 6
        memo {
        3, [0, 1]
        }
        '''
        memo = {}
        for i, num in enumerate(nums):
            if num not in memo:
                memo[num] = []
            memo[num].append(i) 
        
        for i, num in enumerate(nums):
            look = target-num
            if num == look:
                if len(memo[look]) >= 2:
                    return memo[look]
            else:
                if look in memo:
                    return [i, memo[look][0]]
        
'''
Another approach
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            if num in memo:
                return [memo[num], i]
            look = target-num
            memo[look] = i
            
            
        