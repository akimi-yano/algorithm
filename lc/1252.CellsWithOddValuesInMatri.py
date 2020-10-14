# 1252. Cells with Odd Values in a Matrix
# Easy

# 337

# 542

# Add to List

# Share
# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment to all indices.



# Example 1:


# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
# Example 2:


# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.


# Constraints:

# 1 <= n <= 50
# 1 <= m <= 50
# 1 <= indices.length <= 100
# 0 <= indices[i][0] < n
# 0 <= indices[i][1] < m


# This solution works ! - brute force
# Time: O(L * max(M, N) + MN)
# Space: O(MN)
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        grid = [[0 for _ in range(m)] for _ in range(n)]
        
        for r, c in indices:
            for i in range(m):
                grid[r][i] += 1
            for k in range(n):
                grid[k][c] += 1
                
        ans = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] %2 != 0:
                    ans += 1
        return ans
    

# This solution works ! - bitwise :)
# Time: O(L + MN)
# Space: O(M + N)

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0]*n
        cols = [0]*m
        
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
            
        ans = 0
        for r in rows:
            for c in cols:
                ans += r^c
    
        return ans