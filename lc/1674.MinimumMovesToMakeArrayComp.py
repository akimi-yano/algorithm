# 1674. Minimum Moves to Make Array Complementary
# Medium

# 37

# 14

# Add to List

# Share
# You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

# The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

# Return the minimum number of moves required to make nums complementary.

 

# Example 1:

# Input: nums = [1,2,4,3], limit = 4
# Output: 1
# Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
# Example 2:

# Input: nums = [1,2,2,1], limit = 2
# Output: 2
# Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
# Example 3:

# Input: nums = [1,2,1,2], limit = 2
# Output: 0
# Explanation: nums is already complementary.
 

# Constraints:

# n == nums.length
# 2 <= n <= 105
# 1 <= nums[i] <= limit <= 105
# n is even.


# This approach does not work

# class Solution:
#     def minMoves(self, nums: List[int], limit: int) -> int:
        
#         swap_options = set([j for j in range(1, limit+1)])
        
#         def helper(i):
#             if checker():
#                 return 0
#             if i > len(nums)-1:
#                 return float('inf')
#             min_steps = float('inf')
#             original_val = nums[i]
#             for new_elem in swap_options:
#                 nums[i] = new_elem
#                 min_steps = min(min_steps, 1 + helper(i+1))
#                 nums[i] = original_val
#             return min_steps
        
#         def checker():
#             value = None
#             for i in range(len(nums)//2):
#                 if not value:
#                     value = nums[i]+nums[len(nums)-1-i]
#                 else:
#                     if value != nums[i]+nums[len(nums)-1-i]:
#                         return False
#             return True
        
#         return helper(0)



# This solution works!

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        # Sweep Line algorithm !
        # If we want to make the nums complementary, having all the pairs A = nums[i], B = nums[n - 1 - i] with A + B = T.               # Considering a pair A = nums[i], B = nums[n - 1 - i], 
        # there are 5 different situation for every such pair (A, B), 
        # given different target T.

        # 1--- 2 <= T < min(A, B) + 1, we need 2 operations to make both A, B smaller
        # 2--- min(A, B) + 1 <= T < A + B, we need 1 operation to make the larger one out of A and B smaller
        # 3--- T = A + B, we need 0 operation
        # 4--- A + B < T < max(A, B) + limit, we need 1 operation to make the smaller one out of A and B larger
        # 5--- max(A, B) + limit < T <= 2 * limit, we need 2 operation to make both A, B larger
        # We calculate the boundary for each pair (A, B) and note down the corresponding operation changes as delta. 
        # delta[i] = x means we need x more operations when target T change from i - 1 to i.

        # Complexity
        # Time: O(max(n, k))
        # Space: O(k)

        delta = collections.Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # 1--- take 2 operations to make both of them the smallest possible (1 + 1)
            delta[2] += 2
            # 2--- smallest is 1 so changing the larger one to 1 and get a min by 1 move
            delta[min(a, b) + 1] -= 1
            # 3--- no change
            delta[a + b] -= 1
            # 5--- just add 1
            delta[a + b + 1] += 1
            # 4--- largest is 1 so changing the smaller one to the largest possible value (limit) by 1 move and add 1
            delta[max(a, b) + limit + 1] += 1
            
        curr = 0            
        res = float('inf')
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res   