'''
2379. Minimum Recolors to Get K Consecutive Black Blocks
Easy
Topics
Companies
Hint
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
 

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        @cache
        def helper(i, remaining):
            if remaining == 0:
                return 0
            if i > len(blocks)-1:
                return float('inf')
            min_step = float('inf')
            if blocks[i] == 'W':
                min_step = min(min_step, 1 + helper(i+1, remaining-1))
                min_step = min(min_step, helper(i+1, k))
            else:
                min_step = min(min_step, helper(i+1, remaining-1))
            return min_step

        return helper(0, k)
    
# Optimization:

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        sliding window approach:
        count the number of W for each window and take minimum
        '''
        min_white_count = float('inf')
        black_count = 0
        for i in range(len(blocks)):
            if i - k >= 0 and blocks[i - k] == 'B':
                black_count -= 1
            if blocks[i] == 'B':
                black_count += 1
            min_white_count = min(min_white_count, k - black_count)
        return min_white_count