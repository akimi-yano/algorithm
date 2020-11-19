# 77. Combinations
# Medium

# 1830

# 75

# Add to List

# Share
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# You may return the answer in any order.

 

# Example 1:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20
# 1 <= k <= n


# This solution works !

from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1), k))

# This solution works !

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.ans = []
        def helper(i,temp):
            if len(temp) == self.k:
                self.ans.append(temp)
                return
            if i > n:
                return
            helper(i+1, temp+[i])
            helper(i+1, temp)
        
        helper(1,[])
        return self.ans