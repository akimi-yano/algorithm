# 980. Unique Paths III
# Hard

# 887

# 75

# Add to List

# Share
# On a 2-dimensional grid, there are 4 types of squares:

# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, 
# that walk over every non-obstacle square exactly once.



# Example 1:

# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:

# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:

# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.


# Note:

# 1 <= grid.length * grid[0].length <= 20



# YAY THIS SOLUTION  WORKS !  

'''
Yaayyy just solved a HARD problem purely on my own for the first time ! Within less than 30 mins ! 
Thank you #leetcode for the challenges ! My life has seen much more exciting with daily algorithm challenges 
#assumeGoodIntentionFromChallenges 
'''

'''
EXPLANATION:
- dfs to go through all the nodes except 2 and -1
- and then check if the current one is 2
- back tracking
'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        seen = set([])
        
        def helper(row,col,m,n,target):
            if not 0<=row<=m-1 or not 0<=col<=n-1 or grid[row][col] == -1:
                return 0
            if (row, col) in seen:
                return 0
            if len(seen) == target-1:
                if grid[row][col] == 2:
                    return 1

            seen.add((row,col))
            ans = helper(row+1,col,m,n,target) + helper(row-1,col,m,n,target) + helper(row,col+1,m,n,target) + helper(row,col-1,m,n,target)
            seen.remove((row,col))
            return ans
            
        m = len(grid)
        n =  len(grid[0])
        
        target = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]!=-1:
                    target+=1
        
        # print(target)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:  
                    return helper(row,col,m,n,target)
                
                
                
                
# Another solution:
'''
If you look carefully at your problem constraints: m*n <= 20, where m and n your grid sizes, we can guess, that we need to use dfs in this problem: 
that is try to check all possible options. So, we need to do several steps:

Find our starting point: traverse all grid and find cell with value 1. Also count number of cells we need to visit, I denoted them empty.
Now, use recursive dfs(x,y, rest) function, where x and y are current coordinates in our cell and rest is how many empty cells we need to traverse.
2.1 First we check if we can move to the current cell: if it is outside our grid and it is already visited or have obstacle, we return
2.2 If current cell is end cell and we already visited all cells, we add 1 to self.ans.
2.3 Define list of neighbours and for each of them run our dfs: mark visited cell with -2 and then mark it back when we go outside recursion. 
It is important to do this, because in python grid is global variable and we need to change it back.
FInally, we just run dfs(sx, sy, empty - 1), where (sx, sy) is coordinates of starting cell and return self.ans.
Complexity: Space complexity is O(mn), this is the possible biggest length of our recursion stack. Time complexity is O(3^(mn)), 
because on each step (except first) we have no more than 3 options to go: all directions except direction we came from. 
In practice however it will work much faster than this estimate because of big number of dead-ends
'''
class Solution:
    def uniquePathsIII(self, grid):
        self.ans, empty = 0, 0
        m, n = len(grid[0]), len(grid)
        def dfs(x, y, rest):
            if x < 0 or x >= n or y < 0 or y >= m or  grid[x][y] < 0: return
            if grid[x][y] == 2 and rest == 0:
                self.ans += 1
            
            neibs = [[0,1],[0,-1],[1,0],[-1,0]]
            for dx, dy in neibs:
                save = grid[x][y]
                grid[x][y] = -2
                dfs(x+dx, y+dy, rest - 1)
                grid[x][y] = save
            
        for i,j in product(range(n), range(m)):
            if grid[i][j] == 1: (sx, sy) = (i,j)
            empty += (grid[i][j] != -1)

        dfs(sx, sy, empty-1)
        return self.ans