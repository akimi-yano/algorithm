'''
3397. Maximum Number of Distinct Elements After Operations
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

 

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
'''

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # greedily assign the smallest possible valid number for each 
        # element that is still greater than the previously chosen one
        '''
        Thought: Order dosnt matter -> then maybe sorting can help ?
        1 Sort the array in ascending order.
        2 Keep a variable prev to store the last used distinct 
        value (initialize very small).
        3 For each element a in the sorted array:
            - Calculate its valid range [a - k, a + k].
            - Pick the smallest possible value 
            x = max(prev + 1, a - k) that is still distinct.
            - If x <= a + k, count it and update prev = x.
        4 The final count represents the maximum number of 
        distinct elements we can achieve.
        '''
        nums.sort()
        count = 0
        prev = float('-inf')
        for a in nums:
            lowest = a - k
            highest = a + k
            x = prev + 1
            if x < lowest: # x = max(prev + 1, a - k) that is still distinct
                x = lowest
            if x <= highest:
                count += 1
                prev = x
        return count