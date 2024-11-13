'''
2563. Count the Number of Fair Pairs
Medium
Topics
Companies
Hint
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
'''

from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        lower = 4
        upper = 7

        i = 0:
            nums[0] = 1
            j = 1 -> 1 + 3 = 4
            ...
            j 1 + 6 = 7

        i = 1:
        '''
        sorted_list = SortedList(nums)
        ans = 0
        for i in range(len(nums)):
            sorted_list.remove(nums[i])
            lowerend = sorted_list.bisect_left(lower-nums[i])
            upperend = sorted_list.bisect_right(upper-nums[i])
            ans += upperend - lowerend 
        return ans