# 15. 3Sum
# Medium

# 13736

# 1323

# Add to List

# Share
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


# This solution works:


from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set([])
        counts = Counter(nums)
        keys = list(counts)
        for i in range(len(keys)):
            num = keys[i]
            if counts[num] <= 0:
                continue
            counts[num] -= 1
            
            # it is ok to incluse i for j as we are using counter dict
            for j in range(i, len(keys)):
                num2= keys[j]
                if counts[num2] <= 0:
                    continue
                counts[num2] -= 1
                
                look = -num -num2 
                # only do the following if we meet the criteria but always backtrack
                if counts[look] > 0:
                    temp = [num, num2, look]
                    temp.sort()
                    ans.add(tuple(temp))
                
                counts[num2] += 1
            counts[num] += 1
        return [list(tup) for tup in ans]