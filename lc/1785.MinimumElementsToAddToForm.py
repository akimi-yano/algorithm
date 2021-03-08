# 1785. Minimum Elements to Add to Form a Given Sum
# Medium

# 50

# 46

# Add to List

# Share
# You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.

# Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.

# Note that abs(x) equals x if x >= 0, and -x otherwise.

 

# Example 1:

# Input: nums = [1,-1,1], limit = 3, goal = -4
# Output: 2
# Explanation: You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.
# Example 2:

# Input: nums = [1,-10,9,1], limit = 100, goal = 0
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= limit <= 106
# -limit <= nums[i] <= limit
# -109 <= goal <= 109

# This solution works:
import math
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        cur = sum(nums)
        abs_diff = abs(goal-cur)
        return math.ceil(abs_diff / limit)




# These approaches below do not work - TLE:

#         ans = 0
#         while cur != goal:
#             if cur > goal:
#                 for num in range(limit, 0):
#                     if (cur-num) >= goal:
#                         cur -= num
#                         ans += 1
#                     else:
#                         break
#             elif cur < goal:
#                 for num in range(limit, 0):
#                     if (cur+num) <= goal:
#                         cur += num
#                         ans += 1
#                     else:
#                         break

#         return ans

        # while abs_diff:
        #     if (abs_diff - limit) >= 0:
        #         abs_diff -= limit
        #         ans += 1
        #     else:
        #         limit -= 1
        # return ans