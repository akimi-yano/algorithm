# 39. Combination Sum
# Medium

# 4564

# 129

# Add to List

# Share
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.



# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
# Example 4:

# Input: candidates = [1], target = 1
# Output: [[1]]
# Example 5:

# Input: candidates = [1], target = 2
# Output: [[1,1]]


# Constraints:

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500


# This solution works !!!

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(i, arr,  target):
            if sum(arr) == target:
                return [arr]
            #IMPORTANT - so that it does not hit the max recursion depth
            if sum(arr) > target:
                return []
            if i < 0:
                return []
            ans = []
            [ans.append(arr) for arr in helper(i, arr + [candidates[i]] , target)]
            [ans.append(arr) for arr in helper(i-1, arr, target)]
            return ans
        return helper(len(candidates)-1, [], target)
    
    

# This solution works ! -  small optimization - keep track of remaining total  instead of doing sum every time

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(i, arr, remaining):
            if remaining == 0:
                return [arr]
            #IMPORTANT - so that it does not hit the max recursion depth
            if 0 > remaining:
                return []
            if i < 0:
                return []
            ans = []
            [ans.append(arr) for arr in helper(i, arr + [candidates[i]] , remaining - candidates[i])]
            [ans.append(arr) for arr in helper(i-1, arr, remaining)]
            return ans
        return helper(len(candidates)-1, [], target)