# 1001. Grid Illumination
# Hard

# 238

# 67

# Add to List

# Share
# You are given a grid of size N x N, and each cell of this grid has a lamp that is initially turned off.

# You are also given an array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp at grid[rowi][coli] is turned on. When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.

# Finally, you are given a query array queries, where queries[i] = [rowi, coli]. For the ith query, determine whether grid[rowi][coli] is illuminated or not. After answering the ith query, turn off the lamp at grid[rowi][coli] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either a side or corner with grid[rowi][coli].

# Return an array of integers ans, where ans[i] should be 1 if the lamp in the ith query was illuminated, or 0 if the lamp was not.



# Example 1:


# Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
# Output: [1,0]
# Explanation: We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
# The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.

# The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.

# Example 2:

# Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
# Output: [1,1]
# Example 3:

# Input: N = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
# Output: [1,1,0]


# Constraints:

# 1 <= N <= 109
# 0 <= lamps.length <= 20000
# lamps[i].length == 2
# 0 <= lamps[i][j] < N
# 0 <= queries.length <= 20000
# queries[i].length == 2
# 0 <= queries[i][j] < N



# This approach does not work:

# from collections import Counter
# class Solution:
#     def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
#         def helper(r, c, r_delta, c_delta):
#             if not (0<= r < N) or not (0<= c <N):
#                 return False
#             if (r, c) in rowcol:
#                 return True
#             kotae = False
#             kotae |= helper(r+r_delta, c+c_delta, r_delta, c_delta)
#             return kotae
        
#         row = Counter()
#         col = Counter()
#         rowcol = set([])
#         for r, c in lamps:
#             row[r] += 1
#             col[c] += 1
#             rowcol.add((r,c))
        
#         ans = []
#         for r, c in queries:
#             # read
#             res = 0
#             if r in row:
#                 res = 1
#                 print('row')
#             elif c in col:
#                 res = 1
#                 print('col')
#             elif helper(r, c, 0, 1):
#                 res = 1
#                 print('helper1')
#             elif helper(r, c, 0, -1):
#                 res = 1
#                 print('helper2')
#             elif helper(r, c,  1, 0):
#                 res = 1
#                 print('helper3')
#             elif helper(r, c, -1, 0):
#                 res = 1
#                 print('helper4')
#             ans.append(res)
            
#             # write
#             for r_delta, c_delta in ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)):
#                 newr = r+r_delta
#                 newc = c+c_delta
#                 if (newr, newc) in rowcol:
#                     rowcol.remove((newr, newc))
#                 if newr in row:
#                     row[r] -= 1
#                     if row[r] < 1:
#                         del row[r]
#                 if newc in col:
#                     col[c] -= 1
#                     if col[c] < 1:
#                         del col[c]
#         return ans
        

# This solution works!!:

from collections import Counter
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        self.N = N
        self.rows = Counter()
        self.cols = Counter()
        self.diagonals1 = Counter()
        self.diagonals2 = Counter()

        self.lamps = set([tuple(lamp) for lamp in lamps])

        for r, c in self.lamps:
            self.update(r, c, 1)
        
        ans = []
        for r, c in queries:
            ans.append(self.helper(r,c))

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    r2, c2 = r+dr, c+dc
                    if (r2, c2) in self.lamps:
                        self.update(r2, c2, -1)
                        self.lamps.remove((r2, c2))
        return ans
    
    def helper(self, r, c):
        r1, c1 = r-min(r,c), c-min(r,c)
        r2, c2 = r-min(r, self.N-1-c), c + min(r, self.N-1-c)
        
        if self.rows[r] > 0 \
        or self.cols[c] > 0 \
        or self.diagonals1[(r1, c1)] > 0 \
        or self.diagonals2[(r2, c2)] > 0:
            return 1
        
        return 0
    
    def update(self, r, c, change):
        self.rows[r] += change
        self.cols[c] += change
        
        r1, c1 = r-min(r,c), c-min(r,c)
        self.diagonals1[(r1, c1)] += change
        
        r2, c2 = r-min(r, self.N-1-c), c + min(r, self.N-1-c)
        self.diagonals2[(r2, c2)] += change