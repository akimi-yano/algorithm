'''
2033. Minimum Operations to Make a Uni-Value Grid
Medium
Topics
Companies
Hint
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

 

Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:


Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:


Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104
'''

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        '''
        The target value is the median of the sorted grid values
        '''

        # Flatten and Sort the Grid - Convert the 2D grid into a 1D sorted array of values
        flattened_and_sorted = sorted([elem for row in grid for elem in row])

        # Check if every element can be transformed to the first element by verifying that 
        # the absolute difference between each element and the first element is divisible by x
        for elem in flattened_and_sorted:
            # if any element cannot be transformed, return -1
            if abs(elem - flattened_and_sorted[0]) % x != 0:
                return -1

        # Find median
        median = flattened_and_sorted[len(flattened_and_sorted) // 2]
        # Calculate the number of operations by using the median as the target value to minimize total operations
        num_operations = 0
        for elem in flattened_and_sorted:
            # Sum the number of x operations needed to transform each element to the median - diff // x
            num_operations += abs(elem - median) // x
        return num_operations