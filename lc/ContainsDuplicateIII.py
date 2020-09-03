# Contains Duplicate III

# Solution
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:

# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false


# This solution does not work !
# brute forced: 40 / 41 test cases passed but not the last one ! Let's optimize !
'''
        abs()<=t
        absolute difference between nums[i] and nums[j] is at most t 
        
        abs()<=k
        absolute difference between i and j is at most k
        
        
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
               i i i i i i
               j j j j j j
               
               i!=j and abs(i-j)<=k and abs(nums[i]-nums[j])<=t:
               return True
        return False
               
Output: false
'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and abs(i-j)<=k and abs(nums[i]-nums[j])<=t:
                    return True
        return False
    

# THIS SOLUTION WORKS  !

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        k_elems = SortedList()
        for i, num in enumerate(nums):
            if len(k_elems)>k:
                k_elems.remove(nums[i-k-1])
                
            left = 0 
            right = len(k_elems)-1
            while left<=right:
                mid = (left+right)//2
                if abs(k_elems[mid]-num)<=t:
                    return True
                elif num < k_elems[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            k_elems.add(num)
        
        return False
    
    
# Slight optimization with bisect library to find the index of arr using BST!

from sortedcontainers import SortedList
import bisect 
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k<0 or t<0:
            return False
        
        k_elems = SortedList()
        for i, num in enumerate(nums):
            if len(k_elems)>k:
                k_elems.remove(nums[i-k-1])
                
            pos1 = bisect_left(k_elems,num-t)
            pos2 = bisect_right(k_elems,num+t)
            
            if pos1!=pos2:
                return True

            k_elems.add(num)
        
        return False
            
    
'''
Python one pass solution, O(n) time O(n) space using buckets

The idea is like the bucket sort algorithm. Suppose we have consecutive buckets covering the range of 
nums with each bucket a width of (t+1). If there are two item with difference <= t, one of the two will happen:

(1) the two in the same bucket
(2) the two in neighbor buckets
For detailed explanation see my blog here

'''

def containsNearbyAlmostDuplicate(self, nums, k, t):
    if t < 0: return False
    n = len(nums)
    d = {}
    w = t + 1
    for i in range(n):
        m = nums[i] // w
        if m in d:
            return True
        if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
            return True
        if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
            return True
        d[m] = nums[i]
        if i >= k: del d[nums[i - k] // w]
    return False


# IMPROVEMENT !!! - use k_elems.bisect_left(num-t) and k_elems.bisect_right(num+t) as the method built info for SortedList!!!
# Actually this is faster !!!! than the original solutions 

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k<0 or t<0:
            return False
        
        k_elems = SortedList()
        for i, num in enumerate(nums):
            if len(k_elems)>k:
                k_elems.remove(nums[i-k-1])
                
            pos1 = k_elems.bisect_left(num-t)
            pos2 = k_elems.bisect_right(num+t)
            
            if pos1!=pos2:
                return True

            k_elems.add(num)
        
        return False
            