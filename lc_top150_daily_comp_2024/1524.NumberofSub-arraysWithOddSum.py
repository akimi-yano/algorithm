'''
1524. Number of Sub-arrays With Odd Sum
Medium
Topics
Companies
Hint
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
'''

class Solution:
    MOD = 10 ** 9 + 7
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
        - If two prefix sums have the same parity (both even or both odd), 
            their difference will be even, meaning the subarray sum is even.
        - If two prefix sums have different parity (one is even, the other is odd), 
            their difference will be odd, meaning the subarray sum is odd.

        We maintain a cumulative prefixSum while keeping track of how many times 
        we've seen an even or odd prefix sum before the current index. 

        - If prefixSum is even, it means the subarray sum from the start to the current index is even. 
            To form an odd subarray, we need to subtract a previously seen odd prefix sum. 
            So, we add the count of previously seen odd prefix sums to our answer.
        - If prefixSum is odd, the subarray sum from the start to the current index is odd. 
            To form another odd subarray, we need to subtract a previously seen even prefix sum. 
            So, we add the count of previously seen even prefix sums to our answer.
        '''
        prefix_sum = 0
        count_odds = 0
        count_evens = 1 # as we are starting with the prefix_sum of 0
        ans = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2:
                ans += count_evens
                count_odds += 1
            else:
                ans += count_odds
                count_evens += 1    
            ans %= Solution.MOD
        return ans