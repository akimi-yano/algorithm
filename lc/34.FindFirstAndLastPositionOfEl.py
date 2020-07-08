# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


# Constraints:

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non decreasing array.
# -10^9 <= target <= 10^9



# this is my first approach and it works
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        
        def find_end(start,target):
            low = start
            high = len(nums)-1
            while  low<=high:
                m = (low+high)//2
                if nums[m]==target and (m==len(nums)-1 or nums[m+1]!=target):
                    return [start,m]
                elif nums[m]>target:
                    high = m - 1
                else:
                    low = m + 1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target and (mid==0 or nums[mid-1] != target):
                return find_end(mid,target)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid-1
        return [-1,-1]


# another approach -  this works too
    def searchRange(self, nums, target):
        if len(nums)==0:
            return -1,-1
        n = len(nums)
        left, right = -1, -1
        l, r = 0, n-1
        while l < r:
            m = (l+r)//2
            if nums[m] < target: l = m+1
            else: r = m
        if nums[l] != target: return -1, -1
        left = l
        l, r = left, n-1
        while l < r:
            m = (l+r)//2+1
            if nums[m] == target: l = m
            else: r = m-1
        right = l
        return left, right

# clean code which works

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_start(nums,target):
            idx = -1
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid]>=target:
                    right = mid-1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    idx = mid
            return idx
        
        def find_end(nums,target):
            idx = -1
            low = 0
            high = len(nums)-1
            while  low<=high:
                m = (low+high)//2
                if nums[m]<=target:
                    low = m + 1
                else:
                    high = m - 1
                if nums[m]==target:
                    idx = m
            return idx

        res = [-1,-1]
        res[0] = find_start(nums,target)
        res[1] = find_end(nums,target)
        return res

