# 1818. Minimum Absolute Sum Difference
# Medium

# 81

# 11

# Add to List

# Share
# You are given two positive integer arrays nums1 and nums2, both of length n.

# The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

# You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

# Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

# |x| is defined as:

# x if x >= 0, or
# -x if x < 0.
 

# Example 1:

# Input: nums1 = [1,7,5], nums2 = [2,3,5]
# Output: 3
# Explanation: There are two possible optimal solutions:
# - Replace the second element with the first: [1,7,5] => [1,1,5], or
# - Replace the second element with the third: [1,7,5] => [1,5,5].
# Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.
# Example 2:

# Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
# Output: 0
# Explanation: nums1 is equal to nums2 so no replacement is needed. This will result in an 
# absolute sum difference of 0.
# Example 3:

# Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
# Output: 20
# Explanation: Replace the first element with the second: [1,10,4,4,2,7] => [10,10,4,4,2,7].
# This yields an absolute sum difference of |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
 

# Constraints:

# n == nums1.length
# n == nums2.length
# 1 <= n <= 105
# 1 <= nums1[i], nums2[i] <= 105

# This solution works:

from sortedcontainers import SortedList
class Solution:
    MOD = 10**9 + 7
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(idx):
            nonlocal nums1, nums2, s_list
            left = s_list.bisect_left(nums2[idx])
            right = s_list.bisect_right(nums2[idx])
            best_abs = abs(nums1[i] -nums2[i])
            if left < len(s_list):
                best_abs = min(best_abs, abs(s_list[left] - nums2[i]))
                if left - 1 >= 0:
                    best_abs = min(best_abs, abs(s_list[left-1] - nums2[i]))
            if right < len(s_list):
                best_abs = min(best_abs, abs(s_list[right] - nums2[i]))
                if right + 1 < len(s_list):
                    best_abs = min(best_abs, abs(s_list[right + 1] - nums2[i]))
            return best_abs
        
        s_list = SortedList(nums1)
        
        total = 0
        for i in range(len(nums1)):
            total += abs(nums1[i]-nums2[i])
        
        best = total
        for i in range(len(nums1)):
            new_total = total - abs(nums1[i]-nums2[i]) + helper(i)
            # new_total = total - abs(nums1[i]-nums2[i]) + abs(best_val(nums2[i])-nums2[i])
            best = min(best, new_total)
        return best % Solution.MOD
    
# This solution works - optimization:
'''
since I am accessing the element in the list with index, I should use a list that is sorted but not 
the sorted list - also sorted list is not necessary in this case as the order does not change 
once it is set.
'''
from sortedcontainers import SortedList
class Solution:
    MOD = 10**9 + 7
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(idx):
            nonlocal nums1, nums2, s_list
            left = bisect_left(s_list, nums2[idx])
            right = bisect_right(s_list, nums2[idx])
            best_abs = abs(nums1[i] -nums2[i])
            if left < len(s_list):
                best_abs = min(best_abs, abs(s_list[left] - nums2[i]))
                if left - 1 >= 0:
                    best_abs = min(best_abs, abs(s_list[left-1] - nums2[i]))
            if right < len(s_list):
                best_abs = min(best_abs, abs(s_list[right] - nums2[i]))
                if right + 1 < len(s_list):
                    best_abs = min(best_abs, abs(s_list[right + 1] - nums2[i]))
            return best_abs
        
        s_list = list(sorted(nums1))
        
        total = 0
        for i in range(len(nums1)):
            total += abs(nums1[i]-nums2[i])
        
        best = total
        for i in range(len(nums1)):
            new_total = total - abs(nums1[i]-nums2[i]) + helper(i)
            # new_total = total - abs(nums1[i]-nums2[i]) + abs(best_val(nums2[i])-nums2[i])
            best = min(best, new_total)
        return best % Solution.MOD
    
    
# This approach does not work:
# from sortedcontainers import SortedList
# class Solution:
#     MOD = 10**9 + 7
#     def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
#         def helper(idx):
#             nonlocal nums1, nums2, s_list
#             left = s_list.bisect_left(nums2[idx])
#             right = s_list.bisect_right(nums2[idx])
#             best_abs = abs(nums1[i] -nums2[i])
#             if left < len(s_list):
#                 best_abs = min(best_abs, abs(s_list[left] - nums2[i]))
#                 if left - 1 >= 0:
#                     best_abs = min(best_abs, abs(s_list[left-1] - nums2[i]))
#             if right < len(s_list):
#                 best_abs = min(best_abs, abs(s_list[right] - nums2[i]))
#                 if right + 1 < len(s_list):
#                     best_abs = min(best_abs, abs(s_list[right + 1] - nums2[i]))
#             return best_abs
        
#         s_list = SortedList(nums1)
        
#         total = 0
#         for i in range(len(nums1)):
#             total += abs(nums1[i]-nums2[i])
        
#         best = total
#         for i in range(len(nums1)):
#             new_total = total - abs(nums1[i]-nums2[i]) + helper(i)
#             # new_total = total - abs(nums1[i]-nums2[i]) + abs(best_val(nums2[i])-nums2[i])
#             best = min(best, new_total)
#         return best % Solution.MOD


# This approach does not work:

# from sortedcontainers import SortedList
# class Solution:
#     MOD = 10**9 + 7
#     def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
#         def best_val(val):
#             left = s_list.bisect_left(val)
#             right = s_list.bisect_right(val)
#             if left-1 < 0 and right+1 > len(s_list):
#                 return nums1[i]
#             elif left-1 < 0:
#                 if abs(s_list[right+1]-nums2[i]) < abs(nums1[i]-nums2[i]):
#                     return s_list[right+1]
#                 else:
#                     return nums1[i]
#             elif right+1 > len(nums1):
#                 if abs(s_list[right-1]-nums2[i]) < abs(nums1[i]-nums2[i]):
#                     return s_list[right-1]
#                 else:
#                     return nums1[i]
#             else:
#                 res = nums1[i]
#                 if abs(s_list[right+1]-nums2[i]) < abs(nums1[i]-nums2[i]):
#                     res = s_list[right+1]
#                 if abs(s_list[right-1]-nums2[i]) < abs(nums1[i]-nums2[i]):
#                     res = s_list[right-1]
#                 if abs(s_list[right+1]-nums2[i]) < abs(s_list[right-1]-nums2[i]):
#                     res = s_list[right+1]
#                 else:
#                     res = s_list[right-1]
#                 return res
        
#         s_list = SortedList(nums1)
        
#         total = 0
#         for i in range(len(nums1)):
#             total += abs(nums1[i]-nums2[i])
        
#         best = total
#         for i in range(len(nums1)):
#             new_total = total - abs(nums1[i]-nums2[i]) + abs(best_val(nums2[i])-nums2[i])
#             best = min(best, new_total)
#         return total % Solution.MOD

# This approach does not work:

# class Solution:
#     MOD = 10**9 + 7
#     def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
#         @lru_cache(None)
#         def helper(i, swapped):
#             if i > len(nums1)-1:
#                 return 0
#             min_diff = float('inf')
#             if not swapped:
#                 for k in range(len(nums1)):
#                     if k == i:
#                         continue
#                     min_diff = min(min_diff, abs(nums1[k] - nums2[i]) + helper(i+1, True))
#             min_diff = min(min_diff, abs(nums1[i] - nums2[i]) + helper(i+1, swapped))
#             return min_diff
        
#         ans = helper(0, False) % Solution.MOD
#         helper.cache_clear()
#         return ans 