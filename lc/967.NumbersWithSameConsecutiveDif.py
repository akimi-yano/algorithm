# 967. Numbers With Same Consecutive Differences

# Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

# Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

# You may return the answer in any order.

 

# Example 1:

# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:

# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

# Note:

# 1 <= N <= 9
# 0 <= K <= 9





# this solution does not work - missed some possible cases  ... not always uning just 2 numbers :

# class Solution:
#     def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
     
#         nums = [0,1,2,3,4,5,6,7,8,9]
#         if N<2:
#             return nums
#         temp = set([])
#         for k in range(10):
#             if (k + K) in nums:
#                 if k !=0:
#                     temp.add((k,abs(k + K))) 
#                 temp.add((abs(k + K),k)) 
#         # print(temp)
#         answer = []
#         while temp:
#             elem = temp.pop()
#             if elem[0]==0 and elem[1]==0:
#                 continue
#             num = 0
#             for i in range(N):
#                 num+=elem[i%2]
#                 if i != N-1:
#                     num*=10
#             answer.append(num)
#         return answer
            