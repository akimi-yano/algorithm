'''
3197. Find the Minimum Area to Cover All Ones II
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

Return the minimum possible sum of the area of these rectangles.

Note that the rectangles are allowed to touch.

 

Example 1:

Input: grid = [[1,0,1],[1,1,1]]

Output: 5

Explanation:



The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
The 1 at (1, 1) is covered by a rectangle of area 1.
Example 2:

Input: grid = [[1,0,1,0],[0,1,0,1]]

Output: 5

Explanation:



The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
The 1 at (1, 1) is covered by a rectangle of area 1.
The 1 at (1, 3) is covered by a rectangle of area 1.
 

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is either 0 or 1.
The input is generated such that there are at least three 1's in grid.
'''

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        @lru_cache(None)

        def area(r_start: int, c_start: int, r_end: int, c_end: int) -> int:
            max_row = max_col = float('-inf')
            min_row = min_col = float('inf')
            
            for r, c in product(range(r_start, r_end + 1), 
                                range(c_start, c_end + 1)):
                if grid[r][c] == 1:
                    min_row = min(min_row, r)
                    min_col = min(min_col, c)
                    max_row = max(max_row, r)
                    max_col = max(max_col, c)

            if min_row == float('inf'): 
                return 0
            return (max_row - min_row + 1) * (max_col - min_col + 1)

        def horz_tricolor(comb):
            r1, r2 = comb
            return (area(0,0,r1,n-1)+area(r1+1,0,r2,n-1)+area(r2+1,0,m-1,n-1))

        def vert_tricolor(comb):
            c1, c2 = comb
            return(area(0,0,m-1,c1)+area(0,c1+1,m-1,c2)+area(0,c2+1,m-1,n-1))

        def tripatch(coord):
            r, c = coord
            top, bot, lft, rgt = (
                area(0, 0, r, n-1)  , area(r+1, 0,m-1, n-1),
                area(0, 0, m-1, c)  , area(0, c+1,  m-1, n-1))

            toplft, toprgt, botlft, botrgt = (
                area(0, 0, r, c)    , area(0, c+1, r, n-1),
                area(r+1, 0, m-1, c), area(r+1, c+1, m-1, n-1))              

            return min(top + botlft + botrgt, bot + toplft + toprgt,
                       lft + toprgt + botrgt, rgt + toplft + botlft)

        m, n = len(grid), len(grid[0])

        return min(min(map(tripatch, product(range(m), range(n))  )),
                   min(map(horz_tricolor, combinations(range(m),2))),
                   min(map(vert_tricolor, combinations(range(n),2))))