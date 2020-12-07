# 1681. Minimum Incompatibility
# Medium

# 14

# 35

# Add to List

# Share
# You are given an integer array nums​​​ and an integer k. You are asked to distribute this array into k subsets of equal size such that there are no two equal elements in the same subset.

# A subset's incompatibility is the difference between the maximum and minimum elements in that array.

# Return the minimum possible sum of incompatibilities of the k subsets after distributing the array optimally, or return -1 if it is not possible.

# A subset is a group integers that appear in the array with no particular order.

 

# Example 1:

# Input: nums = [1,2,1,4], k = 2
# Output: 4
# Explanation: The optimal distribution of subsets is [1,2] and [1,4].
# The incompatibility is (2-1) + (4-1) = 4.
# Note that [1,1] and [2,4] would result in a smaller sum, but the first subset contains 2 equal elements.
# Example 2:

# Input: nums = [6,3,8,1,3,1,2,2], k = 4
# Output: 6
# Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and [1,3].
# The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
# Example 3:

# Input: nums = [5,3,3,6,3,3], k = 3
# Output: -1
# Explanation: It is impossible to distribute nums into 3 subsets where no two elements are equal in the same subset.
 

# Constraints:

# 1 <= k <= nums.length <= 16
# nums.length is divisible by k
# 1 <= nums[i] <= nums.length

# This approach does not work - TLE 

# from collections import Counter
# class Solution:
#     def minimumIncompatibility(self, nums: List[int], k: int) -> int:
#         counts = Counter(nums)
#         if max(counts.values()) > k:
#             return -1
#         storage = [tuple() for _ in range(k)]
#         ans = []
#         eachnum = len(nums)// k

#         @lru_cache(None)
#         def helper(i, arr):
#             if i > len(nums)-1:
#                 # print(arr)
#                 temp = 0
#                 for j in range(len(arr)):
#                     if arr[j]:
#                         temp += max(arr[j]) - min(arr[j])
#                 # self.min_val = min(temp, self.min_val)
#                 return temp
#             min_val = float('inf')
#             elem = nums[i]
            
#             for idx in range(len(arr)):
#                 if eachnum > len(arr[idx]) and elem not in arr[idx]:
#                     arr = [set(tup) for tup in arr]
#                     arr[idx].add(elem)
#                     arr = tuple(tuple(se) for se in arr)
#                     min_val = min(min_val, helper(i+1, arr))
#                     # helper(i+1, arr)
#                     arr = [set(tup) for tup in arr]
#                     arr[idx].remove(elem)
                    
#             return min_val
#         # self.min_val = float('inf')

#         return helper(0, tuple(storage))
#         # return self.min_val      
        
        
# This solution works !
'''
        # Idea: store the results of all valid subsets of the original array, there are at most 2^16=65536 states that we need to calculate.
        # Time complexity: O(n 2^n)
'''

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d=len(nums)//k # the length of each partition
        
        @lru_cache(None)
        def helper(nums):
            if not nums:
                return 0
            ret=float('inf')
            for a in combinations(nums,d): # choose a as a partition
                if len(set(a))<d: # check for duplicates
                    continue
                left=list(nums) # numbers left after removing partition a
                for v in a:
                    left.remove(v)
                ret=min(ret,max(a)-min(a)+helper(tuple(left)))
            return ret
        
        ans=helper(tuple(nums)) # turn the input into a tuple so the function can be cached
        return ans if ans!=float('inf') else -1






'''
0
'''