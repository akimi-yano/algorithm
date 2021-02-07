# 1755. Closest Subsequence Sum
# Hard

# 54

# 18

# Add to List

# Share
# You are given an integer array nums and an integer goal.

# You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

# Return the minimum possible value of abs(sum - goal).

# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

 

# Example 1:

# Input: nums = [5,-7,3,5], goal = 6
# Output: 0
# Explanation: Choose the whole array as a subsequence, with a sum of 6.
# This is equal to the goal, so the absolute difference is 0.
# Example 2:

# Input: nums = [7,-9,15,-2], goal = -5
# Output: 1
# Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
# The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
# Example 3:

# Input: nums = [1,2,3], goal = -7
# Output: 7
 

# Constraints:

# 1 <= nums.length <= 40
# -107 <= nums[i] <= 107
# -109 <= goal <= 109

# This solution works:

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        '''
        Meet in the middle ! split the array into half :)
        '''
        n1 = [nums[i] for i in range(len(nums)//2)]
        n2 = [nums[i] for i in range(len(nums)//2, len(nums))]
        
        set1 = set([])

        set2 = set([])

        def helper1(i, cur):
            if i > len(n1)-1:
                set1.add(cur)
                return
            helper1(i+1, cur + n1[i])
            helper1(i+1, cur)

        def helper2(i, cur):
            if i > len(n2)-1:
                set2.add(cur)
                return
            helper2(i+1, cur + n2[i])
            helper2(i+1, cur)
        
        helper1(0, 0)
        helper2(0, 0)
        # print(set1, set2)
        
        sorted_set2 = list(set2)
        sorted_set2.sort()

        best = abs(goal)
        right = len(sorted_set2) - 1
        for num1 in sorted(set1):
            left = 0
            while left <= right:
                mid = (left+right)//2
                num2 = sorted_set2[mid]
                
                diff = goal - (num1 + num2)
                best = min(best, abs(diff))
                
                if diff > 0:
                    left = mid + 1
                elif diff < 0:
                    right = mid - 1
                else:
                    return 0

        return best
    


# This approach does not work:

# class Solution:
#     def minAbsDifference(self, nums: List[int], goal: int) -> int:
#         def helper(i):
#             if i > len(nums)-1:
#                 return 0
#             nonlocal goal
#             num1 = nums[i]+ helper(i+1)
#             num2 = helper(i+1)
#             option1 = abs(num1 - goal)
#             option2 = abs(num2 - goal)
#             if option1 < option2:
#                 return num1
#             else:
#                 return num2
#         return abs(helper(0)-goal)


# This approach does not work:
# class Solution:
#     def minAbsDifference(self, nums: List[int], goal: int) -> int:
#         def helper(i):
#             if i > len(nums)-1:
#                 return 0
#             nonlocal goal
#             num1 = nums[i]+ helper(i+1)
#             num2 = helper(i+1)
#             option1 = abs(num1 - goal)
#             option2 = abs(num2 - goal)
#             if option1 < option2:
#                 return num1
#             else:
#                 return num2
#         return abs(helper(0)-goal)