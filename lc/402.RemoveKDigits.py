# 402. Remove K Digits
# Medium

# 3085

# 133

# Add to List

# Share
# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.



# This approach does not works:

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         '''
#         -if current one is smaller than or equal to the previous one ( right side) then remove(skip and decrement the count for k)
#         -else append to arr (if arr is empty and num is 0 dont append)
#         -append the rest to the array
#         -handle the last one - append
#         -"" -> "0"
#         '''
#         arr = []
#         start = len(num)-1
#         for i in range(len(num)):
#             if i == len(num)-1:
#                 k -= 1
#             elif num[i] < num[i+1]:
#                 if arr or num[i] != '0':
#                     arr.append(num[i])
#             else:
#                 k -= 1
#             if k == 0:
#                 start = i+1
#                 break
        
#         for j in range(start, len(num)):
#             if arr or num[j] != '0':
#                 arr.append(num[j])
            
#         if not arr:
#             return "0"
#         return "".join(arr)

# This approach does not works:

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         '''
#         -if current one is smaller than or equal to the previous one ( right side) then remove(skip and decrement the count for k)
#         -else append to arr (if arr is empty and num is 0 dont append)
#         -append the rest to the array
#         -handle the last one - append
#         -"" -> "0"
#         '''
#         arr = []
#         start = len(num)-1
#         for i in range(len(num)):
#             if i == len(num)-1:
#                 k -= 1
#             elif num[i] <= num[i+1]:
#                 if arr or num[i] != '0':
#                     arr.append(num[i])
#             else:
#                 k -= 1
#             if k == 0:
#                 start = i+1
#                 break
        
#         for j in range(start, len(num)):
#             if arr or num[j] != '0':
#                 arr.append(num[j])
                
#         while k:
#             arr.pop()
#             k -= 1   
        
#         if not arr:
#             return "0"
#         return "".join(arr)


# This solution works:

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            if stack or num[i] != '0':
                stack.append(num[i])
            
        while k and stack:
            stack.pop()
            k -= 1
        
        if not stack:
            return "0"
        return "".join(stack)