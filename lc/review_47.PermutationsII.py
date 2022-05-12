# 47. Permutations II
# Medium

# 4995

# 94

# Add to List

# Share
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10


# This solution works:


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(arr):
            if not arr:
                return [[]]
            ans = []
            for i in range(len(arr)):
                ans.extend([arr[i]] + temp for temp in helper(arr[:i]+arr[i+1:]))
            return ans
            
        return list(set(tuple(elem) for elem in helper(nums)))