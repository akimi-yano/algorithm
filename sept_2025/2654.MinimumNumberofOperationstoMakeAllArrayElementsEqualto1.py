'''
2654. Minimum Number of Operations to Make All Array Elements Equal to 1
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

 

Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.
 

Constraints:

2 <= nums.length <= 50
1 <= nums[i] <= 106
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        - If the array already contains some 1s, we can use them to "spread" 1s across the array using minimal operations.

        - Otherwise, we must find a subarray whose GCD equals 1 — because only then can we generate a 1 that can be used to make others 1.
        '''
        N = len(nums)
        ones = nums.count(1)
        if ones:
            return N - ones
        ans = float('inf')
        # find the shortest subarray whose GCD is 1
        for i in range(N):
            g = nums[i]
            for j in range(i+1, N):
                g = gcd(g, nums[j])
                if g == 1:
                    ans = min(ans, j-i)
        if ans == float('inf'):
            return -1
        else:
            return ans + N - 1