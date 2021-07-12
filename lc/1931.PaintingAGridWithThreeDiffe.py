# 1931. Painting a Grid With Three Different Colors
# Hard

# 85

# 6

# Add to List

# Share
# You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

# Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:


# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are shown in the image above.
# Example 2:


# Input: m = 1, n = 2
# Output: 6
# Explanation: The six possible colorings are shown in the image above.
# Example 3:

# Input: m = 5, n = 5
# Output: 580986
 

# Constraints:

# 1 <= m <= 5
# 1 <= n <= 1000


# This approach does not work:

# class Solution:
#     MOD = 10 ** 9 + 7
#     def colorTheGrid(self, m: int, n: int) -> int:

#         @lru_cache(None)
#         def helper(row, col, color):
#             if not(0<=row<m) or not(0<=col<n) or matrix[row][col] != 0:
#                 # (row, col) in seen
#                 return 0
#             if row == m-1 and col == n-1:
#                 return 1
#             matrix[row][col] = color
#             # seen.add((row, col))
#             options = 0
#             for next_c in range(1, 4):
#                 if next_c != color:
#                     options = (options + helper(row+1, col, next_c)) % Solution.MOD
#                     options = (options + helper(row-1, col, next_c)) % Solution.MOD
#                     options = (options + helper(row, col+1, next_c)) % Solution.MOD
#                     options = (options + helper(row, col-1, next_c)) % Solution.MOD
#             matrix[row][col] = 0
#             # seen.remove((row, col))
#             return options
        
#         ans = 0
#         matrix = [[0 for _ in range(n)] for _ in range(m)]
#         for num in range(1, 4):
#             # seen = set([])   
#             ans = (ans + helper(0, 0, num)) % Solution.MOD
        
#         return ans % Solution.MOD

# This solution works:

class Solution:
    MOD = 10 ** 9 + 7
    def colorTheGrid(self, m: int, n: int) -> int:
        '''
        1 make all the possible choices for each row and save it
        2 for each row save all the possible next rows
        3 count the valid ones and return
        '''
        rows = []
        def helper(i, arr):
            if i > m-1:
                rows.append("".join(arr))
                return
            for c in "rgb":
                if not arr or arr[-1] != c:
                    helper(i+1, arr + [c])
        helper(0, [])
        
        choices = defaultdict(list)
        for i in range(len(rows)):
            for j in range(i+1, len(rows)):
                valid = True
                for col in range(len(rows[i])):
                    if rows[i][col] == rows[j][col]:
                        valid = False
                        break
                if valid:
                    choices[rows[i]].append(rows[j])
                    choices[rows[j]].append(rows[i])
        
        @lru_cache(None)
        def helper2(row, remaining_rows):
            if remaining_rows == 0:
                return 1
            
            ans = 0
            for next_row in choices[row]:
                ans += helper2(next_row, remaining_rows-1)
            return ans % Solution.MOD
        
        return sum(helper2(row, n-1) for row in rows) % Solution.MOD