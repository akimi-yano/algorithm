# 932. Beautiful Array
# Medium

# 621

# 859

# Add to List

# Share
# For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

# For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

# Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

 

# Example 1:

# Input: n = 4
# Output: [2,1,4,3]
# Example 2:

# Input: n = 5
# Output: [3,1,2,5,4]
 

# Note:

# 1 <= n <= 1000

# This solution works:

class Solution:
    def beautifulArray(self, N):
        @lru_cache(None)
        def dfs(N):
            if N == 1: return (1,)
            t1 = dfs((N+1)//2)
            t2 = dfs(N//2)
            return [i*2-1 for i in t1] + [i*2 for i in t2]
        
        return dfs(N)
    
    '''
    In this problem we have n = 1000, which is too big to use dfs/backtracking, so we need to find some pattern. We need to avoid structures like i < k < j with nums[i] + nums[j] = 2 * nums[k], which means that nums[i] and nums[j] has the same parity: they are both odd or even. This lead us to the following idea: let us split all numbers into 2 groups: all odd numbers and then all even numbers.

    [ odd numbers ] [ even numbers ]

    Then if i, j, k lies in two different groups, we are OK, we will hever have forbidden pattern. Also, if we look at odd numbers, imagine n = 12, then we have [1, 3, 5, 7, 9, 11] and if we add 1 to each number and divide each number by 2 then we have [0, 1, 2, 3, 4, 5]. Note, that is linear transform: when we did this transformation, if we did not have forbidden pattern, we still do not have it! So, what we need to do is to run function recursively for odd and even numbers and concatenate them.
    
    '''