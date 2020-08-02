# 1537. Get the Maximum Score

# You are given two sorted arrays of distinct integers nums1 and nums2.

# A valid path is defined as follows:

# Choose array nums1 or nums2 to traverse (from index-0).
# Traverse the current array from left to right.
# If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
# Score is defined as the sum of uniques values in a valid path.

# Return the maximum score you can obtain of all possible valid paths.

# Since the answer may be too large, return it modulo 10^9 + 7.

 

# Example 1:



# Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
# Output: 30
# Explanation: Valid paths:
# [2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
# [4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
# The maximum is obtained with the path in green [2,4,6,8,10].
# Example 2:

# Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
# Output: 109
# Explanation: Maximum sum is obtained with the path [1,3,5,100].
# Example 3:

# Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
# Output: 40
# Explanation: There are no common elements between nums1 and nums2.
# Maximum sum is obtained with the path [6,7,8,9,10].
# Example 4:

# Input: nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
# Output: 61
 

# Constraints:

# 1 <= nums1.length <= 10^5
# 1 <= nums2.length <= 10^5
# 1 <= nums1[i], nums2[i] <= 10^7
# nums1 and nums2 are strictly increasing.



# Intuition
# Basically, at each node, you have two choices: 1) to switch and 2) to NOT switch to the other array. I recorded the indices of each value in each array to make the switching easier. I also kept two booleans at1 and at2 to check which array I am in currently. When we reach the base case, we just return 0, but along the path, we accumulate the current value to the result, then return the maximum of the paths at the end. It is important to use your own memoization and NOT to use lru_cache for this one because I think lru_cache evicts so many entries and causes recursion stack overflow.

# Time/Space Complexity
# Time: O(N * 2 * 2) = O(N) where N = max(len(nums1), len(nums2)) due to memoization.
# Space: Same as the Time Complexity



# this  solution does not work - see below
# class Solution:
#     def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
# #         can start with either
# #         if you find the same val you van traverse to the other array
# #         keep track of max 
#         def helper(arr1,idx1,arr2,idx2):
#             if idx1>len(arr1)-1:
#                 return 0
#             max_score = float('-inf')
            
#             max_score = max(max_score,arr1[idx1]+helper(arr1,idx1+1,arr2,idx2))
#             for k in range(idx2,len(arr2)):
#                 if arr2[k]==arr1[idx1]:
#                     max_score=max(max_score,helper(arr2,k,arr1,idx1))            
#             return max_score
        
#         nums1_start = helper(nums1,0,nums2,0)
#         nums2_start = helper(nums2,0,nums1,0)
#         return max(nums1_start,nums2_start)




# this works !

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        pos1 = collections.defaultdict(int)
        pos2 = collections.defaultdict(int)
        for i, n in enumerate(nums1):
            pos1[n] = i
        for i, n in enumerate(nums2):
            pos2[n] = i
        
        memo = [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(max(len(nums1), len(nums2)))]
        def rec(curr_i, at1, at2):
            if curr_i >= len(nums1) and curr_i >= len(nums2):
                return 0
            if (curr_i >= len(nums1) and at1) or (curr_i >= len(nums2) and at2):
                return 0
            if memo[curr_i][at1][at2] == -1:
                no_change = change = 0
                if at1:
                    if nums1[curr_i] in pos2:
                        change = nums1[curr_i] + rec(pos2[nums1[curr_i]] + 1, False, True)
                elif at2:
                    if nums2[curr_i] in pos1:
                        change = nums2[curr_i] + rec(pos1[nums2[curr_i]] + 1, True, False)
                no_change = (nums1[curr_i] if at1 else nums2[curr_i]) + rec(curr_i + 1, at1, at2)
                memo[curr_i][at1][at2] = max(no_change, change)
            return memo[curr_i][at1][at2]
        
        return max(rec(0, True, False), rec(0, False, True)) % (10**9 + 7)
    
    
    
# this works - most intuitive way to me !

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:        
        
        MOD = (10**9 + 7)
        n1_idx = {}
        n2_idx = {}
        
        for i,num in enumerate(nums1):
            n1_idx[num]=i
        for i,num in enumerate(nums2):
            n2_idx[num]=i
        
        memo = {}
        def helper(cur_list_idx,other_list_idx, i, can_hop):
            key = (cur_list_idx, other_list_idx, i, can_hop)
            if key in memo:
                return memo[key]
            cur_list = nums1 if cur_list_idx == 0 else nums2
            other_list = nums1 if other_list_idx == 0 else nums2

            if i >= len(cur_list):
                memo[key] = 0
                return 0

            cur_value = cur_list[i]
            option1 = cur_value + helper(cur_list_idx, other_list_idx, i+1, True)
            option2 = 0
            if can_hop:
                # if we're currently iterating over nums1
                if cur_list is nums1:
                    # see if we can hop to nums2
                    if cur_value in n2_idx:
                        new_i = n2_idx[cur_value]
                        option2 = helper(other_list_idx, cur_list_idx, new_i, False)
                # elif we're currently iterating over nums2
                elif cur_list is nums2:
                    # see if we can hop to nums1
                    if cur_value in n1_idx:
                        new_i = n1_idx[cur_value]
                        option2 = helper(other_list_idx, cur_list_idx, new_i, False)

            ans = max(option1, option2)
            memo[key] = ans
            return ans
            
        
        return max(
            helper(0, 1, 0, True),
            helper(1, 0, 0, True)) % MOD