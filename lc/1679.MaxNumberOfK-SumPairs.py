# 1679. Max Number of K-Sum Pairs
# Medium

# 23

# 2

# Add to List

# Share
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.



# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109


# This solution works !

from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        times = 0
        for num in nums:
            if num in counts:
                another = k - num 
                if num == another:
                    if num in counts and counts[num] >= 2:
                        counts[num] -= 2
                        if counts[num]  <= 0:
                            del counts[num]
                        times += 1 
                elif another in counts:
                    counts[num]  -= 1
                    if counts[num]  <= 0:
                        del counts[num]
                    counts[another] -= 1
                    if counts[another] <=0:
                        del counts[another]
                    times += 1          
    
        return times