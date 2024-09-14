'''
2419. Longest Subarray With Maximum Bitwise AND
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        largest = max(nums)
        best = 0
        l = 0
        while l < len(nums):
            if nums[l] == largest:
                r = l 
                while r < len(nums) and nums[r] == largest:
                    best = max(best, r-l+1)
                    r += 1
                l = r
            l += 1
        return best


# Time: O(N)
# Space: O(1)

# More simple code - but need to be more careful about edge cases:

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur_streak = 0
        ans = 0
        largest_num = 0
        for num in nums:
            if num > largest_num:
                largest_num = num
                ans = cur_streak = 0
            
            if num == largest_num:
                cur_streak += 1
            else:
                cur_streak = 0
            ans = max(ans, cur_streak)
        return ans
                
# Time: O(N)
# Space: O(1)