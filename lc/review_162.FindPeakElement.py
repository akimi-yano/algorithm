# 162. Find Peak Element
# Medium

# 3446

# 2866

# Add to List

# Share
# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

# This solution works:

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get(idx):
            if not 0 <= idx < len(nums):
                return float('-inf')
            return nums[idx]
        left, right = 0, len(nums) - 1
        # if left is peak
        if get(left-1) < get(left) and get(left) > get(left+1):
            return left
        # if right is peak
        if get(right-1) < get(right) and get(right) > get(right+1):
            return right
        # else, it means it's going up at left (/), and going down at right (\)
        # -inf, [1, (something > 1), ... (something > 1), 1], -inf
        
        while True:
            mid = (left + right) // 2
            # option 1: mid is peak (^)
            if get(mid-1) < get(mid) and get(mid) > get(mid+1):
                return mid
            # option 2: mid is going up (/), so update left
            elif get(mid-1) < get(mid) < get(mid+1):
                left = mid + 1
            # option 3: mid is going down (\), so update right
            elif get(mid-1) > get(mid) > get(mid+1):
                right = mid - 1
            # option 4: mid is at bottom (v)
            elif get(mid-1) > get(mid) and get(mid) < get(mid+1):
                right = mid - 1
            else:
                raise Exception("THIS SHOULD NOT HAPPEN")