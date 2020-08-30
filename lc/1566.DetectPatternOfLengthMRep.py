# 1566. Detect Pattern of Length M Repeated K or More Times

# Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times.

# A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

# Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.

 

# Example 1:

# Input: arr = [1,2,4,4,4,4], m = 1, k = 3
# Output: true
# Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.
# Example 2:

# Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
# Output: true
# Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid pattern (2,1) is also repeated 2 times.
# Example 3:

# Input: arr = [1,2,1,2,1,3], m = 2, k = 3
# Output: false
# Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.
# Example 4:

# Input: arr = [1,2,3,1,2], m = 2, k = 2
# Output: false
# Explanation: Notice that the pattern (1,2) exists twice but not consecutively, so it doesn't count.
# Example 5:

# Input: arr = [2,2,2,2], m = 2, k = 3
# Output: false
# Explanation: The only pattern of length 2 is (2,2) however it's repeated only twice. Notice that we do not count overlapping repetitions.
 

# Constraints:

# 2 <= arr.length <= 100
# 1 <= arr[i] <= 100
# 1 <= m <= 100
# 2 <= k <= 100






# ALL THE FAILURES ------------------------------------------------------------------------------------

# class Solution:
#     def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
#         # use m to find a pattern and same in the variable to see if I see it in k consec times -> skip by m
#         # else reset it - keep counting
# #         pattern = arr[:m]

# #         count = 0
# #         i = 1
# #         while i <len(arr):
# #             print(arr[i:i+m],pattern)
# #             if arr[i:i+m] == pattern:
# #                 count += 2  
# # #                 print(count)
# #                 if count >= k:
# #                     return True
                
# #             else:
# #                 pattern = arr[i:i+m]
# #                 count = 0
# #             i += m
            
# #         return count >= k
        
#         # def helper(i):
#         #     if i > len(arr)-1:
#         #         return 0
#         #     count = 0 
#         #     use i
#         #     for s in range(i,len(arr)):
#         #         if arr[s:s+m] == pattern:
#         #             count += 1
#         #             helper(s+m)
#         #         else:
#         #             pattern = arr[s:s+m]
#         #             count = 0
#         #     return count
#         # return helper(0)
        
# #         def helper(i,pattern):
# #             if i > len(arr)-1:
# #                 return 0
# #             use_count = 0 
# #             not_use_count = 0
# #             # use i 
# #             if arr[i:i+m] == pattern:
# #                     use_count += 1 + helper(i+m,pattern)
    
# #             # not use i
# #             else:
# #                 not_use_count += 1 + helper(i+m,arr[i:i+m])
            
# #             return max(use_count,not_use_count)
# #         use = helper(m,arr[:m])
# #         not_use = helper(0,None)
# #         return max(use, not_use)



#         pattern = arr[:m]
#         # print(pattern)
#         count = 0
#         i = m
#         while i <len(arr):
#             print(arr[i:i+m],pattern)
#             if arr[i:i+m] == pattern:
#                 count += 1  
# #                 print(count)
#                 if count >= k:
#                     return True  
#             else:
#                 pattern = arr[i:i+m]
#                 count = 0
#             i += m +1
            
#         pattern = arr[1:1+m]
#         count = 0
#         i = 1+m+1
#         while i <len(arr):
#             # print(arr[i:i+m],pattern)
#             if arr[i:i+m] == pattern:
#                 count += 1
# #                 print(count)
#                 if count >= k:
#                     return True  
#             else:
#                 pattern = arr[i:i+m]
#                 count = 0
#             i += m +1
            
#         return count >= k


# This solution works !:

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # use m to find a pattern and same in the variable to see if I see it in k consec times -> skip by m
        # else reset it - keep counting
        for s in range(m):
            pattern = arr[s:s+m]
            count = 1
            i = s+m
            while i <len(arr):
                if arr[i:i+m] == pattern:
                    count += 1  
                    if count >= k:
                        return True  
                else:
                    pattern = arr[i:i+m]
                    count = 1
                i += m
            
        return False