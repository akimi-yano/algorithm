# 718. Maximum Length of Repeated Subarray
# Medium

# 2578

# 61

# Add to List

# Share
# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100

# This solution works:

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        def helper(size):
            nonlocal nums1, nums2
            subarrays = set([])
            for i in range(len(nums1) - size + 1):
                subarray = nums1[i:i+size]
                subarrays.add(tuple(subarray))
            for i in range(len(nums2) - size + 1):
                subarray = nums2[i:i+size]
                if tuple(subarray) in subarrays:
                    return True
            return False
        
        left, right = 0, len(nums1)
        while left < right:
            mid = (left + right + 1) // 2
            if helper(mid):
                left = mid
            else:
                right = mid - 1
        return left