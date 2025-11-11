'''
474. Ones and Zeroes
Solved
Medium
Topics
premium lock icon
Companies
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
'''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        for i, string in enumerate(strs):
            memo[i] = Counter()
            for elem in string:
                memo[i][elem] += 1

        N = len(strs)
        @cache
        def helper(ones, zeros, i):
            nonlocal n, m, N
            if i >= N:
                return 0
            max_num_subsets = 0
            one_count = memo[i]['1']
            zero_count = memo[i]['0']

            if (one_count + ones) <= n and (zero_count + zeros) <= m:
                max_num_subsets = max(max_num_subsets, 1 + helper(one_count + ones, zero_count + zeros, i+1))
            max_num_subsets = max(max_num_subsets, helper(ones, zeros, i+1))
            return max_num_subsets
            
        return helper(0, 0, 0)