# 1799. Maximize Score After N Operations
# Hard

# 37

# 2

# Add to List

# Share
# You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

# In the ith operation (1-indexed), you will:

# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# Return the maximum score you can receive after performing n operations.

# The function gcd(x, y) is the greatest common divisor of x and y.

 

# Example 1:

# Input: nums = [1,2]
# Output: 1
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 2)) = 1
# Example 2:

# Input: nums = [3,4,6,8]
# Output: 11
# Explanation: The optimal choice of operations is:
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
# Example 3:

# Input: nums = [1,2,3,4,5,6]
# Output: 14
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 

# Constraints:

# 1 <= n <= 7
# nums.length == 2 * n
# 1 <= nums[i] <= 106


# This solution works:

import math
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i, remaining_nums):
            if not remaining_nums:
                return 0
            N = len(remaining_nums)
            best = float('-inf')
            for first in range(N):
                for second in range(first+1, N):
                    new_remaining_nums = []
                    for idx in range(N):
                        if idx not in [first, second]:
                            new_remaining_nums.append(remaining_nums[idx])
                    new_remaining_nums = tuple(new_remaining_nums)
                    best = max(best, i * math.gcd(remaining_nums[first], remaining_nums[second]) + helper(i+1, new_remaining_nums))
            return best
        return helper(1, tuple(nums))
                
                
                

# This approach does not work:

# import math
# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
        
#         def helper(i, seen, turn):
#             if i > len(nums)-1 or i not in seen or turn > len(nums)//2:
#                 return 0
#             seen.remove(i)
#             max_val = 0
#             for j in range(i+1, len(nums)):
#                 if j not in seen:
#                     continue
#                 seen.remove(j)
#                 max_val = max(max_val, math.gcd(nums[i], nums[j]) * turn + helper(j+1, seen, turn+1))
#                 seen.add(j)
#             seen.add(i)
#             # max_val = max(max_val, helper(i+1, seen, turn))
#             return max_val
                
#         return helper(0, set([k for k in range(len(nums))]), 1)
                