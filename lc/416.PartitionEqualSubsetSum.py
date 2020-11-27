# 416. Partition Equal Subset Sum
# Medium

# 3508

# 77

# Add to List

# Share
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

# This approach does not work :
'''
for a case to fail:

[2,2,1,1]
the correct answer is true, but this code returns false

'''

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total%2 != 0:
#             return False
#         target = total // 2  
        
#         nums.sort()
#         left = 0
#         right = len(nums)
#         while left <= right:
#             mid = (left+right)//2
#             l, r = self.helper(mid, nums)
#             if l == r:
#                 return True
#             elif l < r:
#                 left = mid +1
#             else:
#                 right = mid -1
#         return False
    
#     def helper(self, index, nums):
#         l = sum(nums[:index])
#         r = sum(nums[index:])
#         return l, r

# This solution works !:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total // 2  
        memo = {}
        
        def helper(i, cur):
            key = (i, cur)
            if key in memo:
                return memo[key]
            ans = False
            if cur == 0:
                ans = True
            elif i > len(nums)-1:
                pass
            else:
                ans = helper(i+1, cur-nums[i]) or helper(i+1, cur) 
            memo[key] = ans
            return ans
        return helper(0, target)