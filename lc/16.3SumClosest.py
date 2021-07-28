# 16. 3Sum Closest
# Medium

# 3942

# 193

# Add to List

# Share
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

# Constraints:

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

# This solution works:

class Solution:
    '''
    target = 5
    nums = [1, 1, 2, 4]
    
    n1 = 1, n2 = 1
    n3_idx = bisect_left(nums, 5 - 1 - 1)
           = bisect_left(nums, 3)
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        counts = Counter(nums)
        keys = list(counts.keys())
        keys.sort()
        
        best_sum = float('inf')
        for n1 in keys:
            counts[n1] -= 1
            for n2 in keys:
                if not counts[n2]:
                    continue
                counts[n2] -= 1
                n3_idx = bisect_left(keys, target - n1 - n2)
                if n3_idx < len(keys):
                    n3 = keys[n3_idx]
                    if counts[n3] and abs(target-n1-n2-n3) < abs(target-best_sum):
                        best_sum = n1 + n2 + n3
                n3_idx -= 1
                if n3_idx >= 0:
                    n3 = keys[n3_idx]
                    if counts[n3] and abs(target-n1-n2-n3) < abs(target-best_sum):
                        best_sum = n1 + n2 + n3
                counts[n2] += 1
            counts[n1] += 1
        return best_sum