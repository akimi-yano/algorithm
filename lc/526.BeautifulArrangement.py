# 526. Beautiful Arrangement
# Medium

# 977

# 178

# Add to List

# Share
# Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Given an integer n, return the number of the beautiful arrangements that you can construct.

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1, 2]:
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# The second beautiful arrangement is [2, 1]:
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 15

# This solution works - needs optimization

class Solution:
    def countArrangement(self, n: int) -> int:
        def helper(seen):
            nonlocal n
            nonlocal ways
            if len(seen) == n:
                ways += 1
                return 
            idx = len(seen) +1
            for i in range(1, n+1):
                if ((i % idx == 0) or (idx % i == 0)) and i not in seen:
                    helper(seen|set([i]))
            
        ways = 0
        helper(set([]))
        return ways
    
# This solution works - still needs optimization

class Solution:
    def countArrangement(self, n: int) -> int:
        def helper(seen):
            nonlocal n
            if len(seen) == n:
                return 1
            idx = len(seen) +1
            ways = 0
            for i in range(1, n+1):
                if ((i % idx == 0) or (idx % i == 0)) and i not in seen:
                    ways += helper(seen|set([i]))   
            return ways 
        return helper(set([]))

# This solution works - ! optimized with bitmask and cache xD

class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def helper(bitmask, idx):
            nonlocal n
            if bitmask == 0:
                return 1
            ways = 0
            for num in range(1, n+1):
                if ((num % idx == 0) or (idx % num == 0)) and (bitmask & (1 << (num-1))):
                    ways += helper((bitmask ^ (1 << (num-1))), idx+1)   
            return ways 
        return helper((1<<n)-1, 1)
    
