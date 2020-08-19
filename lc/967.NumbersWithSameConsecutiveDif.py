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


# This solution works ! recursive solution !

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # edge case: N is length 1, so just return 0-9
        if N == 1:
            return [str(i) for i in range(10)]
        elif K == 0:
            return [str(i) * N for i in range(1, 10)]
        
        ans = []
        # at each loop, set the first number
        for start_num in range(1, 10):
            # the start num has to be valid
            if start_num + K < 10 or start_num - K > -1:
                ans += self.helper(K, N, start_num)
        return ans
    
    # input:
    #     N - length of the sequence
    #     start_num - first number in the sequence
    # output:
    #     a list of sequences of length N that start with start_num
    def helper(self, K, N, start_num):
        if N == 1:
            return [str(start_num)]
        
        results = []
        if start_num + K < 10:
            next_start_num = start_num + K
            sub_results = self.helper(K, N - 1, next_start_num)
            results.extend([str(start_num) + sub for sub in sub_results])
        if start_num - K > -1:
            next_start_num = start_num - K
            sub_results = self.helper(K, N -1, next_start_num)
            results.extend([str(start_num) + sub for sub in sub_results])
        return results