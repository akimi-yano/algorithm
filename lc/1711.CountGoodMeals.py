# 1711. Count Good Meals
# Medium

# 48

# 74

# Add to List

# Share
# A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

# You can pick any two different foods to make a good meal.

# Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

# Note that items with different indices are considered different even if they have the same deliciousness value.

 

# Example 1:

# Input: deliciousness = [1,3,5,7,9]
# Output: 4
# Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
# Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
# Example 2:

# Input: deliciousness = [1,1,1,3,3,3,7]
# Output: 15
# Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
 

# Constraints:

# 1 <= deliciousness.length <= 105
# 0 <= deliciousness[i] <= 2**20

# This solution works!!!:
'''
look at the constrains and the only options are from 2**0 to 2**20 for each number
so the max summed number is 2**20 + 2**20 = 2 * (2**20) = (2**1) * (2**20) = 2 ** 21 !!
pay attention to  constraints
'''

from collections import Counter
class Solution:
    MOD = (10 ** 9) + 7
    MAX_POW = 21
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        counts = Counter(deliciousness)
        counts_arr = list(counts.items())
      
        for num1, count1 in counts_arr:
            for power in range(Solution.MAX_POW+1):
                val = 2 ** power
                num2 = (val - num1)
                if num1 not in counts or num2 not in counts:
                    continue
                count2 = counts[num2]
                if num1 == num2:
                    ans += math.comb(count1, 2)
                else:
                    ans += count1 * count2 
            del counts[num1]
        return ans % Solution.MOD
    
    
# This approach does not work

# from collections import Counter
# from itertools import combinations
# class Solution:
#     MOD = (10 ** 9) + 7
#     def countPairs(self, deliciousness: List[int]) -> int:
#         ans = 0
#         arr = list(combinations(deliciousness, 2))
#         for x1, x2 in arr:
#             n = (x1+x2) 
#             if (n != 0) and (n & (n-1) == 0):
#                 ans += 1
#         return ans % Solution.MOD
    
#         # counts = Counter(deliciousness)
#         # counts_arr = list(counts.items())
#         # for k, v in counts_arr:
#         #     for k2, v2 in counts_arr:
#         #         if k not in counts or k2 not in counts:
#         #             continue
#         #         n = (k+k2) 
#         #         if n == 0:
#         #             continue
#         #         if n & (n-1) == 0:
#         #             if k == k2:
#         #                 ans += math.comb(v,2)
#         #             else:
#         #                 ans += v * v2 
#         #         ans = ans % Solution.MOD
#         #     del counts[k]
#         # return ans % Solution.MOD
    
# #     # [1,3,5,7,9] - |
# #     1 -  1
# #     3 - 11
# #     5 -101
# #      #  n & (n-1)
    


#     #     # [1,3,5,7,9] - |
# #     1 -  1
# #     3 - 11
# #     5 -101
# #      #  n & (n-1)




# This approach does not work


# from collections import Counter
# class Solution:
#     MOD = (10 ** 9) + 7
#     def countPairs(self, deliciousness: List[int]) -> int:
#         ans = 0
#         counts = Counter(deliciousness)
#         counts_arr = list(counts.items())
#         for i in range(len(counts_arr)):
#             for j in range(i, len(counts_arr)):
#                 k, v = counts_arr[i]
#                 k2, v2 = counts_arr[j]
#                 if k not in counts or k2 not in counts:
#                     continue
#                 n = (k+k2) 
#                 if (n != 0) and (n & (n-1) == 0):
#                     if k == k2:
#                         ans += math.comb(v,2)
#                     else:
#                         ans += v * v2 
#             del counts[k]
#         return ans % Solution.MOD


# This approach does not work

# from collections import Counter
# class Solution:
#     MOD = (10 ** 9) + 7
#     def countPairs(self, deliciousness: List[int]) -> int:
#         ans = 0
#         counts = Counter(deliciousness)
#         counts_arr = list(counts.items())
#         for i in range(len(counts_arr)):
#             for j in range(i, len(counts_arr)):
#                 k, v = counts_arr[i]
#                 k2, v2 = counts_arr[j]
#                 if k not in counts or k2 not in counts:
#                     continue
#                 n = (k+k2) 
#                 if (n != 0) and (n & (n-1) == 0):
#                     if k == k2:
#                         ans += math.comb(v,2)
#                     else:
#                         ans += v * v2 
#             del counts[k]
#         return ans % Solution.MOD
    