'''
3276. Select Cells in Grid With Maximum Score
Solved
Hard
Topics
Companies
Hint
You are given a 2D matrix grid consisting of positive integers.

You have to select one or more cells from the matrix such that the following conditions are satisfied:

No two selected cells are in the same row of the matrix.
The values in the set of selected cells are unique.
Your score will be the sum of the values of the selected cells.

Return the maximum score you can achieve.

 

Example 1:

Input: grid = [[1,2,3],[4,3,2],[1,1,1]]

Output: 8

Explanation:



We can select the cells with values 1, 3, and 4 that are colored above.

Example 2:

Input: grid = [[8,7,6],[8,3,2]]

Output: 15

Explanation:



We can select the cells with values 7 and 8 that are colored above.

 

Constraints:

1 <= grid.length, grid[i].length <= 10
1 <= grid[i][j] <= 100
'''

# This solution works great!:

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        '''
        set a rule to only choose a number that is smaller than last_chosen_number
        ^ this is to be able to memo
        also for rows_used, use a bitmast to efficiently keep track of it (also memo friendly)
        '''
        @cache
        def helper(rows_used, last_chosen_number):
            best = 0
            for i, row in enumerate(grid):
                # if the row is not used, we can try using it
                if not ((1 << i) & rows_used):
                    new_rows_used = (1 << i) | rows_used
                    # first option: skip the row
                    best = max(best, helper(new_rows_used, last_chosen_number))
                    for elem in row:
                        if elem < last_chosen_number:
                            best = max(best, elem + helper(new_rows_used, elem))
            return best
        
        return helper(0, float('inf'))

# Time: O(2^M * K) K is the number of unique elem in the grid, M is the number of row of the grid; its 2^M since I used bitmask
# Space: O(2^M * K) is the number of scopes of recursive call stacks