'''
2342. Max Sum of a Pair With Equal Sum of Digits
Medium
Topics
Companies
Hint
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digitsum_idx = {}
        for i, num in enumerate(nums):
            str_num = str(num)
            total = 0
            for digit in str_num:
                total += int(digit)
            if total not in digitsum_idx:
                digitsum_idx[total] = []
            digitsum_idx[total].append(num)
        
        max_sum = -1
        for pairs in digitsum_idx.values():
            sorted_pairs = sorted(pairs, reverse=True)
            for val in sorted_pairs[1:]:
                max_sum = max(max_sum, val+sorted_pairs[0])
        return max_sum
    
# Optimization:

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digitsum_idx = {}
        max_sum = -1
        for i, num in enumerate(nums):

            str_num = str(num)
            total = 0
            for digit in str_num:
                total += int(digit)
            
            if total not in digitsum_idx:
                digitsum_idx[total] = num
            else:
                max_sum = max(max_sum,  digitsum_idx[total] + num)
                digitsum_idx[total] = max(digitsum_idx[total], num)

        return max_sum
            