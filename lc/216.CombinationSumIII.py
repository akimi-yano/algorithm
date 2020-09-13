# 216. Combination Sum III
# Medium

# 1321

# 57

# Add to List

# Share
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Note:

# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


# OK this solution works !

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        options = [i+1 for i in range(9)]
        def helper(left, target, i, arr):
            
            # if left == 0 and target == 0: then this is one of the possible answers
            if left == 0 and target ==0:
                return [arr]
            # if target !=0: invalid
            if target <0:
                return []
            # if left !=0 then invalid
            if left<0:
                return []
            # if i < 0 then invalid
            if i<0:
                return []
                
            temp = []
            # use
            [temp.extend([ls]) for ls in helper(left-1,target-options[i],i-1,arr+[options[i]])]
            # not use
            [temp.extend([ls]) for ls in helper(left,target,i-1,arr)]
            
            return temp
        
        return helper(k, n, len(options)-1,[])
    

# THIS WORKS TOO !!!  shorter and cleaner !!!

from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        choices = [i for i in range(1, 10)]
        return [comb for comb in combinations(choices, k) if sum(comb) == n]