# 90. Subsets II
# Medium

# 3167

# 120

# Add to List

# Share
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


# This solution works:

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, arr):
            if i > len(nums)-1:
                ans.add(tuple(sorted(arr)))
                return
            helper(i+1, arr+[nums[i]])
            helper(i+1, arr)
        ans = set([])
        helper(0, [])
        return [list(arr) for arr in ans]