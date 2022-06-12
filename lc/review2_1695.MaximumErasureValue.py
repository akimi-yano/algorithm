# 1695. Maximum Erasure Value
# Medium

# 1278

# 20

# Add to List

# Share
# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

# Example 1:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:

# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# This solution works:


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
        4,2,4,5,6
            r
         l    
        seen: 2, 4, 5, 
        '''
        # make prefix sum table
        prefix_sum = {-1:0}
        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            prefix_sum[i] = running_sum
            
        # use the index and prefix sum table to get max
        best = 0
        seen = set([])
        left = 0
        for right, num in enumerate(nums):
            while num in seen:
                seen.remove(nums[left])
                left += 1
            seen.add(num)
            best = max(best, prefix_sum[right]-prefix_sum[left-1])
        return best
            