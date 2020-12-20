# 1696. Jump Game VI
# Medium

# 76

# 9

# Add to List

# Share
# You are given a 0-indexed integer array nums and an integer k.

# You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

# You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

# Return the maximum score you can get.

 

# Example 1:

# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
# Example 2:

# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
# Example 3:

# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0
 

# Constraints:

#  1 <= nums.length, k <= 105
# -104 <= nums[i] <= 104

# This approach does not work 

# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         # can jump 1 - k
#         self.K = k
        
#         @lru_cache(None)
#         def helper(i):
#             if i == len(nums) -1:
#                 return nums[i]
#             elif i > len(nums)-1:
#                 return float('-inf')
#             max_score = float('-inf')
#             for j in range(1, self.K+1):
#                 max_score = max(max_score, helper(i+j))
#             return max_score + nums[i]
            
#         ans = helper(0)
#         helper.cache_clear()
#         return ans


# This approach does not work 

#         class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         total = best = 0
#         previ = -1
#         for i, num in enumerate(nums):
#             total += num
#             if total < 0:
#                 total = 0
#                 previ = i+1
#             else:
#                 previ = i
#             best = max(best, total)   


# This approach does not work 

# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         self.K = k
        
#         def helper(i):
#             if i in memo:
#                 return memo[i]
            
#             res = float('-inf')
#             if i == len(nums) -1:
#                 res = nums[i]
#             elif i > len(nums)-1:
#                 pass
#             else:
#                 max_score = float('-inf')
#                 for j in range(1, self.K+1):
#                     max_score = max(max_score, helper(i+j))
#                 max_score += nums[i]
#                 res = max_score
#             memo[i] = res
#             return res
            
#         memo = {}
#         ans = helper(0)
#         return ans


# This solution works !

from sortedcontainers import SortedList

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        arr = [nums[0]]
        slist = SortedList(arr)
        
        left = 0
        for right in range(1, len(nums)):
            if right - left > k:
                slist.remove(arr[left])
                left += 1
            best_prev = slist[-1]
            arr.append(best_prev + nums[right])
            slist.add(best_prev + nums[right])
        return arr[-1]