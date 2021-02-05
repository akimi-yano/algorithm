# 594. Longest Harmonious Subsequence
# Easy

# 1013

# 106

# Add to List

# Share
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 2
# Example 3:

# Input: nums = [1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109

# This solution works:
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        def binary_search(left, val):
            right = len(nums)-1
            while left < right:
                mid = (left+right+1)//2
                if nums[mid] <= val:
                    left = mid
                else:
                    right = mid -1
            return left
        
        nums.sort()
        best = 0
        prev = None
        for i in range(len(nums)):
            if prev == nums[i]:
                continue
            end = binary_search(i+1, nums[i]+1)
            if end < len(nums) and nums[i]+1 == nums[end]:
                best = max(best, end - i +1)
            prev = nums[i]
        return best
    
# This solution works - optimization:
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        counts = Counter(nums)
        for num in counts:
            if num+1 in counts:
                ans = max(ans, counts[num] + counts[num+1])
        return ans
