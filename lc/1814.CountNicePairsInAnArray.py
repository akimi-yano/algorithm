# 1814. Count Nice Pairs in an Array
# Medium

# 103

# 11

# Add to List

# Share
# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
# Example 2:

# Input: nums = [13,10,35,24,76]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109

# This solution works:

from sortedcontainers import SortedList

class Solution:
    MOD = 10 ** 9 + 7
    def countNicePairs(self, nums: List[int]) -> int:
        memo = {}
        for num in nums:
            digit = 0
            temp = num
            while temp:
                temp //=10
                digit +=1
            val = 0
            temp = num
            digit -= 1
            while temp:
                temp, mod = divmod(temp, 10)
                val += mod * 10 ** digit
                digit -=1
            memo[num] = val

        ans = 0
        slist = SortedList()
        '''
        look = 2
        [1, 3]
        bisect_left = 1
        bisect_right = 1
        
        look = 2
        [1, 2, 2, 3]
        bisect_left = 1
        bisect_right = 3
        '''
        for num in nums:
            opposite = memo[num]
            look = num - opposite
            left = slist.bisect_left(look)
            right = slist.bisect_right(look)
            ans += right - left
            slist.add(look)
        
        return ans % Solution.MOD
    
    
# This approach does not work:

# class Solution:
#     MOD = 10 ** 9 + 7
#     def countNicePairs(self, nums: List[int]) -> int:
#         memo = {}
#         for num in nums:
#             digit = 0
#             temp = num
#             while temp:
#                 temp //=10
#                 digit +=1
#             val = 0
#             temp = num
#             digit -= 1
#             while temp:
#                 temp, mod = divmod(temp, 10)
#                 val += mod * 10 ** digit
#                 digit -=1
#             memo[num] = val
#         ans = 0
#         counts = Counter(nums)
#         for num in nums:
#             if counts[num] < 1:
#                 continue
#             opposite = memo[num]
#             look = num - opposite
#             for nextnum in nums:
#                 if nextnum - memo[nextnum] == look:
#                     ans += 1
#                     counts[num] -= 1
#                     counts[nextnum] -= 1
#                     break
        
#         return ans % Solution.MOD
