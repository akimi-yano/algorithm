# 1798. Maximum Number of Consecutive Values You Can Make
# Medium

# 65

# 14

# Add to List

# Share
# You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. You can make some value x if you can choose some of your n coins such that their values sum up to x.

# Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.

# Note that you may have multiple coins of the same value.

 

# Example 1:

# Input: coins = [1,3]
# Output: 2
# Explanation: You can make the following values:
# - 0: take []
# - 1: take [1]
# You can make 2 consecutive integer values starting from 0.
# Example 2:

# Input: coins = [1,1,1,4]
# Output: 8
# Explanation: You can make the following values:
# - 0: take []
# - 1: take [1]
# - 2: take [1,1]
# - 3: take [1,1,1]
# - 4: take [4]
# - 5: take [4,1]
# - 6: take [4,1,1]
# - 7: take [4,1,1,1]
# You can make 8 consecutive integer values starting from 0.
# Example 3:

# Input: nums = [1,4,10,3,1]
# Output: 20
 

# Constraints:

# coins.length == n
# 1 <= n <= 4 * 104
# 1 <= coins[i] <= 4 * 104

# This solution works:

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        '''
        Input: coins = [1,1,1,4]
        Output: 8
        
        lower  upper
          0  ->  0
        upper+1 = 1 >= cur_lower_bound 1?
        then
         cur_lower_bound 1  ->  upper0+cur_lower_bound1 = 1
        
        0 -> 1
        upper+1 = 2 >= cur_lower_bound 1?
        then
         cur_lower_bound 1  ->  upper1+cur_lower_bound1 = 2
         
        0 -> 2
        upper+1 = 3 >= cur_lower_bound 1?
        then
         cur_lower_bound 1  ->  upper2+cur_lower_bound1 = 3
         
        0 -> 3
        upper+1 = 4 >= cur_lower_bound 4?
        then 
         cur_lower_bound 4  ->  upper3+cur_lower_bound4 = 7
        
        return upper7 + 1 = 8
         
        
        '''
        coins.sort()
        prev_upper_bound = 0
        for cur_lower_bound in coins:
            if prev_upper_bound +1 >= cur_lower_bound:
                prev_upper_bound += cur_lower_bound
            else:
                break
        return prev_upper_bound +1
            
        
        


# This approach does not work:

# class Solution:
#     def getMaximumConsecutive(self, coins: List[int]) -> int:
        
#         @lru_cache(None)
#         def helper(i, total):
#             if i > len(coins)-1:
#                 all_combs.add(total)
#                 return
#             helper(i+1, total+coins[i])
#             helper(i+1, total)
            
#         all_combs = set([])
#         helper(0, 0)
#         max_val = sum(coins)
#         ans = 0
 
#         for x in range(1, max_val+1):
#             if x in all_combs:
#                 ans = x
#             else:
#                 break
#         return ans +1

