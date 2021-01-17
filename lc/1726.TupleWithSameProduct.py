# 1726. Tuple with Same Product
# Medium

# 23

# 3

# Add to List

# Share
# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valids tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
# Example 3:

# Input: nums = [2,3,4,6,8,12]
# Output: 40
# Example 4:

# Input: nums = [2,3,5,7]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104
# All elements in nums are distinct.


# This solution works !

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        memo = {}
        ans = 0
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                quotient = nums[i] * nums[k]
                if quotient not in memo:
                    memo[quotient] = 0
                memo[quotient] += 1
        
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                quotient = nums[i] * nums[k]
                if quotient not in memo:
                    continue
                if memo[quotient] > 1:
                    ans += 2 * 2 * math.perm(memo[quotient], 2)
                    del memo[quotient]
        return ans
    

# This approach does not work - TLE - dont create arrays
# from itertools import permutations
# class Solution:
#     def tupleSameProduct(self, nums: List[int]) -> int:
#         arr = list(permutations(nums, 4))
#         ans = 0
#         for a, b, c, d in arr:
#             if not (a != b != c != d):
#                 continue
#             if a*b == c*d:
#                 ans += 1
#         return ans

# This solution works and much shorter - (but moving states and it might not be intuitive)
'''
building counter dictionary as you go so it does not have to unnecesarily count if its less than 1
'''
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count, ans, n = collections.Counter(), 0, len(nums)
        for i in range(n):
            for j in range(i+1, n):
                ans += 8 * count[nums[i]*nums[j]]
                count[nums[i]*nums[j]] += 1
        return ans