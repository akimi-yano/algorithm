'''
862. Shortest Subarray with Sum at Least K
Hard
Topics
Companies
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''

from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([[0, -1]]) # val, idx
        cur = 0
        min_len = float('inf')
        for i, num in enumerate(nums):
            cur += num
            while queue and cur-queue[0][0] >= k:
                _, prev_idx = queue.popleft()
                min_len = min(min_len, i-prev_idx)
            while queue and queue[-1][0] >= cur:
                queue.pop()
            queue.append([cur, i])
        return min_len if min_len < float('inf') else -1