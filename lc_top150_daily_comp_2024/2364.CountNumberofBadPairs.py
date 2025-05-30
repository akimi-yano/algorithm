'''
2364. Count Number of Bad Pairs
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

 

Example 1:

Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        all_pairs = math.comb(N, 2)
        diff_from_idx = Counter()
        good_pairs = 0
        for i, num in enumerate(nums):
            diff = num - i
            good_pairs += diff_from_idx[diff]
            diff_from_idx[diff] += 1
        return all_pairs - good_pairs

# Another way

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        diff_from_idx = Counter()
        good_pairs = 0
        for i, num in enumerate(nums):
            diff = num - i
            good_pairs += diff_from_idx[diff]
            diff_from_idx[diff] += 1
        return (N*(N-1))//2 - good_pairs

