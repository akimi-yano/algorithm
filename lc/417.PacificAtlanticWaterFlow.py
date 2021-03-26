# 417. Pacific Atlantic Water Flow
# Medium

# 1974

# 499

# Add to List

# Share
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Note:

# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
 

# Example:

# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


# This solution works:

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
          Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
        '''
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return []
        def helper(row, col, orig_row, orig_col, prev):
            nonlocal seen
            key = (row, col) 
            if not(0<=row<ROW) or not(0<=col<COL) or prev < matrix[row][col] or key in seen:
                return
            seen.add(key)
            if key in pacific or key in atlantic:
                memo[(orig_row, orig_col)].add(key)
                
            helper(row+1, col, orig_row, orig_col, matrix[row][col])
            helper(row-1, col, orig_row, orig_col, matrix[row][col])
            helper(row, col+1, orig_row, orig_col, matrix[row][col])
            helper(row, col-1, orig_row, orig_col, matrix[row][col])
            
        pacific = set([])
        atlantic = set([])
        memo = {}
        ROW = len(matrix)
        COL = len(matrix[0])
        
        for row in range(ROW):
            pacific.add((row, 0))
            atlantic.add((row, COL-1))
            
        for col in range(COL):
            pacific.add((0, col)) 
            atlantic.add((ROW-1, col))
       
        for row in range(ROW):
            for col in range(COL):
                memo[(row, col)] = set([])
                seen = set([])
                helper(row, col, row, col, float(inf))
  
        ans = []
        for (row, col), arr in memo.items():
            reached_pacific = reached_atlantic = False
            for r, c in arr:
                if (r, c) in pacific:
                    reached_pacific = True
                if (r, c) in atlantic:
                    reached_atlantic = True
                if reached_pacific and reached_atlantic:
                    ans.append([row, col])
                    break

        return ans
        
# This solution works - optimization:

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return []

        R = len(matrix)
        C = len(matrix[0])

        reached_pacific = set([])
        reached_atlantic = set([])
        
        queue = deque([(0, c, float('-inf')) for c in range(C)] + [(r, 0, float('-inf')) for r in range(1, R)])
        while queue:
            r, c, prev = queue.popleft()
            # if r, c is invalid, or matrix[r][c] is smaller than the previous value
            if not 0 <= r < R or not 0 <= c < C or matrix[r][c] < prev:
                continue
            if (r, c) in reached_pacific:
                continue
            reached_pacific.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                queue.append((r+dr, c+dc, matrix[r][c]))
        
        queue = deque([(R-1, c, float('-inf')) for c in range(C)] + [(r, C-1, float('-inf')) for r in range(R-1)])
        while queue:
            r, c, prev = queue.popleft()
            # if r, c is invalid, or matrix[r][c] is smaller than the previous value
            if not 0 <= r < R or not 0 <= c < C or matrix[r][c] < prev:
                continue
            if (r, c) in reached_atlantic:
                continue
            reached_atlantic.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                queue.append((r+dr, c+dc, matrix[r][c]))
        
        # print(reached_pacific)
        
        return reached_pacific.intersection(reached_atlantic)