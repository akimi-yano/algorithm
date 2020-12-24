# 556. Next Greater Element III
# Medium

# 963

# 246

# Add to List

# Share
# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

# Example 1:

# Input: n = 12
# Output: 21
# Example 2:

# Input: n = 21
# Output: -1
 

# Constraints:

# 1 <= n <= 231 - 1


# This approach does not work - TLE 

# from itertools import permutations
# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         arr = []
#         old_num = n
#         while n:
#             arr.append(n%10)
#             n//=10
#         options = list(permutations(arr, len(arr)))
#         options = [int("".join(str(num) for num in tup)) for tup in options]
#         options = list(set(options))
#         options.sort()
#         idx = options.index(old_num)
#         if idx + 1 <= len(options)-1 and options[idx + 1] <= 2**31 - 1:
#             return options[idx + 1]
#         return -1

# This solution works !

from itertools import permutations
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = []
        old_num = n
        while n:
            arr.append(n%10)
            n//=10
            
        best = float('inf')
        for option in permutations(arr, len(arr)):
            option_num = 0
            for digit in option:
                option_num *= 10
                option_num += digit
            if old_num < option_num < 1 << 31:
                best = min(best, option_num)
        return best if best != float('inf') else -1
    

# This solution works ! - faster - array to store the count and back tracking with recursion - break as soon as succeeding 

class Solution:
    MAX = 1 << 31
    def nextGreaterElement(self, n: int) -> int:
        arr = [0 for _ in range(10)]
        old_num = n
        while n:
            arr[n%10-1] += 1
            n//=10
        digits = sum(arr)
        def helper(cur_digit, cur_num):
            if cur_digit == digits:
                if old_num < cur_num:
                    return cur_num
                else:
                    return float('inf')
            min_num = float('inf')
            for num in range((n//(10**cur_digit))%10, 10):
                if  arr[num-1] > 0: 
                    arr[num-1] -= 1
                    min_num = min(min_num, helper(cur_digit + 1, cur_num * 10 + num))
                    if min_num < float('inf'):
                        break
                    arr[num-1] += 1
            return min_num
        ans = helper(0, 0)
        return ans if ans < Solution.MAX else -1