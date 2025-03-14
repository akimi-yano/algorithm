# 442. Find All Duplicates in an Array
# Medium

# 4505

# 209

# Add to List

# Share
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.


# This solution works:


from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        ans = []
        for num in counts:
            if counts[num] == 2:
                ans.append(num)
        return ans


# This solution works - optimization:


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for idx in nums:
        
            if nums[abs(idx)-1]>0:
                nums[abs(idx)-1]*=(-1)
            else:
                ans.append(abs(idx))

        return ans
    
    # 1<=elem<=n 
    # [4,3,2,7,8,2,3,1]
    #  0 1 2 3 4 5 6 7
      # -3-2-7-8ad-3-1
    