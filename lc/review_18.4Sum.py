# 18. 4Sum
# Medium

# 3895

# 464

# Add to List

# Share
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


# This solution works:

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counts = defaultdict(list)
        for i, num in enumerate(nums):
            counts[num].append(i)
        
        ans = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                for k in range(len(nums)):
                    if i == k or j == k:
                        continue
                    for idx in counts[(target - (nums[i] + nums[j] + nums[k]))]:
                        if idx != i and idx != j and idx != k:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], nums[idx]])))
        return list(list(elem) for elem in ans)
                        
                    