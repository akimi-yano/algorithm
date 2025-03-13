'''
3356. Zero Array Transformation II
Medium
Topics
Companies
Hint
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 5 * 105
1 <= queries.length <= 105
queries[i].length == 3
0 <= li <= ri < nums.length
1 <= vali <= 5
'''

# Sweepline Approach:

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) ->  int:
        N = len(nums)
        counts = [0 for _ in range(N+1)] # This is for sweepline
        running_total = 0
        k = 0
        for i in range(N):
            while (running_total + counts[i]) < nums[i]:
                if k >= len(queries):
                    return -1
                l, r, val = queries[k]
                k += 1
                if r < i:
                    continue
                counts[max(l, i)] += val # This is for sweepline
                counts[r + 1] -= val # This is for sweepline
            running_total += counts[i]
        return k

# Binary Search + Sweepline Approach:

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) ->  int:
        N = len(nums)
        
        def can_make_zero_arr(k):
            counts = [0 for _ in range(N+1)]

            for i in range(k):
                l, r, val = queries[i]
                counts[l] += val
                counts[r+1] -= val
            
            running_total = 0
            for i in range(N):
                running_total += counts[i]
                if running_total < nums[i]:
                    return False
            return True

        left = 0
        right = len(queries)
        if not can_make_zero_arr(right):
            return -1
        
        while left < right:
            mid = (left + right) // 2
            if can_make_zero_arr(mid):
                right = mid
            else:
                left = mid + 1
        return left