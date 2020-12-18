# 334. Increasing Triplet Subsequence
# Medium

# 2078

# 155

# Add to List

# Share
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1


# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?


# this approach does not work 

# import heapq
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         minheap = []
#         maxheap = []
#         memo = {}
#         for i in range(len(nums)):
#             if nums[i] not in memo:
#                 memo[nums[i]] = []
#             memo[nums[i]].append(i)
#             heapq.heappush(minheap, (nums[i],i))
#             heapq.heappush(maxheap, (-nums[i],i))
#         while minheap and maxheap:
#             minnum, minidx = heapq.heappop(minheap)
            
#             maxidx = 0  
#             while maxheap and minidx >= maxidx:
#                 maxnum, maxidx = heapq.heappop(maxheap)
#             maxnum *= (-1)
#             for num in range(minnum+1, maxnum):
#                 if num in memo:
#                     return True
#         return False

# This approach works 

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        second = float('inf')
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num > second:
                return True
            elif num < second:
                if first < num:
                    second = num
                elif num < first:
                    first = num
        return False
    
        '''
        first - keeps track of the first sequence
        second - keeps track of the second sequence
        return true if we find third one
        '''
    
        # [1,4,3,0,5]
        # f 0 
        # s 3
        # 5
        # the answer sequence is not 0-3-5
        # the answer sequence is 1,3,5 or 1,4,5 so its True
        # this works as there must have been a first that came before 3 or 4 showed up so that 3 or 4 became the secound since it only comes second only if the num is between first and second - exclusively smaller than the secound but larger than the first - there must be a number that was smaller than the secound to be able to set secound !