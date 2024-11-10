'''
3097. Shortest Subarray With OR at Least K II
Attempted
Medium
Topics
Companies
Hint
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty 
subarray
 of nums, or return -1 if no special subarray exists.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.

 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
'''

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1

        N = len(nums)
        counts = [0] * 32

        def cur_value_fn():
            value = 0
            for bit in range(32):
                value |= 1 << bit if counts[bit] > 0 else 0
            return value

        l = r = 0
        ans = inf
        while l < N:
            cur_value = cur_value_fn()
            if cur_value >= k:
                ans = min(ans, r-l)
                prev_num = nums[l]
                for bit in range(32):
                    if prev_num & 1 << bit:
                        counts[bit] -= 1
                l += 1
            elif r < N:
                num = nums[r]
                for bit in range(32):
                    if num & 1 << bit:
                        counts[bit] += 1
                r += 1
            else:
                break
        return ans if ans < inf else -1