'''
3686. Number of Stable Subsequences
Hard
premium lock icon
Companies
Hint
You are given an integer array nums.

A subsequence is stable if it does not contain three consecutive elements with the same parity when the subsequence is read in order (i.e., consecutive inside the subsequence).

Return the number of stable subsequences.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,3,5]

Output: 6

Explanation:

Stable subsequences are [1], [3], [5], [1, 3], [1, 5], and [3, 5].
Subsequence [1, 3, 5] is not stable because it contains three consecutive odd numbers. Thus, the answer is 6.
Example 2:

Input: nums = [2,3,4,2]

Output: 14

Explanation:

The only subsequence that is not stable is [2, 4, 2], which contains three consecutive even numbers.
All other subsequences are stable. Thus, the answer is 14.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 10​​​​​​​5
'''

class Solution:
    MOD = 10 ** 9 + 7
    def countStableSubsequences(self, nums: List[int]) -> int:
        
        N = len(nums)

        @cache
        def helper(i, is_odd, streak):
            if i > N-1:
                return 0
            
            total = 0
            # not use
            total += helper(i+1, is_odd, streak)

            # use
            val = nums[i]
            
            # odd
            if val % 2:
                if is_odd:
                    if streak + 1 < 3:
                        total += 1 + helper(i+1, True, streak + 1)
                else:
                    total += 1 + helper(i+1, True, 1)
            # even
            else:
                if is_odd:
                    total += 1 + helper(i+1, False, 1)
                else:
                    if streak + 1 < 3:
                        total += 1 + helper(i+1, False, streak + 1)

            return total % Solution.MOD
        
        ans = helper(0, False, 0)
        helper.cache_clear()
        return ans % Solution.MOD