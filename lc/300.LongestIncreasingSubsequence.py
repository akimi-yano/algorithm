# 300. Longest Increasing Subsequence

# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if i not in d:
                d[i]=[]
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    d[i].append(j)
        memo = {}
        def helper(i):

            if i in memo:
                return memo[i]
            local_max = 1
            if i in d:
                for next_idx in d[i]:
                    local_max=max(local_max,1+helper(next_idx))

            memo[i] = local_max      
            return local_max
            
        max_length = 0
        for k in d:
            max_length=max(max_length,helper(k))
        return max_length
    
# IMPORTANT - its ok to not wrtite base case explicitly as long as the recursive call does not keep calling new new recursive stack
# Sometimes you dont write a base case in the first line 