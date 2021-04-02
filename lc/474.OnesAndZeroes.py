# 474. Ones and Zeroes
# Medium

# 1599

# 279

# Add to List

# Share
# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.



# Example 1:

# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
# Example 2:

# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.


# Constraints:

# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100


# This approach does not work:

# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         arr = []
#         for elem in strs:
#             zeros = 0
#             ones = 0
#             for bit in elem:
#                 if bit == "0":
#                     zeros += 1
#                 else:
#                     ones += 1
#             arr.append((ones, zeros))
#         arr.sort(key = lambda x: (x[0]+x[1], x[0]))
#         # print(arr)
#         best = 0
#         left = 0
#         total_one = total_zero = 0
#         for right in range(len(arr)):
#             one, zero = arr[right]
#             total_one += one
#             total_zero += zero
#             # print(total_one, total_zero)
#             while left <= right and (total_one > n or total_zero > m):
#                 rm_one, rm_zero = arr[left]
#                 total_one -= rm_one
#                 total_zero -= rm_zero
#                 left += 1
#             best = max(best, right - left + 1)
#         return best
            
        
        
# This solution works - DP:

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = []
        for elem in strs:
            zeros = 0
            ones = 0
            for bit in elem:
                if bit == "0":
                    zeros += 1
                else:
                    ones += 1
            arr.append((ones, zeros))
            
        @lru_cache(None)   
        def helper(i, total_zero, total_one):
            nonlocal arr, m, n
            if i > len(arr)-1:
                if total_zero <= m and total_one <= n:
                    return 0
                else:
                    return float('-inf')
            one, zero = arr[i]
            max_length = 0
            if total_zero+zero <= m and total_one+one <= n:
                max_length = max(max_length, 1+ helper(i+1, total_zero+zero, total_one+one))
            max_length = max(max_length, helper(i+1, total_zero, total_one))
            return max_length
            
        return helper(0, 0, 0)    