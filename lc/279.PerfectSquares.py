# 279. Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# this doesnt work because this doesnt allow go go back and check all the previous choices 
# class Solution:
#     def numSquares(self, n: int) -> int:
            
#         # perfect squares: 1^2 2^2 3^2 4^2 ... 
#         choices = []
#         for i in range(1,n+1):
#             sq = i**2
#             if sq<=n:
#                 choices.append(sq)
#         # print(choices)    
#         memo = {}
#         def helper(total,i):
#             # print(memo)
#             if total in memo:
#                 return memo[total]
#             if total == 0:
#                 return 0
#             if total <0:
#                 return float('inf')
#             if i< 0:
#                 return float('inf')
#             min_sqr = float('inf')
        
#             # use
#             min_sqr=min(min_sqr, (1 + helper(total-choices[i],i)))
            
#             # not use
#             min_sqr=min(min_sqr,(helper(total,i-1)))
            
#             memo[total]=min_sqr
#             return min_sqr

#         return helper(n,len(choices)-1)
        
        
        
        
        
        
        
# worked !!! but slow
class Solution:
    def numSquares(self, n: int) -> int:
            
        # perfect squares: 1^2 2^2 3^2 4^2 ... 
        choices = []
        for i in range(1,n+1):
            sq = i**2
            if sq<=n:
                choices.append(sq)
        # print(choices)    
        memo = {}
        def helper(total):
            # print(memo)
            if total in memo:
                return memo[total]
            if total == 0:
                return 0
            if total <0:
                return float('inf')

            min_sqr = float('inf')
            # use
            for i in range(len(choices)):
                choice = choices[i]
                if choice > total:
                    break
                min_sqr=min(min_sqr, (1 + helper(total-choice)))
            memo[total]=min_sqr
            return min_sqr

        return helper(n)
        
        
# works! optimized using class variable (much faster!)
class Solution:
    memo = {}

    def numSquares(self, n: int) -> int:
        def helper(total):
            # print(memo)
            if total in Solution.memo:
                return Solution.memo[total]
            if total == 0:
                return 0
            if total <0:
                return float('inf')

            min_sqr = float('inf')
            # use
            i = 1
            while i ** 2 <= total:
                choice = i ** 2
                min_sqr=min(min_sqr, (1 + helper(total-choice)))
                i += 1
            Solution.memo[total]=min_sqr
            return min_sqr

        return helper(n)
        
        