# 923. 3Sum With Multiplicity
# Medium

# 631

# 116

# Add to List

# Share
# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 109 + 7.



# Example 1:

# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:

# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.


# Constraints:

# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300


# This approach does not work:

# class Solution:
#     MOD = 10 ** 9 + 7
#     def threeSumMulti(self, arr: List[int], target: int) -> int:
#         ans = 0
        
#         counts = {}
#         for num in arr:
#             if num not in counts:
#                 counts[num] = 0
#             counts[num] += 1
        
#         arr = list(counts.items())
#         for num1, count1 in arr:
#             for num2, count2 in arr:
#                 if num1 not in counts:
#                     continue
#                 if num2 not in counts:
#                     continue
#                 num3 = -num1 -num2 +target
#                 if num3 not in counts:
#                     continue
#                 count3 = counts[num3]
#                 if num1 == num2 == num3:
#                     if count1 < 3:
#                         continue
#                     else:
#                         ans += math.comb(count1, 3)
#                         del counts[num1]
#                 elif num1 == num2:
#                     if count1 < 2:
#                         continue
#                     else:
#                         ans += math.comb(count1, 2) + math.comb(count3, 1)
#                         del counts[num1]
#                         del counts[num3]
#                 elif num2 == num3:
#                     if count2 < 2:
#                         continue
#                     else:
#                         ans += math.comb(count2, 2) + math.comb(count1, 1)
#                         del counts[num1]
#                         del counts[num2]
#                 elif num1 == num3:
#                     if count3 < 2:
#                         continue
#                     else:
#                         ans += math.comb(count3, 2) + math.comb(count2, 1)
#                         del counts[num2]
#                         del counts[num3]
#                 else:
#                     ans += math.comb(count1, 1) + math.comb(count2, 1) + math.comb(count3, 1)
#                     del counts[num1]
#                     del counts[num2]
#                     del counts[num3]
#         return ans % Solution.MOD


# This approach does not work:

# class Solution:
#     MOD = 10 ** 9 + 7
#     def threeSumMulti(self, arr: List[int], target: int) -> int:
#         ans = 0
        
#         counts = {}
#         for num in arr:
#             if num not in counts:
#                 counts[num] = 0
#             counts[num] += 1
        
#         arr = list(counts.items())
#         for num1, count1 in arr:
#             for num2, count2 in arr:
#                 if num1 not in counts:
#                     continue
#                 if num2 not in counts:
#                     continue
#                 num3 = -num1 -num2 +target
#                 if num3 not in counts:
#                     continue
#                 count3 = counts[num3]
#                 if num1 == num2 == num3:
#                     if count1 < 3:
#                         continue
#                     else:
#                         ans += math.comb(count1, 3)
#                         del counts[num1]
#                 elif num1 == num2:
#                     if count1 < 2:
#                         continue
#                     else:
#                         ans += math.comb(count1, 2) * math.comb(count3, 1)
#                         del counts[num1]
#                         del counts[num3]
#                 elif num2 == num3:
#                     if count2 < 2:
#                         continue
#                     else:
#                         ans += math.comb(count2, 2) * math.comb(count1, 1)
#                         del counts[num1]
#                         del counts[num2]
#                 elif num1 == num3:
#                     if count3 < 2:
#                         continue
#                     else:
#                         ans += math.comb(count3, 2) * math.comb(count2, 1)
#                         del counts[num2]
#                         del counts[num3]
#                 else:
#                     ans += math.comb(count1, 1) * math.comb(count2, 1) * math.comb(count3, 1)
#                     del counts[num1]
#                     del counts[num2]
#                     del counts[num3]
#         return ans % Solution.MOD


# This solution works:

from collections import Counter
class Solution:
    MOD = 10 ** 9 + 7
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        counts = Counter(arr)
        for first in range(101):
            for second in range(first, 101):
                third = target - first - second
                if third < second:
                    continue
                # below first <= second <= third only
                if first == second == third:
                    ans += math.comb(counts[first], 3)
                elif first == second:
                    ans += math.comb(counts[first], 2) * counts[third]
                elif second == third:
                    ans += math.comb(counts[second], 2) * counts[first]
                elif first == third:
                    ans += math.comb(counts[first], 2) * counts[second]
                else:
                    ans += counts[first] * counts[second] * counts[third]
        return ans % Solution.MOD