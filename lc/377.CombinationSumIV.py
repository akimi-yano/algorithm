# 377. Combination Sum IV
# Medium

# 2154

# 248

# Add to List

# Share
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The answer is guaranteed to fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
 

# Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?




# This approach does not work - TLE:

# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         def helper(cur, i):
#             if cur == target:
#                 return [[]]
#             if cur > target or i > len(nums)-1:
#                 return []
#             ans = []
#             ans.extend([nums[i]] + temp for temp in helper(cur+nums[i], i))
#             ans.extend(temp for temp in helper(cur, i+1))
#             return ans
        
#         arr = helper(0, 0) 
#         res = 0
#         for unique in arr:
#             counts = Counter(unique)
#             mult = 1
#             for v in counts.values():
#                 mult *= math.perm(v)
#             res += math.perm(len(unique)) // mult
#         return res


# This solution works:
'''
DP - recursion with lru cache works but not the memo
'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def helper(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            counts = 0
            for num in nums:
                counts += helper(n-num)
            return counts
        
        return helper(target) 
        